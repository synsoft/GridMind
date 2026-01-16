# RAG Chunking Strategija za EES Dokumentaciju

## Pregled Dokumentacije

Dokumentacija obuhvata:
1. **Rečnik pojmova** (1.00) - Definicije tehničkih termina EES-a
2. **Tehnička uputstva** (2.xx) - Uputstva za eksploataciju sistema
3. **Pravila** (3.xx) - Pravila za priključenje i rad prenosnog sistema
4. **Uputstva za pogon** (8.xx) - Specifična uputstva za trafostanice i razvodna postrojenja

## Analiza Strukture Dokumenata

### 1. Rečnik pojmova (RP)
- Jasno strukturirani pojmovi sa numeracijom (1-150+)
- Svaki pojam ima naziv i definiciju
- Semantička celina = **jedan pojam sa kompletnom definicijom**

### 2. Uputstva za pogon (UP-xxx)
Tipična struktura:
- Poglavlje 2: EKSPLOATACIONI USLOVI
- Poglavlje 3: REZULTATI ANALIZE SIGURNOSTI I STRUJA KRATKOG SPOJA
- Poglavlje 4: PARALELAN RAD SA SUSEDNIM EE OBJEKTIMA
- Poglavlje 5: NORMALNO UKLOPNO STANJE
- Poglavlje 6+: POGON U POSEBNIM USLOVIMA (bez DZS, bez TR, itd.)

### 3. Pravila za priključenje/rad
- Hijerarhijska struktura poglavlja
- Numerisane tačke i podtačke
- Tabele sa tehničkim parametrima

---

## Strategija Chunkinga

### Princip 1: Semantička Celovitost
Svaki chunk mora biti **samostalna semantička celina** koja ima smisla bez konteksta.

### Princip 2: Metadata Enrichment
Svakom chunk-u se dodaju metapodaci:
- `doc_id`: Identifikator dokumenta
- `doc_type`: Tip dokumenta (recnik/uputstvo/pravila)
- `object_code`: Kod objekta (npr. BB, NI2, BG8)
- `object_name`: Puno ime objekta
- `voltage_levels`: Naponski nivoi (400kV, 220kV, 110kV, 35kV)
- `section`: Sekcija/poglavlje
- `section_type`: Tip sekcije (eksploatacioni_uslovi, normalno_uklopno_stanje, itd.)
- `related_objects`: Lista povezanih objekata

### Princip 3: Hijerarhijski Kontekst
Chunk uvek sadrži informacije o hijerarhiji iz koje potiče.

---

## Definicija Chunk Tipova

### Tip A: Pojam iz Rečnika
```
Granularnost: Jedan pojam
Struktura:
- Broj pojma
- Naziv pojma  
- Kompletna definicija
Veličina: 100-500 karaktera
```

### Tip B: Eksploatacioni Uslovi Objekta
```
Granularnost: Jedna tačka/stavka eksploatacionih uslova
Struktura:
- Broj tačke (npr. 2.1, 2.2)
- Tekst uslova
- Kontekst objekta (header)
Veličina: 200-800 karaktera
```

### Tip C: Normalno Uklopno Stanje
```
Granularnost: Cela sekcija za jedan naponski nivo
Struktura:
- Naponski nivo (400kV/220kV/110kV)
- Lista elemenata na svakom sistemu sabirnica
- Stanje spojnog polja
- Status diferencijalne zaštite
Veličina: 300-1000 karaktera
```

### Tip D: Posebno Uklopno Stanje
```
Granularnost: Kompletno stanje za jedan scenario
Struktura:
- Naziv scenarija (npr. "bez TR2", "bez DZS 110kV")
- Uklopna stanja po naponskim nivoima
- Posebna ograničenja
Veličina: 500-1500 karaktera
```

### Tip E: Parelani Rad sa Susedima
```
Granularnost: Jedan susedni objekat
Struktura:
- Naziv susednog objekta
- Reference na uputstvo
- Specifična uklopna stanja
Veličina: 100-500 karaktera
```

### Tip F: Pravilo/Odredba
```
Granularnost: Jedna tačka pravila sa podtačkama
Struktura:
- Broj tačke
- Tekst pravila
- Sve pripadajuće podtačke
Veličina: 200-1500 karaktera
```

### Tip G: Tehnički Parametar/Tabela
```
Granularnost: Kompletna tabela ili set parametara
Struktura:
- Naziv tabele/parametra
- Vrednosti
- Jedinice mere
Veličina: 200-2000 karaktera
```

---

## Chunk Template

```json
{
  "chunk_id": "UP-BB_5.1_uklopno_400kV",
  "content": "...",
  "metadata": {
    "doc_id": "UP-BB_2023",
    "doc_type": "uputstvo_pogon",
    "doc_title": "Uputstvo za pogon TS 220/35 kV Bajina Bašta",
    "object_code": "BB",
    "object_name": "TS Bajina Bašta",
    "voltage_levels": ["220kV", "35kV"],
    "section_number": "5.1",
    "section_title": "Postrojenje 220 kV",
    "section_type": "normalno_uklopno_stanje",
    "chunk_type": "C",
    "related_objects": ["SM2", "VA3", "OBR", "BG3", "PO", "BI"],
    "keywords": ["sistem sabirnica", "spojno polje", "DZS", "ДВ"],
    "year": 2023
  }
}
```

---

## Strategije za Specifične Dokumente

### Za Rečnik Pojmova (1.00)
- Svaki pojam = 1 chunk
- Metadata uključuje sinonime i povezane pojmove
- Cross-reference sa ostalim dokumentima

### Za Uputstva za Pogon (8.xx)
**Eksploatacioni uslovi:**
- Chunk po svakoj numerisanoj tački
- Sačuvati vezu sa objektom i naponskim nivoom

**Normalno uklopno stanje:**
- Chunk po naponskom nivou unutar postrojenja
- Uključiti kompletnu listu elemenata

**Posebna uklopna stanja:**
- Chunk po scenariju (bez DZS, bez TR, itd.)
- Uključiti sve relevantne naponske nivoe za taj scenario

**Paralelni rad:**
- Chunk po susednom objektu
- Uključiti reference na druga uputstva

### Za Pravila (3.xx)
- Chunk po tački sa svim podtačkama
- Sačuvati hijerarhiju poglavlja
- Tabele kao posebni chunk-ovi

---

## Overlap Strategija

```
Preporučen overlap: 10-15% prethodnog chunk-a
Način: Uključiti poslednju rečenicu/stavku prethodnog chunk-a
Svrha: Održati kontekstualni kontinuitet za retrieval
```

---

## Veličina Chunk-ova

| Tip dokumenta | Min karaktera | Max karaktera | Preporučeno |
|---------------|---------------|---------------|-------------|
| Rečnik        | 100           | 500           | 300         |
| Uklopna stanja| 300           | 1500          | 800         |
| Eksp. uslovi  | 150           | 800           | 400         |
| Pravila       | 200           | 2000          | 1000        |

---

## Embedding Preporuke

1. **Model**: `multilingual-e5-large` ili `BGE-M3` (podrška za ćirilicu)
2. **Prefix za query**: "Pronađi informacije o: "
3. **Prefix za dokument**: Tip dokumenta + kontekst objekta

---

## Folder Struktura

```
chunks/
├── README.md                    # Ovaj fajl
├── config/
│   └── chunking_config.json     # Konfiguracija za chunking
├── scripts/
│   └── chunker.py               # Python skripta za chunking
├── output/
│   ├── recnik/                  # Chunk-ovi iz rečnika
│   ├── uputstva/                # Chunk-ovi iz uputstava
│   └── pravila/                 # Chunk-ovi iz pravila
└── metadata/
    └── object_registry.json     # Registar EE objekata
```
