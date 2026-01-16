#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluacija RAG sistema - SVE VARIJANTE
======================================

Pokreće evaluaciju na svim varijantama pitanja iz evals.json:
- text (glavno pitanje)
- text_variants (sve varijante pitanja)

Za svako pitanje testira sve varijante i računa uspešnost po varijantama.
"""

import json
import os
import sys
import warnings
from pathlib import Path
from typing import List, Dict, Any, Set, Tuple
from datetime import datetime

# Suppress tokenizer warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore", message=".*XLMRobertaTokenizerFast.*")
warnings.filterwarnings("ignore", category=FutureWarning)

# Import RAG agent components
from rag_agent import RAGAgent, Colors


def load_evals(evals_path: str) -> List[Dict]:
    """Učitava evaluaciona pitanja iz JSON fajla."""
    with open(evals_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('data', [])


def normalize_section(section: str) -> str:
    """Normalizuje section number za poređenje."""
    if section is None:
        return ""
    return str(section).strip().lower().rstrip('.')


def check_chunk_match(retrieved_info: List[Dict], expected_refs: Any, file_ids: List[str]) -> Tuple[bool, Dict, int]:
    """
    Proverava da li vraćeni chunkovi odgovaraju očekivanim.
    
    Returns:
        (success, match_details, first_match_position)
    """
    # Kreiraj expected sa file_num:section formatom
    expected_display = []
    is_nested = expected_refs and isinstance(expected_refs[0], list)
    if is_nested:
        for idx, refs in enumerate(expected_refs):
            fid = file_ids[idx] if idx < len(file_ids) else file_ids[0]
            for ref in refs:
                expected_display.append(f"{fid}:{ref}")
    else:
        fid = file_ids[0] if file_ids else ''
        for ref in expected_refs:
            expected_display.append(f"{fid}:{ref}")
    
    # Kreiraj retrieved sa file_num:section formatom
    retrieved_display = [f"{r['file_num']}:{r['section'].rstrip('.')}" for r in retrieved_info]
    
    # Pronađi matches i pozicije
    matches_display = []
    first_match_pos = -1
    
    for idx, r in enumerate(retrieved_info):
        section_norm = normalize_section(r['section'])
        for exp in expected_display:
            exp_section = exp.split(':')[-1] if ':' in exp else exp
            if normalize_section(exp_section) == section_norm and r['file_num'] in file_ids:
                matches_display.append(f"{r['file_num']}:{r['section'].rstrip('.')}")
                if first_match_pos == -1:
                    first_match_pos = idx + 1  # 1-indexed
                break
    
    success = len(matches_display) > 0
    
    match_details = {
        'retrieved': retrieved_display,
        'expected': expected_display,
        'matches': matches_display
    }
    
    return success, match_details, first_match_pos


def run_evaluation_all_variants(agent: RAGAgent, evals: List[Dict], top_k: int = 12, 
                                 verbose: bool = True, quiet: bool = False) -> Dict:
    """
    Pokreće evaluaciju na svim pitanjima I svim varijantama.
    """
    results = {
        "total_questions": 0,
        "total_variants": 0,
        "questions_all_pass": 0,
        "questions_some_pass": 0,
        "questions_all_fail": 0,
        "variants_pass": 0,
        "variants_fail": 0,
        "details": [],
        "timestamp": datetime.now().isoformat(),
        "top_k": top_k,
        "match_positions": {}
    }
    
    print(f"\n{Colors.HEADER}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}EVALUACIJA RAG SISTEMA - SVE VARIJANTE{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*70}{Colors.ENDC}")
    print(f"Broj pitanja: {len(evals)}")
    print(f"Top K: {top_k}")
    print(f"{Colors.HEADER}{'='*70}{Colors.ENDC}\n")
    
    if quiet:
        verbose = False
    
    for i, eval_item in enumerate(evals):
        eval_id = eval_item.get('id', i)
        main_text = eval_item.get('text') or eval_item.get('question', '')
        text_variants = eval_item.get('text_variants', [])
        file_ids = eval_item.get('file_id', [])
        expected_refs = eval_item.get('chunk_refs', [])
        
        if not main_text:
            continue
        
        results["total_questions"] += 1
        
        # Kreiraj listu svih varijanti (main + variants)
        all_variants = [main_text] + text_variants
        
        question_results = {
            "id": eval_id,
            "main_text": main_text,
            "file_id": file_ids,
            "expected_refs": expected_refs,
            "variants": []
        }
        
        variants_passed = 0
        variants_failed = 0
        
        for var_idx, variant in enumerate(all_variants):
            results["total_variants"] += 1
            is_main = (var_idx == 0)
            
            try:
                retrieved = agent.retrieve(variant, final_k=top_k)
                
                # Izvuci info iz rezultata
                retrieved_info = []
                for r in retrieved:
                    retrieved_info.append({
                        "section": r.get('section_number', ''),
                        "object_code": r.get('object_code', ''),
                        "file_num": r.get('file_num', ''),
                        "score": r.get('rerank_score', r.get('faiss_score', 0))
                    })
                
                success, match_details, first_match_pos = check_chunk_match(
                    retrieved_info, expected_refs, file_ids
                )
                
                if success:
                    variants_passed += 1
                    results["variants_pass"] += 1
                    if first_match_pos > 0:
                        results["match_positions"][first_match_pos] = \
                            results["match_positions"].get(first_match_pos, 0) + 1
                else:
                    variants_failed += 1
                    results["variants_fail"] += 1
                
                variant_result = {
                    "variant_idx": var_idx,
                    "is_main": is_main,
                    "text": variant,
                    "success": success,
                    "first_match_pos": first_match_pos,
                    "match_details": match_details
                }
                question_results["variants"].append(variant_result)
                
                if verbose:
                    status = f"{Colors.GREEN}✓{Colors.ENDC}" if success else f"{Colors.RED}✗{Colors.ENDC}"
                    var_label = "MAIN" if is_main else f"VAR{var_idx}"
                    pos_info = f"@{first_match_pos}" if first_match_pos > 0 else ""
                    print(f"  [{eval_id:3}] {var_label:5} {status} {pos_info:3} {variant[:60]}{'...' if len(variant) > 60 else ''}")
                
            except Exception as e:
                variants_failed += 1
                results["variants_fail"] += 1
                question_results["variants"].append({
                    "variant_idx": var_idx,
                    "is_main": is_main,
                    "text": variant,
                    "success": False,
                    "error": str(e)
                })
                if verbose:
                    print(f"  [{eval_id:3}] VAR{var_idx:2} {Colors.RED}ERROR: {e}{Colors.ENDC}")
        
        # Odredi status pitanja
        if variants_passed == len(all_variants):
            results["questions_all_pass"] += 1
            question_results["status"] = "ALL_PASS"
        elif variants_passed > 0:
            results["questions_some_pass"] += 1
            question_results["status"] = "SOME_PASS"
        else:
            results["questions_all_fail"] += 1
            question_results["status"] = "ALL_FAIL"
        
        question_results["variants_passed"] = variants_passed
        question_results["variants_total"] = len(all_variants)
        
        results["details"].append(question_results)
        
        if quiet:
            pct = (results["variants_pass"] / results["total_variants"] * 100) if results["total_variants"] > 0 else 0
            print(f"\r[{results['total_questions']:3}/{len(evals)}] Variants: {results['variants_pass']}/{results['total_variants']} ({pct:.1f}%)", end="", flush=True)
    
    if quiet:
        print()
    
    # Summary
    print(f"\n{Colors.HEADER}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}REZULTATI EVALUACIJE - SVE VARIJANTE{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*70}{Colors.ENDC}")
    
    print(f"\n{Colors.BOLD}PO PITANJIMA:{Colors.ENDC}")
    print(f"  Ukupno pitanja:     {results['total_questions']}")
    print(f"  {Colors.GREEN}Sve varijante OK:{Colors.ENDC}   {results['questions_all_pass']}")
    print(f"  {Colors.YELLOW}Neke varijante OK:{Colors.ENDC}  {results['questions_some_pass']}")
    print(f"  {Colors.RED}Sve varijante FAIL:{Colors.ENDC} {results['questions_all_fail']}")
    
    print(f"\n{Colors.BOLD}PO VARIJANTAMA:{Colors.ENDC}")
    var_rate = (results["variants_pass"] / results["total_variants"] * 100) if results["total_variants"] > 0 else 0
    print(f"  Ukupno varijanti:   {results['total_variants']}")
    print(f"  {Colors.GREEN}Uspešno:{Colors.ENDC}            {results['variants_pass']}")
    print(f"  {Colors.RED}Neuspešno:{Colors.ENDC}          {results['variants_fail']}")
    print(f"  {Colors.BOLD}Uspešnost:{Colors.ENDC}          {var_rate:.1f}%")
    
    print(f"{Colors.HEADER}{'='*70}{Colors.ENDC}")
    
    # Statistika pozicija match-eva
    if results["match_positions"]:
        print(f"\n{Colors.BOLD}STATISTIKA POZICIJA MATCH-EVA:{Colors.ENDC}")
        print(f"{Colors.HEADER}{'-'*40}{Colors.ENDC}")
        total_matches = sum(results["match_positions"].values())
        for pos in sorted(results["match_positions"].keys()):
            count = results["match_positions"][pos]
            pct = (count / total_matches * 100) if total_matches > 0 else 0
            bar = '█' * int(pct / 5)
            print(f"  Pozicija {pos:2}: {count:3} ({pct:5.1f}%) {bar}")
        print(f"{Colors.HEADER}{'-'*40}{Colors.ENDC}")
        print(f"  Ukupno match-eva: {total_matches}")
    print()
    
    results["variants_success_rate"] = var_rate
    
    return results


def save_results_all_txt(results: Dict, output_path: Path):
    """Sačuvaj rezultate u čitljivom TXT formatu."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("EVALUACIJA RAG SISTEMA - SVE VARIJANTE\n")
        f.write("="*70 + "\n\n")
        f.write(f"Ažurirano: {timestamp}\n")
        f.write(f"Top K: {results.get('top_k', 12)}\n\n")
        
        f.write("PO PITANJIMA:\n")
        f.write(f"  Ukupno: {results['total_questions']}\n")
        f.write(f"  Sve OK: {results['questions_all_pass']}\n")
        f.write(f"  Neke OK: {results['questions_some_pass']}\n")
        f.write(f"  Sve FAIL: {results['questions_all_fail']}\n\n")
        
        f.write("PO VARIJANTAMA:\n")
        f.write(f"  Ukupno: {results['total_variants']}\n")
        f.write(f"  Pass: {results['variants_pass']}\n")
        f.write(f"  Fail: {results['variants_fail']}\n")
        f.write(f"  Uspešnost: {results.get('variants_success_rate', 0):.1f}%\n\n")
        
        f.write("="*70 + "\n\n")
        
        # Pitanja sa problemima (SOME_PASS ili ALL_FAIL)
        problem_items = [d for d in results['details'] if d['status'] != 'ALL_PASS']
        if problem_items:
            f.write(f"PITANJA SA PROBLEMIMA ({len(problem_items)}):\n")
            f.write("-"*70 + "\n\n")
            
            for q in problem_items:
                f.write(f"[{q['id']:3}] {q['status']} ({q['variants_passed']}/{q['variants_total']})\n")
                f.write(f"  Main: {q['main_text']}\n")
                f.write(f"  Expected: {q.get('expected_refs', [])}\n")
                
                # Prikaži failed varijante
                failed_vars = [v for v in q['variants'] if not v['success']]
                for v in failed_vars:
                    var_label = "MAIN" if v['is_main'] else f"VAR{v['variant_idx']}"
                    f.write(f"    {var_label} FAIL: {v['text']}\n")
                    md = v.get('match_details', {})
                    f.write(f"      Retrieved: {md.get('retrieved', [])}\n")
                f.write("\n")
        
        # Pitanja OK
        ok_items = [d for d in results['details'] if d['status'] == 'ALL_PASS']
        f.write(f"\nPITANJA SVE OK ({len(ok_items)}):\n")
        f.write("-"*70 + "\n")
        for q in ok_items:
            f.write(f"[{q['id']:3}] ({q['variants_total']} var) {q['main_text']}\n")


def save_failed_txt(results: Dict, output_path: Path):
    """Sačuvaj SVE failed varijante u TXT."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Prikupi SVE failed varijante
    failed_variants = []
    for q in results['details']:
        for v in q['variants']:
            if not v['success']:
                failed_variants.append({
                    'id': q['id'],
                    'main_text': q['main_text'],
                    'variant_text': v['text'],
                    'is_main': v['is_main'],
                    'variant_idx': v['variant_idx'],
                    'match_details': v.get('match_details', {})
                })
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("EVALUACIJA RAG SISTEMA - SVE FAILED VARIJANTE\n")
        f.write("="*70 + "\n\n")
        f.write(f"Ažurirano: {timestamp}\n")
        f.write(f"Top K: {results.get('top_k', 12)}\n")
        f.write(f"Ukupno failed varijanti: {len(failed_variants)}\n")
        f.write("="*70 + "\n\n")
        
        if not failed_variants:
            f.write("Nema failed varijanti.\n")
            return
        
        for item in failed_variants:
            var_label = "MAIN" if item['is_main'] else f"VAR{item['variant_idx']}"
            f.write(f"[{item['id']:3}] {var_label}: {item['variant_text']}\n")
            md = item['match_details']
            f.write(f"  Retrieved: {md.get('retrieved', [])}\n")
            f.write(f"  Expected:  {md.get('expected', [])}\n")
            f.write(f"  Matches:   {md.get('matches', [])}\n")
            f.write(f"  FAIL\n\n")


def save_low_rank_txt(results: Dict, output_path: Path):
    """Sačuvaj SVE varijante gde je match na poziciji > 5 (za optimizaciju)."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Pronađi SVE varijante sa match-om na poziciji > 5
    low_rank_matches = []
    for q in results['details']:
        for v in q['variants']:
            if v['success'] and v.get('first_match_pos', 0) > 5:
                low_rank_matches.append({
                    'id': q['id'],
                    'main_text': q['main_text'],
                    'variant_text': v['text'],
                    'is_main': v['is_main'],
                    'variant_idx': v['variant_idx'],
                    'first_match_pos': v['first_match_pos'],
                    'retrieved': v.get('match_details', {}).get('retrieved', []),
                    'expected': v.get('match_details', {}).get('expected', []),
                    'matches': v.get('match_details', {}).get('matches', [])
                })
    
    # Sortiraj po poziciji (najviša prva)
    low_rank_matches.sort(key=lambda x: x['first_match_pos'], reverse=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("VARIJANTE SA MATCH-EVIMA NA POZICIJI > 5 (ZA OPTIMIZACIJU)\n")
        f.write("="*70 + "\n\n")
        f.write(f"Ažurirano: {timestamp}\n")
        f.write(f"Top K: {results.get('top_k', 12)}\n")
        f.write(f"Ukupno varijanti za optimizaciju: {len(low_rank_matches)}\n")
        f.write("="*70 + "\n\n")
        
        if not low_rank_matches:
            f.write("Nema varijanti sa match-evima na poziciji > 5.\n")
            return
        
        for item in low_rank_matches:
            var_label = "MAIN" if item['is_main'] else f"VAR{item['variant_idx']}"
            f.write(f"[{item['id']:3}] (pos={item['first_match_pos']:2}) {var_label}: {item['variant_text']}\n")
            f.write(f"  Retrieved: {item['retrieved']}\n")
            f.write(f"  Expected:  {item['expected']}\n")
            f.write(f"  Matches:   {item['matches']}\n\n")


def main():
    """Glavna funkcija za pokretanje evaluacije."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Evaluacija RAG sistema - sve varijante')
    parser.add_argument('--eval-file', '-e', type=str, default=None,
                       help='Custom eval JSON fajl (default: eval/evals.json)')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Tihi mod - samo rezultati')
    parser.add_argument('--top-k', '-k', type=int, default=12,
                       help='Top K rezultata (default: 12)')
    args, _ = parser.parse_known_args()
    
    # Putanje
    base_dir = Path(__file__).parent.parent
    config_path = base_dir / 'config' / 'rag_config.json'
    
    if args.eval_file:
        evals_path = Path(args.eval_file)
        if not evals_path.is_absolute():
            evals_path = base_dir / 'eval' / args.eval_file
    else:
        evals_path = base_dir / 'eval' / 'evals.json'
    
    output_path_txt = base_dir / 'eval' / 'eval_results_all.txt'
    output_path_failed = base_dir / 'eval' / 'eval_results_failed.txt'
    output_path_low_rank = base_dir / 'eval' / 'eval_results_low_rank.txt'
    
    # Proveri da li postoje fajlovi
    if not evals_path.exists():
        print(f"{Colors.RED}Greška: eval fajl ne postoji: {evals_path}{Colors.ENDC}")
        sys.exit(1)
    
    # Učitaj evaluaciona pitanja
    print(f"{Colors.CYAN}Učitavanje evaluacionih pitanja: {evals_path}{Colors.ENDC}")
    evals = load_evals(str(evals_path))
    print(f"{Colors.GREEN}✓ Učitano {len(evals)} pitanja{Colors.ENDC}")
    
    # Prebroj varijante
    total_variants = sum(1 + len(e.get('text_variants', [])) for e in evals)
    print(f"{Colors.GREEN}✓ Ukupno varijanti: {total_variants}{Colors.ENDC}")
    
    # Inicijalizuj RAG agenta
    try:
        agent = RAGAgent(str(config_path))
    except Exception as e:
        print(f"{Colors.RED}Greška pri inicijalizaciji RAG agenta: {e}{Colors.ENDC}")
        sys.exit(1)
    
    # Pokreni evaluaciju
    quiet_mode = args.quiet
    results = run_evaluation_all_variants(agent, evals, top_k=args.top_k, 
                                           verbose=not quiet_mode, quiet=quiet_mode)
    
    # Sačuvaj rezultate u TXT
    print(f"{Colors.CYAN}Čuvanje rezultata: {output_path_txt}{Colors.ENDC}")
    save_results_all_txt(results, output_path_txt)
    print(f"{Colors.GREEN}✓ Rezultati sačuvani{Colors.ENDC}")
    
    # Sačuvaj failed u poseban fajl
    print(f"{Colors.CYAN}Čuvanje failed: {output_path_failed}{Colors.ENDC}")
    save_failed_txt(results, output_path_failed)
    failed_count = sum(1 for q in results['details'] for v in q['variants'] if not v['success'])
    print(f"{Colors.GREEN}✓ Failed sačuvani ({failed_count} varijanti){Colors.ENDC}")
    
    # Sačuvaj low rank u poseban fajl
    print(f"{Colors.CYAN}Čuvanje low rank: {output_path_low_rank}{Colors.ENDC}")
    save_low_rank_txt(results, output_path_low_rank)
    low_rank_count = sum(1 for q in results['details'] for v in q['variants'] if v['success'] and v.get('first_match_pos', 0) > 5)
    print(f"{Colors.GREEN}✓ Low rank sačuvani ({low_rank_count} varijanti za optimizaciju){Colors.ENDC}")


if __name__ == '__main__':
    main()
