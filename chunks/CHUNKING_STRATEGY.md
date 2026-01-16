# Konceptualno Rešenje za RAG Chunking EES Dokumentacije

## 1. Uvod

Ovaj dokument opisuje strategiju za semantičko deljenje dokumenata Elektroenergetskog sistema (EES) Srbije na chunk-ove pogodne za Retrieval Augmented Generation (RAG) sistem.

### 1.1 Cilj
Kreirati chunk-ove koji su:
- **Semantički koherentni** - svaki chunk ima samostalno značenje
- **Kontekstualno bogati** - sadrže potrebne metapodatke za precizno pretraživanje
- **Optimalne veličine** - dovoljno veliki za kontekst, dovoljno mali za preciznost

### 1.2 Tipovi dokumenata

| Prefiks | Tip | Opis |
|---------|-----|------|
| 1.xx | Rečnik pojmova | Definicije tehničkih termina |
| 2.xx | Tehnička uputstva | Opšta uputstva za eksploataciju |
| 3.xx | Pravila | Pravila za priključenje i rad sistema |
| 8.xx | Uputstva za pogon | Specifična uputstva po objektima |

---

## 2. Semantička Analiza Strukture Dokumenata

### 2.1 Rečnik Pojmova (1.xx)

**Struktura:**
```
### Broj. Naziv pojma

Definicija pojma...
```

**Semantička celina:** Jedan pojam = Jedan chunk

**Primer:**
```
### 26. Елемент ЕЕС

Далековод, кабл, мешовити вод, далеководно поље...
```

### 2.2 Uputstva za Pogon (8.xx)

Tipična struktura uputstva:

```
### 2. EKSPLOATACIONI USLOVI
    - 2.1 Opis funkcije objekta
    - 2.2 Povezanost sa mrežom
    - 2.3 Ograničenja u radu
    ...

### 3. REZULTATI ANALIZA SIGURNOSTI
    - 3.1 N-1 kritеrijum
    - 3.2 Struje kratkog spoja

### 4. PARALELAN RAD SA SUSEDNIM OBJEKTIMA
    ## 4.1 Objekat A
    ## 4.2 Objekat B
    ...

### 5. NORMALNO UKLOPNO STANJE
    ## 5.1 Postrojenje 400 kV
    ## 5.2 Postrojenje 220 kV
    ## 5.3 Postrojenje 110 kV

### 6+ POSEBNA UKLOPNA STANJA
    ## 6.1 Pogon bez DZS
    ## 7.1 Pogon bez TR
    ...
```

### 2.3 Pravila (3.xx)

Hijerarhijska struktura:
```
## Poglavlje
### Sekcija
#### Tačka
##### Podtačka
```

---

## 3. Definisani Tipovi Chunk-ova

### Tip A: Pojam iz Rečnika

| Atribut | Vrednost |
|---------|----------|
| Granularnost | Jedan pojam |
| Min veličina | 100 karaktera |
| Max veličina | 500 karaktera |
| Overlap | 0% |

**Obrazloženje:** Svaki pojam je samostalna definicija koja ne zavisi od susednih pojmova.

### Tip B: Eksploatacioni Uslov

| Atribut | Vrednost |
|---------|----------|
| Granularnost | Jedna numerisana tačka (npr. 2.1, 2.2) |
| Min veličina | 150 karaktera |
| Max veličina | 800 karaktera |
| Overlap | Header sekcije |

**Obrazloženje:** Svaka tačka opisuje jedan aspekt rada objekta. Uključiti header za kontekst.

**Primer sadržaja:**
- Opis funkcije TS/RP
- Povezanost sa susednim objektima
- Lista dalekovoda i transformatora
- Napajanje sopstvene potrošnje
- Ograničenja paralelnog rada

### Tip C: Normalno Uklopno Stanje

| Atribut | Vrednost |
|---------|----------|
| Granularnost | Jedan naponski nivo (400kV/220kV/110kV) |
| Min veličina | 200 karaktera |
| Max veličina | 1000 karaktera |
| Overlap | Naziv scenarija |

**Obrazloženje:** Uklopna stanja su logički grupisana po naponskim nivoima. Svaki nivo ima:
- Raspored elemenata po sistemima sabirnica
- Stanje spojnog polja
- Status diferencijalne zaštite

**Kritični elementi koje treba sačuvati:**
```
- ГС 1: ДВ xxx, ДВ yyy, ТР1
- ГС 2: ДВ zzz, ТР2
- СП укључено/искључено
- ДЗС активна/неактивна
```

### Tip D: Posebno Uklopno Stanje

| Atribut | Vrednost |
|---------|----------|
| Granularnost | Ceo scenario (npr. "bez DZS 400kV") |
| Min veličina | 300 karaktera |
| Max veličina | 1500 karaktera |
| Overlap | 10% |

**Tipični scenariji:**
- Pogon bez diferencijalne zaštite sabirnica (DZS)
- Pogon bez jednog transformatora
- Pogon u slučaju remonta
- Pogon u vanrednim situacijama

### Tip E: Paralelan Rad

| Atribut | Vrednost |
|---------|----------|
| Granularnost | Jedan susedni objekat |
| Min veličina | 100 karaktera |
| Max veličina | 500 karaktera |
| Overlap | 0% |

**Obrazloženje:** Reference na druge objekte su nezavisne celine.

### Tip F: Pravilo/Odredba

| Atribut | Vrednost |
|---------|----------|
| Granularnost | Tačka sa svim podtačkama |
| Min veličina | 200 karaktera |
| Max veličina | 2000 karaktera |
| Overlap | 10% |

**Obrazloženje:** Pravne/tehničke odredbe moraju biti kompletne.

### Tip G: Opšta Sekcija

Fallback za sekcije koje ne pripadaju drugim tipovima.

---

## 4. Struktura Metapodataka

```json
{
  "chunk_id": "string",         // Jedinstveni ID
  "content": "string",          // Tekst chunk-a
  
  "doc_id": "string",           // ID dokumenta
  "doc_type": "enum",           // recnik|uputstvo_pogon|pravila
  "doc_title": "string",        // Naslov dokumenta
  
  "object_code": "string|null", // Kod objekta (BB, NI2, itd.)
  "object_name": "string|null", // Puno ime objekta
  
  "voltage_levels": ["string"], // Naponski nivoi u chunk-u
  
  "section_number": "string",   // Broj sekcije (5.1, 2.3, itd.)
  "section_title": "string",    // Naslov sekcije
  "section_type": "enum",       // Tip sekcije
  
  "chunk_type": "A-G",          // Tip chunk-a
  
  "related_objects": ["string"],// Povezani objekti
  "keywords": ["string"],       // Ključne reči
  
  "year": "int|null",           // Godina dokumenta
  "char_count": "int"           // Broj karaktera
}
```

### 4.1 Važnost Metapodataka za RAG

| Metapodatak | Svrha |
|-------------|-------|
| `object_code` | Filtriranje po objektu |
| `voltage_levels` | Filtriranje po naponskom nivou |
| `section_type` | Razlikovanje normalnog od posebnog stanja |
| `related_objects` | Cross-referencing |
| `keywords` | Hibridno pretraživanje |

---

## 5. Primeri Chunk-ova

### 5.1 Primer Tipa C (Normalno Uklopno Stanje)

```json
{
  "chunk_id": "ni2_norm_5.1",
  "content": "## 5.1 Постројење 400 kV\n\n- ГС 1 (или ГС 2) систем сабирница: ДВ 403, ДВ 460, TР2 (или ТР4) и TР3;\n- ГС 2 (или ГС 1) систем сабирница: ДВ 404, ДВ 407, ДВ 423/2 и ТР4 (или ТР2);\n- спојно поље је укључено;\n- активна је диференцијална заштита сабирница.",
  "object_code": "NI2",
  "object_name": "TS Niš 2",
  "voltage_levels": ["400kV"],
  "section_type": "normalno_uklopno_stanje",
  "chunk_type": "C"
}
```

### 5.2 Primer Tipa D (Posebno Uklopno Stanje)

```json
{
  "chunk_id": "bb_bez_dzs_6.1",
  "content": "### 6. ПОГОН ТС БАЈИНА БАШТА У СЛУЧАЈУ НЕРАСПОЛОЖИВОСТИ ДИФЕРЕНЦИЈАЛНЕ ЗАШТИТЕ САБИРНИЦА\n\n## 6.1 Постројење 220 kV:\n\n- 1. (или 2.) систем сабирница: ДВ 210, ДВ 211, ДВ 209/1, ДВ 227/1, ДВ 206/1, ДВ 292Б, ДВ 203/3, ДВ 291, ДВ 292А, ДВ 204, ДВ 213/1 и ТР1;\n- спојно поље 220 kV искључено и растављено.",
  "object_code": "BB",
  "section_type": "posebno_uklopno_stanje",
  "chunk_type": "D",
  "keywords": ["ДЗС", "нерасположивост", "искључено"]
}
```

---

## 6. Strategija Pretraživanja

### 6.1 Tipični Upiti i Očekivani Rezultati

| Upit | Očekivani chunk tip |
|------|---------------------|
| "Šta je aktivna snaga?" | A (rečnik) |
| "Normalno uklopno stanje TS Niš 2 na 400kV" | C |
| "Kako radi TS BB kad nema DZS?" | D |
| "Sa kim je povezana TS Bajina Bašta?" | B ili E |
| "Pravila za napon u mreži 110kV" | F |

### 6.2 Filteri za Pretragu

Preporučeni filteri pri upitu:
- `object_code`: Kada je poznat objekat
- `voltage_levels`: Kada je naponski nivo relevantan
- `section_type`: Za razlikovanje normalnog/posebnog stanja
- `doc_type`: Za ograničavanje na tip dokumenta

---

## 7. Preporuke za Embedding Model

### 7.1 Zahtevi
- Podrška za ćirilicu (srpski jezik)
- Multilingual capability
- Kontekstualna senzitivnost na tehničke termine

### 7.2 Preporučeni Modeli

1. **BGE-M3** (BAAI)
   - Odlična podrška za više jezika
   - Dense + Sparse retrieval

2. **multilingual-e5-large** (Microsoft)
   - Optimizovan za multilingual

3. **sentence-transformers/paraphrase-multilingual-mpnet-base-v2**
   - Dobra alternativa

### 7.3 Query Prefix

Za bolje rezultate, koristiti prefix:
```
Query: "query: [tekst upita]"
Document: "passage: [sadržaj chunk-a]"
```

---

## 8. Zaključak

Ova strategija obezbeđuje:

1. **Semantičku celovitost** - Svaki chunk ima samostalno značenje
2. **Kontekstualno bogatstvo** - Metapodaci omogućavaju precizno filtriranje
3. **Fleksibilnost** - Različiti tipovi chunk-ova za različite potrebe
4. **Skalabilnost** - Lako proširivo na nove dokumente

### Sledeci Koraci

1. Pokrenuti `chunker.py` za generisanje chunk-ova
2. Analizirati rezultate sa `chunk_analyzer.py`
3. Fine-tuning veličina chunk-ova na osnovu rezultata
4. Implementirati embedding pipeline
5. Testirati retrieval kvalitet
