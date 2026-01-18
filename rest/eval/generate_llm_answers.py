#!/usr/bin/env python3
"""
Skripta za generisanje LLM odgovora za evaluaciju.
Učitava pitanja iz CSV fajla i generiše odgovore pomoću chat_rag_api.py
"""

import json
import csv
import sys
import os
import re
from pathlib import Path

# Dodaj parent direktorijum u sys.path da možemo importovati chat_rag_api
parent_dir = str(Path(__file__).parent.parent)
sys.path.insert(0, parent_dir)

from chat_rag_api import OllamaRAGChat


def get_next_file_number(output_file, eval_dir):
    """
    Pronalazi sledeći broj za fajl na osnovu postojećih fajlova.
    """
    # Izvuci bazno ime fajla (bez .json)
    base_name = output_file.replace('.json', '')
    
    # Traži sve fajlove sa istim baznim imenom
    pattern = re.compile(rf"{re.escape(base_name)}_(\d+)\.json")
    max_num = 0
    
    for file_path in eval_dir.glob(f"{base_name}_*.json"):
        match = pattern.match(file_path.name)
        if match:
            num = int(match.group(1))
            max_num = max(max_num, num)
    
    return max_num + 1


def generate_llm_answers(input_file="temp_input.json", output_file="llm_answers.json", config_path=None):
    """
    Generise LLM odgovore za sva pitanja iz input fajla.
    
    Args:
        input_file: JSON fajl sa pitanjima i očekivanim odgovorima
        output_file: Izlazni JSON fajl sa pitanjima, očekivanim i LLM odgovorima
        config_path: Putanja do config.json fajla (opciono)
    """
    
    # Postavi putanje
    eval_dir = Path(__file__).parent
    input_path = eval_dir / input_file
    
    # Dodaj broj na output fajl
    next_num = get_next_file_number(output_file, eval_dir)
    base_name = output_file.replace('.json', '')
    numbered_output_file = f"{base_name}_{next_num}.json"
    output_path = eval_dir / numbered_output_file
    
    if config_path is None:
        config_path = eval_dir.parent / "config.json"
    
    print("="*100)
    print("GENERISANJE LLM ODGOVORA ZA EVALUACIJU")
    print("="*100)
    print(f"📂 Input: {input_path}")
    print(f"📂 Output: {output_path}")
    print(f"📂 Config: {config_path}")
    print("="*100 + "\n")
    
    # Učitaj pitanja iz JSON (već filtrirana)
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            questions_data = json.load(f)
        print(f"✅ Učitano {len(questions_data)} pitanja\n")
    except Exception as e:
        print(f"❌ Greška pri učitavanju pitanja: {e}")
        return
    
    # Inicijalizuj RAG chat
    try:
        print("🤖 Inicijalizujem RAG sistem...\n")
        chat = OllamaRAGChat(config_path=str(config_path))
    except Exception as e:
        print(f"❌ Greška pri inicijalizaciji RAG sistema: {e}")
        return
    
    # Generisi odgovore
    results = []
    total = len(questions_data)
    
    for idx, item in enumerate(questions_data, 1):
        question = item.get("question", "")
        expected_answer = item.get("answer", "")
        num = item.get("num", str(idx))
        
        print(f"\n{'='*100}")
        print(f"📝 Pitanje {idx}/{total} (#{num})")
        print(f"{'='*100}")
        print(f"❓ {question}\n")
        
        try:
            # Resetuj konverzaciju pre svakog pitanja za clean state
            chat.reset_conversation()
            
            # Dobij odgovor od LLM-a
            llm_answer = chat.chat(question)
            
            # Sačuvaj rezultat
            result = {
                "num": num,
                "question": question,
                "answer": expected_answer,
                "llm_answer": llm_answer
            }
            results.append(result)
            
            print(f"\n✅ Odgovor generisan ({idx}/{total})")
            
        except Exception as e:
            print(f"\n❌ Greška pri generisanju odgovora za pitanje #{num}: {e}")
            # Dodaj sa praznim odgovorom
            result = {
                "num": num,
                "question": question,
                "answer": expected_answer,
                "llm_answer": f"ERROR: {str(e)}"
            }
            results.append(result)
        
        # Sačuvaj međurezultate nakon svakih 10 pitanja
        if idx % 10 == 0 or idx == total:
            try:
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                print(f"💾 Progres sačuvan: {idx}/{total} pitanja")
            except Exception as e:
                print(f"⚠️ Greška pri čuvanju progresa: {e}")
    
    # Sačuvaj finalne rezultate
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\n{'='*100}")
        print(f"✅ Generisanje završeno!")
        print(f"📊 Ukupno: {len(results)} odgovora")
        print(f"💾 Rezultati sačuvani u: {output_path}")
        print(f"{'='*100}\n")
    except Exception as e:
        print(f"\n❌ Greška pri čuvanju finalnih rezultata: {e}")


def main():
    """Main funkcija sa CLI argumentima."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generiši LLM odgovore za evaluaciju")
    parser.add_argument(
        "--input",
        default="pitanja_prva_faza.csv",
        help="Input CSV fajl sa pitanjima (default: pitanja_prva_faza.csv)"
    )
    parser.add_argument(
        "--output",
        default="llm_answers.json",
        help="Output JSON fajl za rezultate (default: llm_answers.json)"
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Putanja do config.json fajla (default: ../config.json)"
    )
    parser.add_argument(
        "--start",
        type=int,
        default=None,
        help="Počni od N-tog pitanja (za nastavak)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Procesuiraj samo prvih N pitanja"
    )
    
    args = parser.parse_args()
    
    # Učitaj pitanja iz CSV
    eval_dir = Path(__file__).parent
    input_path = eval_dir / args.input
    
    questions_data = []
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pitanje = row.get("pitanje", "").strip()
            if pitanje:
                questions_data.append({
                    "num": row.get("broj", "").strip(),
                    "question": pitanje,
                    "answer": row.get("odgovor", "").strip()
                })
    
    # Filtriraj po start/limit ako je potrebno
    if args.start:
        questions_data = questions_data[args.start - 1:]
        print(f"ℹ️  Počinjem od pitanja #{args.start}")
    
    if args.limit:
        questions_data = questions_data[:args.limit]
        print(f"ℹ️  Procesuiram samo prvih {args.limit} pitanja")
    
    # Sačuvaj filtrirani dataset privremeno
    temp_input = eval_dir / "temp_input.json"
    with open(temp_input, "w", encoding="utf-8") as f:
        json.dump(questions_data, f, ensure_ascii=False, indent=2)
    
    # Pozovi funkciju sa temp JSON fajlom
    generate_llm_answers(
        input_file="temp_input.json",
        output_file=args.output,
        config_path=args.config
    )
    
    # Obriši temp fajl
    temp_input.unlink()


if __name__ == "__main__":
    main()
