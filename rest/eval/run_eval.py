import csv
import json
import os
import sys
from pathlib import Path

# Ensure we can import chat_rag from project root when running inside eval/
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from chat_rag import OllamaRAGChat


def load_questions(csv_path: Path):
    questions = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header row
        for row in reader:
            if not row or len(row) < 4:
                continue
            num = row[0].strip()  # Column 0 is "broj"
            q = row[1].strip()  # Column 1 is "pitanje"
            org_answer = row[3].strip()  # Column 3 is "odgovor"
            if q:
                questions.append({
                    'num': num,
                    'question': q,
                    'org_answer': org_answer
                })
    return questions


def main():
    eval_dir = Path(__file__).resolve().parent
    csv_file = eval_dir / 'pitanja_prva_faza.csv'
    out_file = eval_dir / 'answers_prva_faza.json'

    if not csv_file.exists():
        print(f"❌ Missing CSV file: {csv_file}")
        sys.exit(1)

    questions = load_questions(csv_file)
    if not questions:
        print("⚠️ No questions found in CSV.")
        sys.exit(1)

    # Initialize chat (reads config.json internally)
    chat = OllamaRAGChat()

    # Load existing results if file exists
    results = []
    start_idx = 1
    if out_file.exists():
        with open(out_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
        start_idx = len(results) + 1
        print(f"📂 Resuming from question {start_idx} (loaded {len(results)} previous answers)")

    for idx, q_data in enumerate(questions, 1):
        if idx < start_idx:
            continue
        print(f"\n[{idx}/{len(questions)}] ❓ {q_data['question']}")
        try:
            answer = chat.chat(q_data['question'])
        except Exception as e:
            answer = f"Error: {e}"
        results.append({
            "num": q_data['num'],
            "question": q_data['question'],
            "org_answer": q_data['org_answer'],
            "answer": answer
        })
        
        # Save every 10 questions to avoid losing work
        if idx % 10 == 0:
            with open(out_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"💾 Checkpoint: Saved {idx} answers to {out_file}")

    # Final save
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Saved all {len(results)} answers to {out_file}")


if __name__ == '__main__':
    main()
