#!/usr/bin/env python3
"""
Generate BGE-M3 Reranker finetune dataset from eval results.
Format: {"query": "...", "pos": ["..."], "neg": ["...", "..."]}
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# Config
MAX_HARD_NEGATIVES = 20
MIN_NEG_SCORE = 0.6
INCLUDE_FAILED = False

EVAL_DIR = Path(__file__).parent.parent / "eval"
OUTPUT_DIR = Path(__file__).parent.parent / "output"
CHUNKS_FILE = OUTPUT_DIR / "all_chunks.jsonl"
EVAL_RESULTS_FILE = EVAL_DIR / "eval_results.txt"
EVAL_ALL_FILE = EVAL_DIR / "eval_all.json"
OUTPUT_FILE = EVAL_DIR / "finetune_reranker.jsonl"


def load_chunks():
    """Load all chunks and index by file_num:section_number"""
    chunks = {}
    with open(CHUNKS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            chunk = json.loads(line)
            # Key format: "8.05:5.2"
            key = f"{chunk['file_num']}:{chunk['section_number']}"
            chunks[key] = chunk['content']
    print(f"Loaded {len(chunks)} chunks")
    return chunks


def load_eval_variants():
    """Load text variants from eval_all.json"""
    variants = {}
    with open(EVAL_ALL_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data.get('data', []):
        question = item.get('text', '')
        all_variants = [question] + item.get('text_variants', [])
        variants[item['id']] = all_variants
        # Also index by question text for matching
        variants[question.lower().strip()] = all_variants
    
    print(f"Loaded variants for {len(data.get('data', []))} questions")
    return variants


def parse_eval_results():
    """Parse eval_results.txt to extract PASSED questions with retrieved/expected"""
    results = []
    
    with open(EVAL_RESULTS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find PASSED section
    passed_match = re.search(r'PASSED \(\d+\):\n-+\n(.+?)(?:\n\n[A-Z]|\Z)', content, re.DOTALL)
    if not passed_match:
        print("ERROR: Could not find PASSED section")
        return results
    
    passed_section = passed_match.group(1)
    
    # Parse each question block
    # Pattern: [  0] Question text\n  Retrieved: [...]\n  Expected: [...]\n  Matches: [...]\n  PASS
    pattern = r'\[\s*(\d+)\]\s+(.+?)\n\s+Retrieved:\s+\[([^\]]+)\]\n\s+Expected:\s+\[([^\]]+)\]\n\s+Matches:\s+\[([^\]]*)\]\n\s+PASS'
    
    for match in re.finditer(pattern, passed_section):
        qid = int(match.group(1))
        question = match.group(2).strip()
        retrieved_str = match.group(3)
        expected_str = match.group(4)
        
        # Parse retrieved: '8.05:5.2:1.000', '8.05:5.1:1.000', ...
        retrieved = []
        for item in re.findall(r"'([^']+)'", retrieved_str):
            parts = item.split(':')
            if len(parts) >= 3:
                chunk_id = f"{parts[0]}:{parts[1]}"
                score = float(parts[2])
                retrieved.append((chunk_id, score))
        
        # Parse expected: '8.05:5.1', '8.05:5.2'
        expected = set()
        for item in re.findall(r"'([^']+)'", expected_str):
            expected.add(item)
        
        results.append({
            'id': qid,
            'question': question,
            'retrieved': retrieved,
            'expected': expected
        })
    
    print(f"Parsed {len(results)} PASSED questions")
    return results


def generate_finetune_data(results, chunks, variants):
    """Generate finetune dataset"""
    finetune_data = []
    stats = {
        'total_examples': 0,
        'skipped_no_pos': 0,
        'skipped_no_neg': 0,
        'total_with_variants': 0
    }
    
    for result in results:
        question = result['question']
        expected = result['expected']
        retrieved = result['retrieved']
        
        # Get positive chunk texts
        pos_texts = []
        for exp_id in expected:
            if exp_id in chunks:
                pos_texts.append(chunks[exp_id])
        
        if not pos_texts:
            stats['skipped_no_pos'] += 1
            continue
        
        # Get hard negatives (retrieved but not expected, score >= MIN_NEG_SCORE)
        neg_texts = []
        for chunk_id, score in retrieved:
            if chunk_id not in expected and score >= MIN_NEG_SCORE:
                if chunk_id in chunks:
                    neg_texts.append(chunks[chunk_id])
                    if len(neg_texts) >= MAX_HARD_NEGATIVES:
                        break
        
        if not neg_texts:
            stats['skipped_no_neg'] += 1
            continue
        
        # Get all query variants
        query_variants = [question]
        question_key = question.lower().strip()
        if question_key in variants:
            query_variants = variants[question_key]
        
        # Create examples for each variant
        for query in query_variants:
            finetune_data.append({
                'query': query,
                'pos': pos_texts,
                'neg': neg_texts
            })
            stats['total_examples'] += 1
        
        if len(query_variants) > 1:
            stats['total_with_variants'] += 1
    
    return finetune_data, stats


def main():
    print("=" * 60)
    print("BGE-M3 Reranker Finetune Dataset Generator")
    print("=" * 60)
    print(f"Config: max_negatives={MAX_HARD_NEGATIVES}, min_score={MIN_NEG_SCORE}")
    print()
    
    # Load data
    chunks = load_chunks()
    variants = load_eval_variants()
    results = parse_eval_results()
    
    # Generate finetune data
    finetune_data, stats = generate_finetune_data(results, chunks, variants)
    
    # Write output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for item in finetune_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    print()
    print("=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Total examples generated: {stats['total_examples']}")
    print(f"Questions with variants: {stats['total_with_variants']}")
    print(f"Skipped (no positive chunks): {stats['skipped_no_pos']}")
    print(f"Skipped (no hard negatives): {stats['skipped_no_neg']}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
