#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility funkcije za analizu i validaciju RAG chunk-ova.
"""

import json
from pathlib import Path
from typing import List, Dict
from collections import defaultdict


def load_chunks(filepath: str) -> List[Dict]:
    """Učitava chunk-ove iz JSONL fajla."""
    chunks = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                chunks.append(json.loads(line))
    return chunks


def analyze_chunks(chunks: List[Dict]) -> Dict:
    """Analizira statistike chunk-ova."""
    stats = {
        'total_chunks': len(chunks),
        'by_type': defaultdict(int),
        'by_doc_type': defaultdict(int),
        'by_section_type': defaultdict(int),
        'by_object': defaultdict(int),
        'size_distribution': {
            'min': float('inf'),
            'max': 0,
            'avg': 0,
            'under_200': 0,
            'under_500': 0,
            'under_1000': 0,
            'over_1000': 0
        },
        'voltage_coverage': defaultdict(int)
    }
    
    total_size = 0
    
    for chunk in chunks:
        # Po tipu chunk-a
        stats['by_type'][chunk.get('chunk_type', 'unknown')] += 1
        
        # Po tipu dokumenta
        stats['by_doc_type'][chunk.get('doc_type', 'unknown')] += 1
        
        # Po tipu sekcije
        stats['by_section_type'][chunk.get('section_type', 'unknown')] += 1
        
        # Po objektu
        obj = chunk.get('object_code')
        if obj:
            stats['by_object'][obj] += 1
        
        # Veličina
        size = chunk.get('char_count', 0)
        total_size += size
        stats['size_distribution']['min'] = min(stats['size_distribution']['min'], size)
        stats['size_distribution']['max'] = max(stats['size_distribution']['max'], size)
        
        if size < 200:
            stats['size_distribution']['under_200'] += 1
        elif size < 500:
            stats['size_distribution']['under_500'] += 1
        elif size < 1000:
            stats['size_distribution']['under_1000'] += 1
        else:
            stats['size_distribution']['over_1000'] += 1
        
        # Naponski nivoi
        for voltage in chunk.get('voltage_levels', []):
            stats['voltage_coverage'][voltage] += 1
    
    if chunks:
        stats['size_distribution']['avg'] = total_size / len(chunks)
    
    return stats


def validate_chunk(chunk: Dict) -> List[str]:
    """Validira pojedinačni chunk i vraća listu grešaka."""
    errors = []
    
    required_fields = ['chunk_id', 'content', 'doc_id', 'doc_type', 'chunk_type']
    for field in required_fields:
        if field not in chunk or not chunk[field]:
            errors.append(f"Nedostaje obavezno polje: {field}")
    
    # Provera veličine
    content = chunk.get('content', '')
    if len(content) < 50:
        errors.append(f"Sadržaj prekratak: {len(content)} karaktera")
    elif len(content) > 3000:
        errors.append(f"Sadržaj predugačak: {len(content)} karaktera")
    
    # Provera chunk_type
    valid_types = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    if chunk.get('chunk_type') not in valid_types:
        errors.append(f"Nepoznat chunk_type: {chunk.get('chunk_type')}")
    
    return errors


def find_similar_chunks(chunks: List[Dict], threshold: float = 0.8) -> List[tuple]:
    """Pronalazi potencijalne duplikate na osnovu sličnosti sadržaja."""
    from difflib import SequenceMatcher
    
    similar_pairs = []
    
    for i, chunk1 in enumerate(chunks):
        for j, chunk2 in enumerate(chunks[i+1:], i+1):
            content1 = chunk1.get('content', '')
            content2 = chunk2.get('content', '')
            
            similarity = SequenceMatcher(None, content1, content2).ratio()
            if similarity >= threshold:
                similar_pairs.append((
                    chunk1['chunk_id'],
                    chunk2['chunk_id'],
                    similarity
                ))
    
    return similar_pairs


def generate_report(stats: Dict, output_path: str = None) -> str:
    """Generiše tekstualni izveštaj o chunk-ovima."""
    lines = [
        "=" * 60,
        "IZVEŠTAJ O RAG CHUNK-OVIMA",
        "=" * 60,
        "",
        f"Ukupno chunk-ova: {stats['total_chunks']}",
        "",
        "DISTRIBUCIJA PO TIPU CHUNK-A:",
        "-" * 30
    ]
    
    type_names = {
        'A': 'Pojam iz rečnika',
        'B': 'Eksploatacioni uslov',
        'C': 'Normalno uklopno stanje',
        'D': 'Posebno uklopno stanje',
        'E': 'Paralelan rad',
        'F': 'Pravilo/Odredba',
        'G': 'Opšta sekcija'
    }
    
    for t, count in sorted(stats['by_type'].items()):
        name = type_names.get(t, t)
        lines.append(f"  {t} ({name}): {count}")
    
    lines.extend([
        "",
        "DISTRIBUCIJA PO TIPU DOKUMENTA:",
        "-" * 30
    ])
    
    for doc_type, count in sorted(stats['by_doc_type'].items()):
        lines.append(f"  {doc_type}: {count}")
    
    lines.extend([
        "",
        "VELIČINA CHUNK-OVA:",
        "-" * 30,
        f"  Minimalna: {stats['size_distribution']['min']} karaktera",
        f"  Maksimalna: {stats['size_distribution']['max']} karaktera",
        f"  Prosečna: {stats['size_distribution']['avg']:.0f} karaktera",
        "",
        "  Distribucija:",
        f"    < 200 karaktera: {stats['size_distribution']['under_200']}",
        f"    200-500 karaktera: {stats['size_distribution']['under_500']}",
        f"    500-1000 karaktera: {stats['size_distribution']['under_1000']}",
        f"    > 1000 karaktera: {stats['size_distribution']['over_1000']}",
        "",
        "POKRIVENOST NAPONSKIH NIVOA:",
        "-" * 30
    ])
    
    for voltage, count in sorted(stats['voltage_coverage'].items(), 
                                   key=lambda x: float(x[0].replace('kV', '').replace(',', '.')),
                                   reverse=True):
        lines.append(f"  {voltage}: {count} chunk-ova")
    
    if stats['by_object']:
        lines.extend([
            "",
            "TOP 10 OBJEKATA PO BROJU CHUNK-OVA:",
            "-" * 30
        ])
        
        sorted_objects = sorted(stats['by_object'].items(), key=lambda x: x[1], reverse=True)[:10]
        for obj, count in sorted_objects:
            lines.append(f"  {obj}: {count}")
    
    report = "\n".join(lines)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
    
    return report


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        # Default: učitaj sve chunk-ove
        filepath = Path(__file__).parent.parent / 'output' / 'all_chunks.jsonl'
    
    if Path(filepath).exists():
        chunks = load_chunks(str(filepath))
        stats = analyze_chunks(chunks)
        report = generate_report(stats)
        print(report)
        
        # Validacija
        print("\n" + "=" * 60)
        print("VALIDACIJA")
        print("=" * 60)
        
        error_count = 0
        for chunk in chunks:
            errors = validate_chunk(chunk)
            if errors:
                error_count += 1
                print(f"\nChunk {chunk.get('chunk_id', 'unknown')}:")
                for error in errors:
                    print(f"  - {error}")
        
        if error_count == 0:
            print("\nSvi chunk-ovi su validni!")
        else:
            print(f"\nUkupno chunk-ova sa greškama: {error_count}")
    else:
        print(f"Fajl ne postoji: {filepath}")
