#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ekstraktor normalnih uklopnih stanja iz uputstava za pogon.

Prolazi kroz sve 8.xx fajlove i ekstrahuje sekciju 5 (NORMALNO UKLOPNO STANJE),
konvertuje u latinicu i ažurira object_registry.json.
"""

import json
import re
import os
from pathlib import Path
from typing import Optional, Dict, Tuple


# Mapiranje srpske ćirilice u latinicu
CYRILLIC_TO_LATIN = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ђ': 'Đ', 'Е': 'E',
    'Ж': 'Ž', 'З': 'Z', 'И': 'I', 'Ј': 'J', 'К': 'K', 'Л': 'L', 'Љ': 'Lj',
    'М': 'M', 'Н': 'N', 'Њ': 'Nj', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S',
    'Т': 'T', 'Ћ': 'Ć', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č',
    'Џ': 'Dž', 'Ш': 'Š',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'đ', 'е': 'e',
    'ж': 'ž', 'з': 'z', 'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'љ': 'lj',
    'м': 'm', 'н': 'n', 'њ': 'nj', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's',
    'т': 't', 'ћ': 'ć', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č',
    'џ': 'dž', 'ш': 'š',
}


def cyrillic_to_latin(text: str) -> str:
    """Konvertuje srpsku ćirilicu u latinicu."""
    if not text:
        return text
    result = []
    for char in text:
        result.append(CYRILLIC_TO_LATIN.get(char, char))
    return ''.join(result)


def extract_object_code(filename: str) -> Optional[str]:
    """
    Ekstrahuje kod objekta iz imena fajla.
    Npr: '8.05 UP-BG5_2023...' -> 'BG5'
    """
    # Pattern: UP-<KOD>_<GODINA>
    match = re.search(r'UP-([A-Z0-9]+)_', filename)
    if match:
        return match.group(1)
    
    # Specijalni slučajevi
    # KOŠ -> KOS (Košava)
    match = re.search(r'UP-KOŠ_', filename)
    if match:
        return 'KOS'
    
    # TENT B -> TENT-B-RP
    if 'TENT B' in filename or 'TENT-B' in filename:
        return 'TENT-B-RP'
    
    # TENT A SP -> TENT-A-SP
    if 'TENT A SP' in filename or 'TENT-A-SP' in filename:
        return 'TENT-A-SP'
    
    return None


def extract_section_5(content: str) -> Optional[str]:
    """
    Ekstrahuje sekciju 5 (NORMALNO UKLOPNO STANJE) iz sadržaja dokumenta.
    Vraća tekst od ### 5. do ### 6. (ili kraja dokumenta).
    """
    # Traži početak sekcije 5
    # Patterns za različite formate naslova sekcije 5
    # Napomena: neki dokumenti imaju grešku u kucanju (CTAЊE umesto СТАЊЕ)
    section_5_patterns = [
        r'###\s*5\.\s*НОРМАЛНО УКЛОПНО СТАЊЕ',
        r'###\s*5\.\s*НОРМАЛНО УКЛОПНО CTAЊE',  # greška u kucanju
        r'###\s*5\.\s*NORMALNO UKLOPNO STANJE',
        r'###\s*5\s+НОРМАЛНО УКЛОПНО СТАЊЕ',
        r'###\s*5\s+НОРМАЛНО УКЛОПНО CTAЊE',  # greška u kucanju
        r'###\s*5\s+NORMALNO UKLOPNO STANJE',
        r'###\s*5[.\s]+НОРМАЛНО\s+УКЛОПНО',  # opštiji pattern
    ]
    
    start_match = None
    for pattern in section_5_patterns:
        start_match = re.search(pattern, content, re.IGNORECASE)
        if start_match:
            break
    
    if not start_match:
        return None
    
    start_pos = start_match.start()
    
    # Traži kraj sekcije 5 (početak sekcije 6 ili kraj dokumenta)
    end_patterns = [
        r'###\s*6\.',
        r'###\s*6\s+',
    ]
    
    end_pos = len(content)
    for pattern in end_patterns:
        end_match = re.search(pattern, content[start_pos + 10:])
        if end_match:
            end_pos = start_pos + 10 + end_match.start()
            break
    
    section_text = content[start_pos:end_pos].strip()
    
    # Ukloni naslov sekcije, zadrži samo sadržaj
    # Traži prvi ## (podsekciju) ili prvu bullet tačku
    lines = section_text.split('\n')
    content_lines = []
    skip_header = True
    
    for line in lines:
        # Preskoči naslov ### 5. NORMALNO UKLOPNO STANJE
        if skip_header and line.strip().startswith('### 5'):
            skip_header = False
            continue
        content_lines.append(line)
    
    return '\n'.join(content_lines).strip()


def clean_section_text(text: str) -> str:
    """
    Čisti tekst sekcije - uklanja suvišne prazne linije,
    ali zadržava strukturu.
    """
    lines = text.split('\n')
    cleaned = []
    prev_empty = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if not prev_empty:
                cleaned.append('')
            prev_empty = True
        else:
            cleaned.append(line)
            prev_empty = False
    
    return '\n'.join(cleaned).strip()


def process_all_uputstva(files_dir: str) -> Dict[str, str]:
    """
    Prolazi kroz sve 8.xx fajlove i ekstrahuje normalno uklopno stanje.
    
    Returns:
        Dict mapiranje object_code -> normalno_uklopno_stanje (u latinici)
    """
    results = {}
    files_path = Path(files_dir)
    
    # Pronađi sve 8.xx fajlove (uputstva za pogon)
    uputstvo_files = sorted(files_path.glob('8.* UP-*.txt'))
    
    print(f"Pronađeno {len(uputstvo_files)} uputstava za pogon")
    print("-" * 60)
    
    for filepath in uputstvo_files:
        filename = filepath.name
        object_code = extract_object_code(filename)
        
        if not object_code:
            print(f"⚠ Ne mogu da ekstrahunjem kod objekta iz: {filename}")
            continue
        
        # Čitaj sadržaj fajla
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Ekstrahuj sekciju 5
        section_5 = extract_section_5(content)
        
        if not section_5:
            print(f"⚠ Sekcija 5 nije pronađena u: {filename}")
            continue
        
        # Očisti i konvertuj u latinicu
        section_5_clean = clean_section_text(section_5)
        section_5_latin = cyrillic_to_latin(section_5_clean)
        
        results[object_code] = section_5_latin
        
        # Kratak izveštaj
        line_count = len(section_5_latin.split('\n'))
        char_count = len(section_5_latin)
        print(f"✓ {object_code}: {line_count} linija, {char_count} karaktera")
    
    print("-" * 60)
    print(f"Ukupno ekstrahovanо: {len(results)} normalnih uklopnih stanja")
    
    return results


def update_object_registry(registry_path: str, uklopna_stanja: Dict[str, str]) -> Tuple[int, int]:
    """
    Ažurira object_registry.json sa normalnim uklopnim stanjima.
    
    Returns:
        Tuple (broj ažuriranih, broj novih)
    """
    with open(registry_path, 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    updated = 0
    not_found = []
    
    for obj in registry.get('objects', []):
        code = obj.get('code')
        if code in uklopna_stanja:
            obj['normalno_uklopno_stanje'] = uklopna_stanja[code]
            updated += 1
        else:
            # Probaj sa manjim varijacijama koda
            # npr. DJE1 vs DJE-1, BB vs BB
            for uk_code, uk_stanje in uklopna_stanja.items():
                if uk_code.replace('-', '') == code.replace('-', ''):
                    obj['normalno_uklopno_stanje'] = uk_stanje
                    updated += 1
                    break
    
    # Pronađi kodove koji nisu u registru
    registry_codes = {obj.get('code') for obj in registry.get('objects', [])}
    for code in uklopna_stanja:
        if code not in registry_codes:
            not_found.append(code)
    
    # Sačuvaj ažurirani registar
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)
    
    return updated, not_found


def main():
    # Putanje
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    files_dir = project_root / 'files'
    registry_path = script_dir.parent / 'metadata' / 'object_registry.json'
    
    print("=" * 60)
    print("EKSTRAKCIJA NORMALNIH UKLOPNIH STANJA")
    print("=" * 60)
    print()
    
    # Proveri da li postoje potrebni fajlovi
    if not files_dir.exists():
        print(f"GREŠKA: Direktorijum {files_dir} ne postoji!")
        return
    
    if not registry_path.exists():
        print(f"GREŠKA: Registar {registry_path} ne postoji!")
        return
    
    # Ekstrahuj uklopna stanja
    print("1. Ekstrakcija sekcija 5 iz uputstava...")
    print()
    uklopna_stanja = process_all_uputstva(files_dir)
    
    print()
    print("2. Ažuriranje object_registry.json...")
    updated, not_found = update_object_registry(registry_path, uklopna_stanja)
    
    print(f"   Ažurirano objekata: {updated}")
    if not_found:
        print(f"   Kodovi koji nisu u registru: {not_found}")
    
    print()
    print("=" * 60)
    print("ZAVRŠENO!")
    print("=" * 60)
    
    # Prikaži primer
    if uklopna_stanja:
        first_code = list(uklopna_stanja.keys())[0]
        print()
        print(f"Primer ({first_code}):")
        print("-" * 40)
        # Prikaži prvih 500 karaktera
        sample = uklopna_stanja[first_code][:500]
        print(sample)
        if len(uklopna_stanja[first_code]) > 500:
            print("...")


if __name__ == '__main__':
    main()
