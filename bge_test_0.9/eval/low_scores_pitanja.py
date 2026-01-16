import json
import csv
from pathlib import Path


def main():
    eval_dir = Path(__file__).resolve().parent
    scores_file = eval_dir / 'scores_prva_faza.json'
    output_file = eval_dir / 'pitanja_low_scores.csv'
    
    # Load scores
    with open(scores_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Filter items with score < 0.8
    low_scores = [item for item in data['results'] if item['score'] < 0.8]
    
    print(f"Found {len(low_scores)} items with score < 0.8")
    
    # Write to CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        
        # Header
        writer.writerow(['broj', 'score', 'pitanje', 'tezina', 'odgovor', 'dokument_i', 'paragraf', 'SYN_komentar'])
        
        # Data rows
        for item in low_scores:
            writer.writerow([
                item['num'],
                f"{item['score']:.1f}",
                item['question'],
                '',  # tezina - empty
                item['org_answer'],
                '',  # dokument_i - empty
                '',  # paragraf - empty
                ''   # SYN_komentar - empty
            ])
    
    print(f"✅ Saved {len(low_scores)} low-scoring questions to {output_file}")


if __name__ == '__main__':
    main()
