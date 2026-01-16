#!/usr/bin/env python3
"""
Generisanje sintetičkih pitanja iz chunk-ova za finetune reranker-a.

Koristi LLM (Ollama lokalno ili Anthropic API) da generiše pitanja 
na osnovu svakog chunk-a iz dokumentacije.
"""

import json
import random
import argparse
import os
import sys
import time
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# ============================================================
# KONFIGURACIJA
# ============================================================

@dataclass
class Config:
    """Konfiguracija za generisanje sintetičkih pitanja."""
    
    # Putanje
    chunks_file: str = "/home/synsoft/gridmind_v0.9/chunks/output/all_chunks.jsonl"
    output_file: str = "/home/synsoft/gridmind_v0.9/chunks/finetune_rerank/synthetic_questions.jsonl"
    
    # LLM konfiguracija
    llm_provider: str = "ollama"  # "ollama" ili "anthropic"
    ollama_model: str = "llama3.2:latest"  # ili "mistral", "gemma2", itd.
    ollama_base_url: str = "http://localhost:11434"
    anthropic_model: str = "claude-sonnet-4-20250514"
    
    # Generisanje
    questions_per_chunk: int = 2  # koliko pitanja po chunk-u
    target_questions: int = 2000  # ukupno ciljani broj pitanja
    min_chunk_length: int = 100  # minimalna dužina chunk-a za razmatranje
    max_workers: int = 4  # paralelni workers za API pozive
    
    # Hard negatives
    num_hard_negatives: int = 20
    
    # Retry konfiguracija
    max_retries: int = 3
    retry_delay: float = 1.0


# ============================================================
# LLM PROMPT
# ============================================================

SYSTEM_PROMPT = """Ti si ekspert za elektroenergetske sisteme (EES) i trafostanice.
Tvoj zadatak je da generiješ realistična pitanja koja bi dispečer ili inženjer postavio
na osnovu datog teksta iz tehničke dokumentacije.

Pravila:
1. Pitanja moraju biti konkretna i direktno vezana za sadržaj teksta
2. Koristi tehničku terminologiju iz elektroenergetike
3. Pitanja mogu biti o postupcima, pravilima, manipulacijama, kvarovima
4. Pitanja mogu biti na srpskom (latinica ili ćirilica) ili kombinacija
5. Varijacije: "šta", "kako", "koji", "kada", "da li", "objasni", "napiši", itd.
6. Pitanja treba da budu prirodna, kao da ih postavlja pravi dispečer

Primeri dobrih pitanja:
- "Koji je postupak za prebacivanje dalekovoda na pomoćni sistem sabirnica?"
- "Колико времена има диспечер за растерећење далековода при првом степену преоптерећења?"
- "da li dispecer sme da ukljuci vod posle APU?"
"""

USER_PROMPT_TEMPLATE = """Na osnovu sledećeg teksta iz tehničke dokumentacije, generiši {n} različita pitanja.

TEKST:
---
{text}
---

IZVOR: {source}
SEKCIJA: {section}

Generiši {n} pitanja u JSON formatu:
{{"questions": ["pitanje1", "pitanje2", ...]}}

Samo JSON, bez dodatnog teksta."""


# ============================================================
# LLM KLIJENTI
# ============================================================

class OllamaClient:
    """Klijent za Ollama API."""
    
    def __init__(self, base_url: str, model: str):
        self.base_url = base_url.rstrip('/')
        self.model = model
        
    def generate(self, prompt: str, system_prompt: str = None) -> str:
        """Generiši tekst koristeći Ollama."""
        import requests
        
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "num_predict": 500
                }
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json()["message"]["content"]


class AnthropicClient:
    """Klijent za Anthropic API."""
    
    def __init__(self, model: str, api_key: str = None):
        self.model = model
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY nije postavljen!")
        
    def generate(self, prompt: str, system_prompt: str = None) -> str:
        """Generiši tekst koristeći Anthropic API."""
        import requests
        
        headers = {
            "x-api-key": self.api_key,
            "content-type": "application/json",
            "anthropic-version": "2023-06-01"
        }
        
        data = {
            "model": self.model,
            "max_tokens": 500,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        
        if system_prompt:
            data["system"] = system_prompt
            
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data,
            timeout=60
        )
        response.raise_for_status()
        return response.json()["content"][0]["text"]


# ============================================================
# GENERISANJE PITANJA
# ============================================================

def load_chunks(chunks_file: str, min_length: int = 100) -> List[Dict]:
    """Učitaj chunk-ove iz JSONL fajla."""
    chunks = []
    with open(chunks_file, 'r', encoding='utf-8') as f:
        for line in f:
            chunk = json.loads(line.strip())
            if len(chunk.get('text', '')) >= min_length:
                chunks.append(chunk)
    return chunks


def parse_questions_response(response: str) -> List[str]:
    """Parsuj JSON odgovor sa pitanjima."""
    # Pokušaj da pronađeš JSON u odgovoru
    try:
        # Probaj direktno parsiranje
        data = json.loads(response)
        if isinstance(data, dict) and 'questions' in data:
            return data['questions']
        elif isinstance(data, list):
            return data
    except json.JSONDecodeError:
        pass
    
    # Pokušaj da nađeš JSON u tekstu
    import re
    json_match = re.search(r'\{[\s\S]*"questions"[\s\S]*\}', response)
    if json_match:
        try:
            data = json.loads(json_match.group())
            return data.get('questions', [])
        except json.JSONDecodeError:
            pass
    
    # Poslednja opcija - pronađi listu
    list_match = re.search(r'\[[\s\S]*\]', response)
    if list_match:
        try:
            return json.loads(list_match.group())
        except json.JSONDecodeError:
            pass
    
    return []


def generate_questions_for_chunk(
    chunk: Dict,
    client,
    config: Config
) -> Tuple[Dict, List[str]]:
    """Generiši pitanja za jedan chunk."""
    
    text = chunk.get('text', '')
    source = chunk.get('source', 'nepoznato')
    section = chunk.get('section', 'nepoznato')
    
    prompt = USER_PROMPT_TEMPLATE.format(
        n=config.questions_per_chunk,
        text=text[:2000],  # Limitiraj tekst
        source=source,
        section=section
    )
    
    for attempt in range(config.max_retries):
        try:
            response = client.generate(prompt, SYSTEM_PROMPT)
            questions = parse_questions_response(response)
            
            # Filtriraj prazna pitanja
            questions = [q.strip() for q in questions if q and len(q.strip()) > 10]
            
            return chunk, questions
            
        except Exception as e:
            if attempt < config.max_retries - 1:
                time.sleep(config.retry_delay * (attempt + 1))
            else:
                print(f"  ⚠ Greška za chunk {chunk.get('chunk_id', 'N/A')}: {e}")
                return chunk, []
    
    return chunk, []


def generate_synthetic_dataset(config: Config):
    """Glavna funkcija za generisanje sintetičkih pitanja."""
    
    print("=" * 60)
    print("GENERISANJE SINTETIČKIH PITANJA ZA FINETUNE")
    print("=" * 60)
    
    # Učitaj chunk-ove
    print(f"\nUčitavanje chunk-ova iz: {config.chunks_file}")
    all_chunks = load_chunks(config.chunks_file, config.min_chunk_length)
    print(f"✓ Učitano {len(all_chunks)} chunk-ova (min dužina: {config.min_chunk_length})")
    
    # Izračunaj koliko chunk-ova treba obraditi
    chunks_needed = config.target_questions // config.questions_per_chunk
    if chunks_needed > len(all_chunks):
        chunks_needed = len(all_chunks)
        print(f"  Upozorenje: Nema dovoljno chunk-ova za {config.target_questions} pitanja")
    
    # Nasumično izaberi chunk-ove
    selected_chunks = random.sample(all_chunks, chunks_needed)
    print(f"  Izabrano {len(selected_chunks)} chunk-ova za obradu")
    
    # Kreiraj LLM klijent
    print(f"\nLLM Provider: {config.llm_provider}")
    if config.llm_provider == "ollama":
        print(f"  Model: {config.ollama_model}")
        print(f"  URL: {config.ollama_base_url}")
        client = OllamaClient(config.ollama_base_url, config.ollama_model)
    else:
        print(f"  Model: {config.anthropic_model}")
        client = AnthropicClient(config.anthropic_model)
    
    # Generiši pitanja
    print(f"\nGenerisanje {config.questions_per_chunk} pitanja po chunk-u...")
    print(f"Paralelni workers: {config.max_workers}")
    
    results = []
    total_questions = 0
    
    # Koristi ThreadPoolExecutor za paralelizaciju
    with ThreadPoolExecutor(max_workers=config.max_workers) as executor:
        futures = {
            executor.submit(generate_questions_for_chunk, chunk, client, config): chunk
            for chunk in selected_chunks
        }
        
        pbar = tqdm(as_completed(futures), total=len(selected_chunks), desc="Generisanje")
        for future in pbar:
            chunk, questions = future.result()
            
            if questions:
                for q in questions:
                    results.append({
                        "query": q,
                        "chunk_id": chunk.get("chunk_id", ""),
                        "chunk_text": chunk.get("text", ""),
                        "source": chunk.get("source", ""),
                        "section": chunk.get("section", ""),
                        "ts_code": chunk.get("ts_code", "")
                    })
                    total_questions += 1
                    
            pbar.set_postfix({"pitanja": total_questions})
    
    print(f"\n✓ Generisano {total_questions} pitanja")
    
    # Sačuvaj rezultate
    print(f"\nČuvanje u: {config.output_file}")
    os.makedirs(os.path.dirname(config.output_file), exist_ok=True)
    
    with open(config.output_file, 'w', encoding='utf-8') as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    
    print(f"✓ Sačuvano {len(results)} pitanja")
    
    return results


def create_finetune_dataset(
    synthetic_file: str,
    all_chunks_file: str,
    output_file: str,
    num_negatives: int = 20
):
    """Kreiraj finetune dataset sa hard negatives."""
    
    print("\n" + "=" * 60)
    print("KREIRANJE FINETUNE DATASET-A")
    print("=" * 60)
    
    # Učitaj sintetička pitanja
    print(f"\nUčitavanje sintetičkih pitanja iz: {synthetic_file}")
    synthetic = []
    with open(synthetic_file, 'r', encoding='utf-8') as f:
        for line in f:
            synthetic.append(json.loads(line.strip()))
    print(f"✓ Učitano {len(synthetic)} pitanja")
    
    # Učitaj sve chunk-ove
    print(f"Učitavanje svih chunk-ova iz: {all_chunks_file}")
    all_chunks = load_chunks(all_chunks_file)
    chunk_texts = [c.get('text', '') for c in all_chunks]
    chunk_ids = [c.get('chunk_id', '') for c in all_chunks]
    print(f"✓ Učitano {len(all_chunks)} chunk-ova")
    
    # Kreiraj ID -> tekst mapu
    id_to_text = {c.get('chunk_id', ''): c.get('text', '') for c in all_chunks}
    
    # Generiši finetune primere
    print(f"\nGenerisanje finetune primera sa {num_negatives} negativnih primera...")
    
    finetune_examples = []
    for item in tqdm(synthetic, desc="Kreiranje primera"):
        query = item['query']
        pos_text = item['chunk_text']
        pos_chunk_id = item['chunk_id']
        
        # Izaberi negativne primere (isključi pozitivni)
        neg_candidates = [
            (cid, text) for cid, text in id_to_text.items() 
            if cid != pos_chunk_id and text != pos_text
        ]
        
        if len(neg_candidates) < num_negatives:
            continue
            
        neg_samples = random.sample(neg_candidates, num_negatives)
        neg_texts = [text for _, text in neg_samples]
        
        finetune_examples.append({
            "query": query,
            "pos": [pos_text],
            "neg": neg_texts
        })
    
    print(f"✓ Kreirano {len(finetune_examples)} finetune primera")
    
    # Sačuvaj
    print(f"\nČuvanje u: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        for ex in finetune_examples:
            f.write(json.dumps(ex, ensure_ascii=False) + '\n')
    
    print(f"✓ Sačuvano {len(finetune_examples)} primera")
    
    return finetune_examples


def merge_finetune_datasets(
    original_file: str,
    synthetic_file: str,
    output_file: str
):
    """Spoji originalni i sintetički finetune dataset."""
    
    print("\n" + "=" * 60)
    print("SPAJANJE FINETUNE DATASET-A")
    print("=" * 60)
    
    all_examples = []
    
    # Učitaj originalni
    print(f"\nUčitavanje originalnog dataset-a: {original_file}")
    with open(original_file, 'r', encoding='utf-8') as f:
        for line in f:
            all_examples.append(json.loads(line.strip()))
    original_count = len(all_examples)
    print(f"✓ Učitano {original_count} originalnih primera")
    
    # Učitaj sintetički
    print(f"Učitavanje sintetičkog dataset-a: {synthetic_file}")
    with open(synthetic_file, 'r', encoding='utf-8') as f:
        for line in f:
            all_examples.append(json.loads(line.strip()))
    synthetic_count = len(all_examples) - original_count
    print(f"✓ Učitano {synthetic_count} sintetičkih primera")
    
    # Promešaj
    random.shuffle(all_examples)
    
    # Sačuvaj
    print(f"\nČuvanje spojenog dataset-a: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        for ex in all_examples:
            f.write(json.dumps(ex, ensure_ascii=False) + '\n')
    
    print(f"✓ Ukupno: {len(all_examples)} primera ({original_count} orig + {synthetic_count} synth)")
    
    return all_examples


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generiši sintetička pitanja za finetune reranker-a"
    )
    
    parser.add_argument(
        "--action",
        choices=["generate", "create-finetune", "merge", "all"],
        default="all",
        help="Akcija: generate, create-finetune, merge, all (default: all)"
    )
    
    parser.add_argument(
        "--provider",
        choices=["ollama", "anthropic"],
        default="ollama",
        help="LLM provider (default: ollama)"
    )
    
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Model name (ollama: llama3.2:latest, anthropic: claude-sonnet-4-20250514)"
    )
    
    parser.add_argument(
        "--target",
        type=int,
        default=2000,
        help="Ciljani broj pitanja (default: 2000)"
    )
    
    parser.add_argument(
        "--questions-per-chunk",
        type=int,
        default=2,
        help="Broj pitanja po chunk-u (default: 2)"
    )
    
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Broj paralelnih workers (default: 4)"
    )
    
    parser.add_argument(
        "--negatives",
        type=int,
        default=20,
        help="Broj hard negatives (default: 20)"
    )
    
    args = parser.parse_args()
    
    # Konfiguracija
    config = Config()
    config.llm_provider = args.provider
    config.target_questions = args.target
    config.questions_per_chunk = args.questions_per_chunk
    config.max_workers = args.workers
    config.num_hard_negatives = args.negatives
    
    if args.model:
        if args.provider == "ollama":
            config.ollama_model = args.model
        else:
            config.anthropic_model = args.model
    
    # Putanje
    finetune_dir = "/home/synsoft/gridmind_v0.9/chunks/finetune_rerank"
    synthetic_questions_file = f"{finetune_dir}/synthetic_questions.jsonl"
    synthetic_finetune_file = f"{finetune_dir}/finetune_synthetic.jsonl"
    original_finetune_file = f"{finetune_dir}/finetune_reranker.jsonl"
    merged_finetune_file = f"{finetune_dir}/finetune_merged.jsonl"
    
    config.output_file = synthetic_questions_file
    
    # Izvrši akcije
    if args.action in ["generate", "all"]:
        generate_synthetic_dataset(config)
    
    if args.action in ["create-finetune", "all"]:
        create_finetune_dataset(
            synthetic_file=synthetic_questions_file,
            all_chunks_file=config.chunks_file,
            output_file=synthetic_finetune_file,
            num_negatives=config.num_hard_negatives
        )
    
    if args.action in ["merge", "all"]:
        merge_finetune_datasets(
            original_file=original_finetune_file,
            synthetic_file=synthetic_finetune_file,
            output_file=merged_finetune_file
        )
    
    print("\n" + "=" * 60)
    print("ZAVRŠENO!")
    print("=" * 60)
    print(f"""
Sledeći korak - treniraj reranker sa svim podacima:

python train_reranker.py \\
    --train-file {merged_finetune_file} \\
    --base-model BAAI/bge-reranker-v2-m3 \\
    --epochs 3

NAPOMENA: Treniraj od ORIGINALNOG modela, ne od finetuned!
""")


if __name__ == "__main__":
    main()
