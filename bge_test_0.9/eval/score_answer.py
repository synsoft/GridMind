#!/usr/bin/env python3
"""
Skripta za scoring LLM odgovora u odnosu na originalne odgovore.
Koristi LLM (Ollama ili OpenAI) za poređenje i davanje score-a od 0 do 1.
"""

import json
import os
import glob
import requests
from typing import List, Dict, Any


def load_config(config_path: str = "../config.json") -> Dict[str, Any]:
    """Učitava config fajl."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_latest_llm_answers_file() -> str:
    """Pronalazi poslednji llm_answers_*.json fajl."""
    pattern = "llm_answers_*.json"
    files = glob.glob(pattern)
    
    if not files:
        raise FileNotFoundError(f"Nema fajlova koji odgovaraju pattern-u {pattern}")
    
    # Sortiranje po broju u imenu fajla
    def extract_number(filename):
        try:
            # Izvlači broj iz llm_answers_X.json
            return int(filename.replace("llm_answers_", "").replace(".json", ""))
        except:
            return 0
    
    files.sort(key=extract_number)
    return files[-1]


def load_llm_answers(filepath: str) -> List[Dict[str, Any]]:
    """Učitava LLM odgovore iz fajla."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def call_ollama(host: str, port: int, model: str, prompt: str) -> str:
    """Poziva Ollama server za scoring."""
    url = f"http://{host}:{port}/api/generate"
    
    system_prompt = "You are a scoring assistant. Provide a score and brief explanation in the requested format."
    full_prompt = f"{system_prompt}\n\n{prompt}"
    
    payload = {
        "model": model,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 200
        }
    }
    
    try:
        print(f"    Pozivam Ollama server: {url} (model: {model})")
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()["response"]
        print(f"    Primljen odgovor ({len(result)} karaktera)")
        return result
    except requests.exceptions.Timeout:
        print(f"    GREŠKA: Timeout pri pozivu servera (120s)")
        return ""
    except requests.exceptions.ConnectionError as e:
        print(f"    GREŠKA: Nije moguće povezati se sa serverom: {e}")
        return ""
    except Exception as e:
        print(f"    GREŠKA: {type(e).__name__}: {e}")
        return ""


def call_openai(host: str, port: int, prompt: str) -> str:
    """Poziva OpenAI-compatible server za scoring."""
    url = f"http://{host}:{port}/v1/chat/completions"
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.1,
        "max_tokens": 500
    }
    
    try:
        print(f"    Pozivam OpenAI server: {url}")
        print(f"    Prompt length: {len(payload['messages'][0]['content'])} chars")
        print(f"    Prompt preview: {payload['messages'][0]['content'][:150]}...")
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        
        response_json = response.json()
        
        # Pokušaj različite strukture
        if "choices" in response_json and len(response_json["choices"]) > 0:
            choice = response_json["choices"][0]
            if "message" in choice:
                message = choice["message"]
                # Za Qwen3 thinking models - kombinuj reasoning i content
                reasoning = message.get("reasoning_content", "")
                content = message.get("content", "")
                
                # Ako ima content (finalni odgovor), koristi njega
                if content:
                    result = content
                    print(f"    Koristi content ({len(content)} karaktera)")
                # Ako nema content, koristi reasoning
                elif reasoning:
                    result = reasoning
                    print(f"    Koristi reasoning_content ({len(reasoning)} karaktera)")
                else:
                    print(f"    Poruka nema content ni reasoning_content")
                    result = ""
            elif "text" in choice:
                result = choice["text"]
            else:
                print(f"    Nepoznata struktura choices: {choice}")
                result = ""
        else:
            print(f"    Nema 'choices' u odgovoru")
            result = ""
            
        print(f"    Primljen odgovor: '{result[:200]}...'")
        return result
    except requests.exceptions.Timeout:
        print(f"    GREŠKA: Timeout pri pozivu servera (120s)")
        return ""
    except requests.exceptions.ConnectionError as e:
        print(f"    GREŠKA: Nije moguće povezati se sa serverom: {e}")
        return ""
    except Exception as e:
        print(f"    GREŠKA: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return ""


def create_scoring_prompt(original_answer: str, llm_answer: str) -> str:
    """Kreira prompt za scoring."""
    prompt = f"""Compare two answers and rate semantic similarity 0.0-1.0.

Original: {original_answer}

LLM: {llm_answer}

Rules:
- 1.0 = same core meaning
- 0.8-0.9 = LLM longer but has all key info
- 0.5-0.7 = partially similar
- 0.0 = different

Reply:
SCORE: [number]
EXPLANATION: [Serbian, 1-2 sentences]"""
    
    return prompt


def parse_score_and_explanation(llm_response: str) -> tuple[float, str]:
    """Parsira score i objašnjenje iz LLM odgovora."""
    import re
    
    score = 0.0
    explanation = ""
    
    try:
        # Prvo traži eksplicitno "SCORE:" format
        score_match = re.search(r'SCORE:\s*(\d+\.?\d*)', llm_response, re.IGNORECASE)
        explanation_match = re.search(r'EXPLANATION:\s*(.+?)(?:\n\n|\n?$)', llm_response, re.IGNORECASE | re.DOTALL)
        
        if score_match:
            score = float(score_match.group(1))
            if score > 1.0:
                score = score / 10.0
            score = max(0.0, min(1.0, score))
            
        # Ako nema SCORE: tag, traži bilo koji broj sa kontekstom
        if score == 0.0:
            # Traži pattern kao "score is 0.X" ili "I give X" ili samo decimalni broj
            patterns = [
                r'(?:score|rating|ocena|ocene)\s*(?:is|je|:)?\s*(\d+\.?\d*)',
                r'(?:give|dajem|dati)\s*(?:a|an)?\s*(?:score|rating)?\s*(?:of)?\s*(\d+\.?\d*)',
                r'\b([0-1]\.\d+)\b',  # Decimalni broj između 0 i 1
                r'\b(0\.\d+|1\.0)\b'  # Još specifičniji za score format
            ]
            
            for pattern in patterns:
                match = re.search(pattern, llm_response, re.IGNORECASE)
                if match:
                    score = float(match.group(1))
                    if score > 1.0:
                        score = score / 10.0
                    score = max(0.0, min(1.0, score))
                    break
        
        # Parsiranje objašnjenja
        if explanation_match:
            explanation = explanation_match.group(1).strip()
        else:
            # Uzmi deo nakon score-a ili ceo odgovor
            if score > 0:
                parts = re.split(r'SCORE:\s*\d+\.?\d*', llm_response, flags=re.IGNORECASE)
                if len(parts) > 1:
                    explanation = parts[1].strip()[:300]  # Prvi deo nakon score-a
                else:
                    explanation = llm_response.strip()[:300]
            else:
                explanation = llm_response.strip()[:300]
            
    except Exception as e:
        print(f"Greška pri parsiranju: {e}")
        explanation = llm_response.strip()[:300]
    
    if score == 0.0:
        print(f"Upozorenje: Nije pronađen score u odgovoru")
        explanation = f"Parser nije pronašao score. Raw: {llm_response[:200]}"
    
    return score, explanation


def score_answers(config: Dict[str, Any], data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Scoruje sve odgovore."""
    provider = config["llm"]["provider"]
    results = []
    
    for i, item in enumerate(data):
        print(f"Scoring pitanje {i+1}/{len(data)}: {item['num']}")
        
        original = item["answer"]
        llm_ans = item["llm_answer"]
        
        # Kreira prompt
        prompt = create_scoring_prompt(original, llm_ans)
        
        # Poziva odgovarajući LLM
        if provider == "ollama":
            host = config["llm"]["ollama_host"]
            port = config["llm"]["ollama_port"]
            model = config["llm"]["model"]
            llm_response = call_ollama(host, port, model, prompt)
        elif provider == "openai":
            host = config["llm"]["openai_host"]
            port = config["llm"]["openai_port"]
            llm_response = call_openai(host, port, prompt)
        else:
            print(f"Nepoznat provider: {provider}")
            llm_response = "0.0"
        
        # Parsira score i objašnjenje
        score, explanation = parse_score_and_explanation(llm_response)
        
        # Dodaje score i objašnjenje u rezultat
        result = item.copy()
        result["score"] = score
        result["llm_thinking"] = explanation
        results.append(result)
        
        print(f"  Score: {score}")
        print(f"  Thinking: {explanation[:100]}...")
    
    return results


def save_results(data: List[Dict[str, Any]], input_filename: str):
    """Čuva rezultate u novi JSON fajl."""
    # Sortira po score-u (od najnižeg ka najvišem)
    sorted_data = sorted(data, key=lambda x: x["score"])
    
    # Kreira ime output fajla
    base_name = input_filename.replace("llm_answers_", "llm_scores_")
    output_filename = base_name
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nRezultati sačuvani u: {output_filename}")
    
    # Ispisuje statistiku
    scores = [item["score"] for item in data]
    avg_score = sum(scores) / len(scores) if scores else 0
    print(f"\nStatistika:")
    print(f"  Ukupno pitanja: {len(data)}")
    print(f"  Prosečan score: {avg_score:.3f}")
    print(f"  Min score: {min(scores):.3f}")
    print(f"  Max score: {max(scores):.3f}")


def main():
    """Glavna funkcija."""
    # Učitava config
    config = load_config()
    print(f"Provider: {config['llm']['provider']}")
    
    # Pronalazi poslednji llm_answers fajl
    input_file = get_latest_llm_answers_file()
    print(f"Učitavam fajl: {input_file}")
    
    # Učitava podatke
    data = load_llm_answers(input_file)
    print(f"Učitano {len(data)} pitanja")
    
    # Scoruje odgovore
    print("\nPokrećem scoring...\n")
    results = score_answers(config, data)
    
    # Čuva rezultate
    save_results(results, input_file)


if __name__ == "__main__":
    main()
