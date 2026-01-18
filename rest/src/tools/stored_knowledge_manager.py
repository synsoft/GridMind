#!/usr/bin/env python3
"""
Stored Knowledge Manager CLI
Interaktivno upravljanje stored_knowledge.json bazom
"""

from src.core.stored_knowledge import StoredKnowledgeManager
import sys


def list_all_entries(skm):
    """Prikaži sve stavke"""
    entries = skm.list_all()
    if not entries:
        print("\n❌ Nema stavki u bazi.")
        return
    
    print(f"\n📋 Pronađeno {len(entries)} stavki:\n")
    for i, entry in enumerate(entries, 1):
        print(f"{i}. ID: {entry['id']}")
        if 'title' in entry and entry['title']:
            print(f"   Title: {entry['title']}")
        content_preview = entry['content'][:150].replace('\n', ' ')
        print(f"   Content: {content_preview}...")
        print(f"   Timestamp: {entry.get('timestamp', 'N/A')}")
        print("-" * 60)


def delete_by_id(skm):
    """Obriši stavku po ID-u"""
    entry_id = input("\nUnesite ID stavke za brisanje: ").strip()
    
    if not entry_id:
        print("❌ ID ne može biti prazan.")
        return
    
    # Prvo prikaži stavku
    entries = [e for e in skm.list_all() if e['id'] == entry_id]
    if not entries:
        print(f"❌ Stavka sa ID '{entry_id}' nije pronađena.")
        return
    
    entry = entries[0]
    print("\n📄 Stavka za brisanje:")
    if 'title' in entry and entry['title']:
        print(f"Title: {entry['title']}")
    print(f"Content: {entry['content'][:200]}...")
    
    confirm = input("\n⚠️  Da li ste sigurni? (da/ne): ").strip().lower()
    if confirm in ['da', 'yes', 'y']:
        if skm.delete_entry(entry_id):
            print(f"✅ Stavka '{entry_id}' uspešno obrisana!")
        else:
            print(f"❌ Greška pri brisanju stavke.")
    else:
        print("❌ Brisanje otkazano.")


def delete_all(skm):
    """Obriši sve stavke"""
    count = skm.count()
    if count == 0:
        print("\n❌ Nema stavki za brisanje.")
        return
    
    print(f"\n⚠️  UPOZORENJE: Brisanje svih {count} stavki!")
    confirm = input("Unesite 'OBRIŠI SVE' za potvrdu: ").strip()
    
    if confirm == "OBRIŠI SVE":
        skm.knowledge_base = []
        skm.embeddings = []
        skm._save()
        print("✅ Sve stavke su uspešno obrisane!")
    else:
        print("❌ Brisanje otkazano.")


def search_entries(skm):
    """Pretraži stavke"""
    query = input("\nUnesite upit za pretragu: ").strip()
    
    if not query:
        print("❌ Upit ne može biti prazan.")
        return
    
    top_k = input("Broj rezultata (default 5): ").strip()
    top_k = int(top_k) if top_k.isdigit() else 5
    
    results = skm.search(query, top_k=top_k)
    
    if not results:
        print("\n❌ Nema rezultata.")
        return
    
    print(f"\n🔍 Pronađeno {len(results)} rezultata:\n")
    for i, (entry, score) in enumerate(results, 1):
        print(f"{i}. Score: {score:.4f} | ID: {entry['id']}")
        if 'title' in entry and entry['title']:
            print(f"   Title: {entry['title']}")
        content_preview = entry['content'][:150].replace('\n', ' ')
        print(f"   Content: {content_preview}...")
        print("-" * 60)


def add_entry(skm):
    """Dodaj novu stavku"""
    print("\n➕ Dodavanje nove stavke")
    
    entry_id = input("ID (ostavi prazno za automatski): ").strip()
    title = input("Title (opciono): ").strip()
    
    print("Content (unesi tekst, završi sa praznim redom):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    content = '\n'.join(lines)
    
    if not content:
        print("❌ Content ne može biti prazan.")
        return
    
    metadata = {}
    if title:
        metadata['title'] = title
    
    added_id = skm.add_entry(content, entry_id=entry_id if entry_id else None, metadata=metadata)
    print(f"✅ Stavka uspešno dodata sa ID: {added_id}")


def main():
    skm = StoredKnowledgeManager(storage_file="data/stored_knowledge_data/stored_knowledge.json")
    
    while True:
        print("\n" + "="*60)
        print("📚 STORED KNOWLEDGE MANAGER")
        print("="*60)
        print(f"Ukupno stavki: {skm.count()}")
        print("\nOpcije:")
        print("1. Prikaži sve stavke")
        print("2. Obriši stavku po ID-u")
        print("3. Obriši sve stavke")
        print("4. Pretraga")
        print("5. Dodaj novu stavku")
        print("0. Izlaz")
        print("-"*60)
        
        choice = input("Izaberite opciju: ").strip()
        
        if choice == "1":
            list_all_entries(skm)
        elif choice == "2":
            delete_by_id(skm)
        elif choice == "3":
            delete_all(skm)
        elif choice == "4":
            search_entries(skm)
        elif choice == "5":
            add_entry(skm)
        elif choice == "0":
            print("👋 Kraj!")
            sys.exit(0)
        else:
            print("❌ Nepoznata opcija. Pokušajte ponovo.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Prekinuto od strane korisnika.")
        sys.exit(0)
