#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluacija RAG sistema
======================

Pokreće evaluaciju na pitanjima iz evals.json i proverava
da li vraćeni chunkovi odgovaraju očekivanim chunk_refs.
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
    # Strip whitespace, lowercase, i ukloni trailing tačku
    return str(section).strip().lower().rstrip('.')


def check_chunk_match(retrieved_sections: List[str], expected_refs: Any, file_ids: List[str]) -> Tuple[bool, Dict]:
    """
    Proverava da li vraćeni chunkovi odgovaraju očekivanim.
    
    Args:
        retrieved_sections: Lista section_number iz vraćenih chunkova
        expected_refs: Očekivani chunk_refs (može biti lista ili lista listi)
        file_ids: Lista file_id-eva za pitanje
    
    Returns:
        (match, details) - da li ima poklapanja i detalji o poklapanju
    """
    # Normalizuj retrieved sections
    retrieved_set = set(normalize_section(s) for s in retrieved_sections)
    
    # Proveri strukturu expected_refs
    # Može biti:
    # 1. Lista stringova: ["5.1", "5.2"]
    # 2. Lista listi (za više dokumenata): [["2.1.63"], ["3.4.1", "3.4.2"]]
    
    if not expected_refs:
        return False, {"error": "no expected refs"}
    
    # Određi da li je lista listi
    is_nested = isinstance(expected_refs[0], list)
    
    if is_nested:
        # Za svaki file_id, proveri odgovarajući set expected_refs
        all_expected = set()
        for refs in expected_refs:
            for ref in refs:
                all_expected.add(normalize_section(ref))
    else:
        # Jednostavna lista
        all_expected = set(normalize_section(ref) for ref in expected_refs)
    
    # Pronađi poklapanja
    matches = retrieved_set & all_expected
    
    details = {
        "retrieved": list(retrieved_set),
        "expected": list(all_expected),
        "matches": list(matches),
        "num_matches": len(matches),
        "num_expected": len(all_expected),
        "num_retrieved": len(retrieved_set)
    }
    
    # Smatramo uspešnim ako ima bar jedno poklapanje
    success = len(matches) > 0
    
    return success, details


def run_evaluation(agent: RAGAgent, evals: List[Dict], top_k: int = 5, initial_k: int = 40, verbose: bool = True, quiet: bool = False,
                   output_path_txt: Path = None, output_path_failed: Path = None, min_score: float = 0.0) -> Dict:
    """
    Pokreće evaluaciju na svim pitanjima.
    
    Args:
        agent: RAG agent instanca
        evals: Lista evaluacionih pitanja
        top_k: Koliko top rezultata da vraća RAG
        verbose: Da li da štampa detalje za svako pitanje
        quiet: Da li da suzbije sve osim progress i rezultata
        output_path_txt: Putanja za snimanje rezultata (svakih 10)
        output_path_failed: Putanja za snimanje failed (svakih 10 failed)
        min_score: Minimalni score za uključivanje u retrieved rezultate (default: 0.0)
    
    Returns:
        Rezultati evaluacije
    """
    results = {
        "total": 0,
        "success": 0,
        "failed": 0,
        "details": [],
        "timestamp": datetime.now().isoformat(),
        "top_k": top_k,
        "match_positions": {},  # Statistika pozicija match-eva
        "low_rank_matches": []  # Pitanja gde je match na poziciji > 5
    }
    
    print(f"\n{Colors.HEADER}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}EVALUACIJA RAG SISTEMA{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*70}{Colors.ENDC}")
    print(f"Broj pitanja: {len(evals)}")
    print(f"Top K: {top_k}")
    print(f"Initial K (embedding): {initial_k}")
    if min_score > 0:
        print(f"Min Score: {min_score}")
    print(f"{Colors.HEADER}{'='*70}{Colors.ENDC}\n")
    
    if quiet:
        verbose = False
    
    last_save_total = 0
    last_save_failed = 0
    
    for i, eval_item in enumerate(evals):
        eval_id = eval_item.get('id', i)
        question = eval_item.get('text') or eval_item.get('question', '')
        file_ids = eval_item.get('file_id', [])
        expected_refs = eval_item.get('chunk_refs', [])
        
        if not question:
            continue
        
        results["total"] += 1
        
        # Retrieve chunks
        try:
            retrieved = agent.retrieve(question, initial_k=initial_k, final_k=top_k)
            
            # Izvuci section_number i object_code iz rezultata
            retrieved_sections = []
            retrieved_info = []
            for r in retrieved:
                section = r.get('section_number', '')
                object_code = r.get('object_code', '')
                file_num = r.get('file_num', '')
                score = r.get('rerank_score', r.get('faiss_score', 0))
                
                retrieved_sections.append(section)
                retrieved_info.append({
                    "section": section,
                    "object_code": object_code,
                    "file_num": file_num,
                    "score": score
                })
            
            # Filtriraj rezultate po file_id ako je potrebno
            filtered_sections = []
            filtered_info = []
            for r in retrieved_info:
                if r['file_num'] in file_ids:
                    filtered_sections.append(r['section'])
                    filtered_info.append(r)
            
            # Ako nema poklapanja po file_id, koristi sve retrieved sections
            sections_to_check = filtered_sections if filtered_sections else retrieved_sections
            
            # Check match
            success, match_details = check_chunk_match(sections_to_check, expected_refs, file_ids)
            
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
            
            # Kreiraj retrieved sa file_num:section:score formatom (normalizovano, bez trailing tačke)
            # Filtriraj po min_score ako je postavljeno
            if min_score > 0:
                retrieved_info = [r for r in retrieved_info if r['score'] >= min_score]
            retrieved_display = [f"{r['file_num']}:{r['section'].rstrip('.')}:{r['score']:.3f}" for r in retrieved_info]
            
            # Kreiraj matches sa file_num:section:score:position formatom i prati pozicije
            matches_display = []
            match_positions_for_question = []  # Sve pozicije match-eva za ovo pitanje
            first_match_pos = None
            for idx, r in enumerate(retrieved_info):
                section_norm = normalize_section(r['section'])
                for exp in expected_display:
                    exp_section = exp.split(':')[-1] if ':' in exp else exp
                    if normalize_section(exp_section) == section_norm and r['file_num'] in file_ids:
                        # Prati poziciju match-a (1-indexed)
                        pos = idx + 1
                        matches_display.append(f"{r['file_num']}:{r['section'].rstrip('.')}:{r['score']:.3f}:{pos}")
                        match_positions_for_question.append(pos)
                        results["match_positions"][pos] = results["match_positions"].get(pos, 0) + 1
                        if first_match_pos is None:
                            first_match_pos = pos
                        break
            
            # Proveri koji očekivani chunk-ovi NISU pronađeni uopšte
            # Strip score i position iz matches_display za poređenje (format je "file:section:score:pos")
            found_expected = set()
            for m in matches_display:
                # Ukloni poslednja 2 dela (score i position) za poređenje - ostaje "file:section"
                parts = m.rsplit(':', 2)
                if len(parts) == 3:  # format je file:section:score:pos
                    found_expected.add(parts[0])
                else:
                    found_expected.add(m)
            missing_expected = [e for e in expected_display if e not in found_expected]
            
            # Izračunaj worst (najgoru) poziciju - ili max poziciju ako postoji, ili "missing" ako neki chunk nije pronađen
            worst_pos = None
            if missing_expected:
                worst_pos = "missing"  # Neki očekivani chunk nije uopšte u top_k
            elif match_positions_for_question:
                worst_pos = max(match_positions_for_question)
            
            # Dodaj u low_rank_matches ako:
            # 1. Neki očekivani chunk nije pronađen uopšte, ILI
            # 2. Najgora pozicija match-a je > 5 (tj. 6+)
            if worst_pos == "missing" or (worst_pos is not None and worst_pos > 5):
                results["low_rank_matches"].append({
                    "id": eval_id,
                    "question": question,
                    "first_match_pos": first_match_pos,
                    "worst_match_pos": worst_pos,
                    "all_match_positions": match_positions_for_question,
                    "retrieved": retrieved_display,
                    "expected": expected_display,
                    "matches": matches_display,
                    "missing": missing_expected
                })
            
            # Ažuriraj match_details sa novim formatom
            match_details['retrieved'] = retrieved_display
            match_details['expected'] = expected_display
            match_details['matches'] = matches_display
            
            # Preračunaj success na osnovu matches_display (posle min_score filtriranja)
            success = len(matches_display) > 0
            
            if success:
                results["success"] += 1
                status = f"{Colors.GREEN}PASS{Colors.ENDC}"
            else:
                results["failed"] += 1
                status = f"{Colors.RED}FAIL{Colors.ENDC}"
            
            if verbose:
                print(f"\n{Colors.CYAN}[{results['total']:3}]{Colors.ENDC} {question[:90]}{'...' if len(question) > 90 else ''}")
                print(f"    Retrieved: {retrieved_display}")
                print(f"    Expected:  {expected_display}")
                print(f"    Matches:   {matches_display}")
                print(f"    {status}")
            elif quiet:
                pass_fail = "✓" if success else "✗"
                print(f"\r[{results['total']:3}/{len(evals)}] {pass_fail} P:{results['success']} F:{results['failed']}", end="", flush=True)
            
            # Sačuvaj detalje
            results["details"].append({
                "id": eval_id,
                "question": question,
                "file_id": file_ids,
                "expected_refs": expected_refs,
                "match_details": match_details,
                "success": success
            })
            
            # Snimaj svakih 10 pitanja
            if output_path_txt and (results["total"] - last_save_total) >= 10:
                results["success_rate"] = (results["success"] / results["total"] * 100) if results["total"] > 0 else 0
                save_results_txt(results, output_path_txt)
                last_save_total = results["total"]
                if not quiet:
                    print(f"    {Colors.YELLOW}[Saved at {results['total']}]{Colors.ENDC}")
            
            # Snimaj failed svakih 10 failed
            if output_path_failed and (results["failed"] - last_save_failed) >= 10:
                failed_results = {
                    'total': results['failed'],
                    'failed': results['failed'],
                    'success': 0,
                    'timestamp': results.get('timestamp', ''),
                    'top_k': results.get('top_k', 10),
                    'success_rate': 0,
                    'details': [d for d in results['details'] if not d['success']]
                }
                save_results_txt(failed_results, output_path_failed)
                last_save_failed = results["failed"]
            
        except Exception as e:
            results["failed"] += 1
            if verbose:
                print(f"    {Colors.RED}✗ ERROR: {e}{Colors.ENDC}")
            results["details"].append({
                "id": eval_id,
                "question": question,
                "error": str(e),
                "success": False
            })
    
    if quiet:
        print()  # Nova linija nakon progress bara
    
    # Summary
    success_rate = (results["success"] / results["total"] * 100) if results["total"] > 0 else 0
    
    print(f"\n{Colors.HEADER}{'='*70}{Colors.ENDC}")
    print(f"{Colors.BOLD}REZULTATI EVALUACIJE{Colors.ENDC}")
    print(f"{Colors.HEADER}{'='*70}{Colors.ENDC}")
    print(f"  Ukupno pitanja:  {results['total']}")
    print(f"  {Colors.GREEN}Uspešno:{Colors.ENDC}         {results['success']}")
    print(f"  {Colors.RED}Neuspešno:{Colors.ENDC}       {results['failed']}")
    print(f"  {Colors.BOLD}Uspešnost:{Colors.ENDC}       {success_rate:.1f}%")
    print(f"{Colors.HEADER}{'='*70}{Colors.ENDC}")
    
    # Statistika pozicija match-eva
    if results["match_positions"]:
        print(f"\n{Colors.BOLD}STATISTIKA POZICIJA MATCH-EVA:{Colors.ENDC}")
        print(f"{Colors.HEADER}{'-'*40}{Colors.ENDC}")
        total_matches = sum(results["match_positions"].values())
        for pos in sorted(results["match_positions"].keys()):
            count = results["match_positions"][pos]
            pct = (count / total_matches * 100) if total_matches > 0 else 0
            bar = '█' * int(pct / 5)  # Bar chart
            print(f"  Pozicija {pos:2}: {count:3} ({pct:5.1f}%) {bar}")
        print(f"{Colors.HEADER}{'-'*40}{Colors.ENDC}")
        print(f"  Ukupno match-eva: {total_matches}")
        
        # Statistika za pozicije 6-12 (van top 5)
        top5_matches = sum(results["match_positions"].get(p, 0) for p in range(1, 6))
        pos6_12_matches = sum(results["match_positions"].get(p, 0) for p in range(6, 13))
        top5_pct = (top5_matches / total_matches * 100) if total_matches > 0 else 0
        pos6_12_pct = (pos6_12_matches / total_matches * 100) if total_matches > 0 else 0
        print(f"{Colors.HEADER}{'-'*40}{Colors.ENDC}")
        print(f"  {Colors.GREEN}Top 1-5:{Colors.ENDC}  {top5_matches:3} ({top5_pct:5.1f}%)")
        print(f"  {Colors.YELLOW}Poz 6-12:{Colors.ENDC} {pos6_12_matches:3} ({pos6_12_pct:5.1f}%)")
        
        # Računanje dodatnih metrika (Recall@K, MRR, Hit@K)
        # Grupišemo match-eve po pitanjima da dobijemo prvi match za svako pitanje
        question_first_positions = {}  # id -> prva pozicija match-a
        for detail in results["details"]:
            if detail.get("success"):
                # Pronađi prvi match za ovo pitanje
                match_details = detail.get("match_details", {})
                matches = match_details.get("matches", [])
                if matches:
                    # Izvuci poziciju iz prvog match-a (format: "file:section:score:pos")
                    first_match = matches[0]
                    if ":" in first_match:
                        pos = int(first_match.split(":")[-1])
                        question_first_positions[detail["id"]] = pos
        
        num_questions = results["total"]
        
        # Recall@50: koliko pitanja ima bar jedan match u top 50
        recall_50 = sum(1 for pos in question_first_positions.values() if pos <= 50)
        recall_50_pct = (recall_50 / num_questions * 100) if num_questions > 0 else 0
        
        # Recall@100: koliko pitanja ima bar jedan match u top 100
        recall_100 = sum(1 for pos in question_first_positions.values() if pos <= 100)
        recall_100_pct = (recall_100 / num_questions * 100) if num_questions > 0 else 0
        
        # MRR@10: Mean Reciprocal Rank za top 10
        reciprocal_ranks = [1.0 / pos for pos in question_first_positions.values() if pos <= 10]
        mrr_10 = (sum(reciprocal_ranks) / num_questions) if num_questions > 0 else 0
        
        # Hit@1: koliko pitanja ima match na poziciji 1
        hit_1 = sum(1 for pos in question_first_positions.values() if pos == 1)
        hit_1_pct = (hit_1 / num_questions * 100) if num_questions > 0 else 0
        
        # Hit@3: koliko pitanja ima match u top 3
        hit_3 = sum(1 for pos in question_first_positions.values() if pos <= 3)
        hit_3_pct = (hit_3 / num_questions * 100) if num_questions > 0 else 0
        
        # Računanje prosečne veličine tokena po chunk-u
        # Aproksimacija: 1 token ≈ 4 karaktera (standardna aproksimacija za LLM modele)
        total_chars = 0
        total_chunks = len(agent.chunks) if hasattr(agent, 'chunks') else 0
        for chunk in agent.chunks if hasattr(agent, 'chunks') else []:
            content = chunk.get('content', '')
            total_chars += len(content)
        avg_chars_per_chunk = total_chars / total_chunks if total_chunks > 0 else 0
        avg_tokens_per_chunk = avg_chars_per_chunk / 4  # Aproksimacija: 4 chars ≈ 1 token
        
        # Ispis dodatnih metrika
        print(f"\n{Colors.BOLD}DODATNE METRIKE:{Colors.ENDC}")
        print(f"{Colors.HEADER}{'-'*40}{Colors.ENDC}")
        print(f"  Recall@50:  {recall_50:3}/{num_questions} ({recall_50_pct:5.1f}%)")
        print(f"  Recall@100: {recall_100:3}/{num_questions} ({recall_100_pct:5.1f}%)")
        print(f"  MRR@10:     {mrr_10:.4f}")
        print(f"  Hit@1:      {hit_1:3}/{num_questions} ({hit_1_pct:5.1f}%)")
        print(f"  Hit@3:      {hit_3:3}/{num_questions} ({hit_3_pct:5.1f}%)")
        print(f"{Colors.HEADER}{'-'*40}{Colors.ENDC}")
        print(f"  Ukupno chunkova:      {total_chunks:,}")
        print(f"  Prosečno karaktera:   {avg_chars_per_chunk:.0f}")
        print(f"  Prosečno tokena:      {avg_tokens_per_chunk:.0f} (≈4 chars/token)")
    print()
    
    results["success_rate"] = success_rate
    
    return results


def save_results_txt(results: Dict, output_path: Path):
    """Sačuvaj rezultate u čitljivom TXT formatu."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("EVALUACIJA RAG SISTEMA - REZULTATI\n")
        f.write("="*70 + "\n\n")
        f.write(f"Ažurirano: {timestamp}\n")
        f.write(f"Top K: {results.get('top_k', 10)}\n\n")
        
        total = results['total']
        success = results['success']
        failed = results['failed']
        rate = results.get('success_rate', 0)
        
        f.write(f"UKUPNO: {total}  |  PASS: {success}  |  FAIL: {failed}  |  {rate:.1f}%\n")
        f.write("="*70 + "\n\n")
        
        # Prvo failed
        failed_items = [d for d in results['details'] if not d['success']]
        if failed_items:
            f.write(f"FAILED ({len(failed_items)}):\n")
            f.write("-"*70 + "\n\n")
            for d in failed_items:
                f.write(f"[{d['id']:3}] {d['question']}\n")
                md = d.get('match_details', {})
                f.write(f"  Retrieved: {md.get('retrieved', [])}\n")
                f.write(f"  Expected:  {md.get('expected', [])}\n")
                f.write(f"  Matches:   {md.get('matches', [])}\n")
                f.write(f"  FAIL\n\n")
        
        # Pa passed
        passed_items = [d for d in results['details'] if d['success']]
        if passed_items:
            f.write(f"\nPASSED ({len(passed_items)}):\n")
            f.write("-"*70 + "\n\n")
            for d in passed_items:
                f.write(f"[{d['id']:3}] {d['question']}\n")
                md = d.get('match_details', {})
                f.write(f"  Retrieved: {md.get('retrieved', [])}\n")
                f.write(f"  Expected:  {md.get('expected', [])}\n")
                f.write(f"  Matches:   {md.get('matches', [])}\n")
                f.write(f"  PASS\n\n")


def save_low_rank_txt(low_rank_matches: list, output_path: Path, top_k: int):
    """Sačuvaj pitanja gde očekivani chunk-ovi nisu u top 5 ili nedostaju."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("PITANJA GDE OČEKIVANI CHUNK NIJE U TOP 5 ILI NEDOSTAJE\n")
        f.write("="*70 + "\n\n")
        f.write(f"Ažurirano: {timestamp}\n")
        f.write(f"Top K: {top_k}\n")
        f.write(f"Ukupno pitanja za optimizaciju: {len(low_rank_matches)}\n")
        f.write("="*70 + "\n\n")
        
        if not low_rank_matches:
            f.write("Sva pitanja imaju očekivane chunk-ove u top 5. Odlično!\n")
            return
        
        # Razdvoji na missing i low rank
        missing_items = [x for x in low_rank_matches if x.get('worst_match_pos') == 'missing']
        low_rank_items = [x for x in low_rank_matches if x.get('worst_match_pos') != 'missing']
        
        # Sortiraj low_rank po worst poziciji (najviša prva)
        low_rank_items = sorted(low_rank_items, key=lambda x: x.get('worst_match_pos', 0), reverse=True)
        
        # Prvo prikaži MISSING (najgori slučajevi)
        if missing_items:
            f.write(f"{'='*70}\n")
            f.write(f"NEDOSTAJU OČEKIVANI CHUNK-OVI ({len(missing_items)} pitanja)\n")
            f.write(f"{'='*70}\n\n")
            for item in missing_items:
                f.write(f"[{item['id']:3}] {item['question']}\n")
                f.write(f"  Retrieved: {item['retrieved']}\n")
                f.write(f"  Expected:  {item['expected']}\n")
                f.write(f"  Matches:   {item['matches']}\n")
                f.write(f"  MISSING:   {item.get('missing', [])}\n\n")
        
        # Pa LOW RANK (match postoji ali je na poziciji > 5)
        if low_rank_items:
            f.write(f"{'='*70}\n")
            f.write(f"MATCH NA POZICIJI > 5 ({len(low_rank_items)} pitanja)\n")
            f.write(f"{'='*70}\n\n")
            for item in low_rank_items:
                worst = item.get('worst_match_pos', '?')
                all_pos = item.get('all_match_positions', [])
                f.write(f"[{item['id']:3}] (worst={worst}, all={all_pos}) {item['question']}\n")
                f.write(f"  Retrieved: {item['retrieved']}\n")
                f.write(f"  Expected:  {item['expected']}\n")
                f.write(f"  Matches:   {item['matches']}\n\n")


def main():
    """Glavna funkcija za pokretanje evaluacije."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Evaluacija RAG sistema')
    parser.add_argument('--eval-file', '-e', type=str, default=None,
                       help='Custom eval JSON fajl (default: eval/evals.json)')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Tihi mod - samo rezultati')
    parser.add_argument('--min-score', '-m', type=float, default=0.0,
                       help='Minimalni score za uključivanje u retrieved (default: 0.0, npr. 0.9)')
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
    
    output_path_txt = base_dir / 'eval' / 'eval_results.txt'
    output_path_failed = base_dir / 'eval' / 'eval_results_failed.txt'
    
    # Proveri da li postoje fajlovi
    if not evals_path.exists():
        print(f"{Colors.RED}Greška: eval fajl ne postoji: {evals_path}{Colors.ENDC}")
        sys.exit(1)
    
    # Učitaj evaluaciona pitanja
    print(f"{Colors.CYAN}Učitavanje evaluacionih pitanja: {evals_path}{Colors.ENDC}")
    evals = load_evals(str(evals_path))
    print(f"{Colors.GREEN}✓ Učitano {len(evals)} pitanja{Colors.ENDC}")
    
    # Inicijalizuj RAG agenta
    try:
        agent = RAGAgent(str(config_path))
    except Exception as e:
        print(f"{Colors.RED}Greška pri inicijalizaciji RAG agenta: {e}{Colors.ENDC}")
        sys.exit(1)
    
    # Pokreni evaluaciju
    # top_k i initial_k se čitaju iz config-a
    quiet_mode = args.quiet
    top_k = agent.config.get('retrieval', {}).get('top_k', 12)
    initial_k = agent.config.get('retrieval', {}).get('embedding_top_k', 40)
    min_score = args.min_score
    results = run_evaluation(agent, evals, top_k=top_k, initial_k=initial_k, verbose=not quiet_mode, quiet=quiet_mode,
                            output_path_txt=output_path_txt, output_path_failed=output_path_failed, min_score=min_score)
    
    # Sačuvaj rezultate u TXT
    print(f"{Colors.CYAN}Čuvanje rezultata: {output_path_txt}{Colors.ENDC}")
    save_results_txt(results, output_path_txt)
    print(f"{Colors.GREEN}✓ Rezultati sačuvani{Colors.ENDC}")
    
    # Sačuvaj samo failed u poseban fajl
    failed_results = {
        'total': results['failed'],
        'failed': results['failed'],
        'success': 0,
        'timestamp': results.get('timestamp', ''),
        'top_k': results.get('top_k', 10),
        'success_rate': 0,
        'details': [d for d in results['details'] if not d['success']]
    }
    print(f"{Colors.CYAN}Čuvanje failed: {output_path_failed}{Colors.ENDC}")
    save_results_txt(failed_results, output_path_failed)
    print(f"{Colors.GREEN}✓ Failed sačuvani ({failed_results['failed']} pitanja){Colors.ENDC}")
    
    # Sačuvaj pitanja sa low rank match-evima (pozicija > 5)
    output_path_low_rank = base_dir / 'eval' / 'eval_results_low_rank.txt'
    low_rank_matches = results.get('low_rank_matches', [])
    print(f"{Colors.CYAN}Čuvanje low rank: {output_path_low_rank}{Colors.ENDC}")
    save_low_rank_txt(low_rank_matches, output_path_low_rank, results.get('top_k', 12))
    print(f"{Colors.GREEN}✓ Low rank sačuvani ({len(low_rank_matches)} pitanja za optimizaciju){Colors.ENDC}")


if __name__ == '__main__':
    main()
