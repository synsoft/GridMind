#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RAG Chunker za EES dokumentaciju - V3
=====================================

Verzija 3 - Poboljšano chunking za uputstva za pogon:
- Deli po ## (dve tarabe) za podsekcije (npr. 5.1, 5.2...)
- Svaka podsekcija = jedan chunk
- Svaki chunk obavezno sadrži naslov(e) roditelja (### ...)
- Čuva metadata o dokumentu i sekciji
"""

import json
import re
import os
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Optional, Tuple
from datetime import datetime
import hashlib


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


@dataclass
class Chunk:
    """Predstavlja jedan semantički chunk."""
    file_num: str  # Broj fajla (npr. "8.20") - PRVI atribut
    chunk_id: str
    doc_title: str
    content: str
    doc_id: str
    doc_type: str
    object_code: Optional[str]
    object_name: Optional[str]
    voltage_levels: List[str]
    section_number: str
    section_title: str
    section_type: str
    chunk_type: str
    related_objects: List[str]
    keywords: List[str]
    year: Optional[int]
    char_count: int
    hierarchy: List[Dict[str, str]] = field(default_factory=list)
    parent_section: Optional[str] = None
    parent_title: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Konvertuje u dict sa file_num na prvom mestu."""
        d = asdict(self)
        # Osiguraj da file_num bude prvi
        ordered = {'file_num': d.pop('file_num')}
        ordered.update(d)
        return ordered
    
    def to_latin(self) -> 'Chunk':
        """Konvertuje sva tekstualna polja u latinicu."""
        return Chunk(
            file_num=self.file_num,
            chunk_id=self.chunk_id,
            doc_title=self.doc_title,
            content=cyrillic_to_latin(self.content),
            doc_id=self.doc_id,
            doc_type=self.doc_type,
            object_code=self.object_code,
            object_name=cyrillic_to_latin(self.object_name) if self.object_name else None,
            voltage_levels=self.voltage_levels,
            section_number=self.section_number,
            section_title=cyrillic_to_latin(self.section_title),
            section_type=self.section_type,
            chunk_type=self.chunk_type,
            related_objects=self.related_objects,
            keywords=[cyrillic_to_latin(k) for k in self.keywords],
            year=self.year,
            char_count=self.char_count,
            hierarchy=[{'number': h['number'], 'title': cyrillic_to_latin(h['title'])} for h in self.hierarchy],
            parent_section=self.parent_section,
            parent_title=cyrillic_to_latin(self.parent_title) if self.parent_title else None,
        )


class EESChunkerV3:
    """Chunker V3 - deli po ### za uputstva za pogon."""
    
    MIN_CHUNK_SIZE = 50
    MAX_CHUNK_SIZE = 8000  # Maksimalna veličina chunk-a
    
    def __init__(self, config_path: str, registry_path: str = None):
        """Inicijalizacija."""
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        # Opcioni registry fajl
        self.object_codes = {}
        self.abbreviations = {}
        
        if registry_path and os.path.exists(registry_path):
            with open(registry_path, 'r', encoding='utf-8') as f:
                registry = json.load(f)
                if 'objects' in registry:
                    self.object_codes = {obj['code']: obj for obj in registry['objects']}
                self.abbreviations = registry.get('element_abbreviations', {})
        
        self.patterns = {
            'main_section': re.compile(r'^###\s*(\d+)\.\s*(.+)$', re.MULTILINE),
            'subsection': re.compile(r'^##\s*(\d+\.\d+\.?\d*)\s*(.+)$', re.MULTILINE),
            'voltage': re.compile(r'(\d+(?:,\d+)?)\s*kV', re.IGNORECASE),
            'object_code': re.compile(r'UP-([A-Z0-9]+)_'),
            'term_definition': re.compile(r'^###\s*(\d+)\.\s*(.+?)\n\n(.+?)(?=\n###|\Z)', re.MULTILINE | re.DOTALL),
        }
    
    def detect_document_type(self, filename: str) -> str:
        """Detektuje tip dokumenta."""
        if filename.startswith('1.'):
            return 'recnik'
        elif filename.startswith('2.'):
            return 'tehnicko_uputstvo'
        elif filename.startswith('3.'):
            return 'pravila'
        elif filename.startswith('8.'):
            return 'uputstvo_pogon'
        return 'unknown'
    
    def extract_file_num(self, filename: str) -> str:
        """Izvlači broj fajla (npr. '8.20' iz '8.20 UP-NI2_2022 ...')."""
        match = re.match(r'^(\d+\.\d+)', filename)
        if match:
            return match.group(1)
        return ''
    
    def extract_object_code(self, filename: str) -> Optional[str]:
        """Izvlači kod objekta."""
        match = self.patterns['object_code'].search(filename)
        if match:
            return match.group(1)
        return None
    
    def extract_object_name(self, filename: str) -> Optional[str]:
        """Izvlači puno ime objekta iz naziva fajla (bez naponskih nivoa).
        
        Npr: '8.20 UP-NI2_2022 Uputstvo za pogon TS 400_220_110 kV Niš 2.txt'
             -> 'TS Niš 2'
        """
        # Traži pattern: "Uputstvo za pogon <IME OBJEKTA>.txt"
        match = re.search(r'Uputstvo za pogon\s+(.+?)\.txt$', filename, re.IGNORECASE)
        if match:
            name = match.group(1).strip()
            # Ukloni naponske nivoe (npr. "400_220_110 kV", "110 kV", "400/220 kV")
            name = re.sub(r'[\d_/,]+\s*kV\s*', '', name, flags=re.IGNORECASE)
            # Ukloni višestruke razmake
            name = re.sub(r'\s+', ' ', name).strip()
            return name
        return None
    
    def extract_voltage_levels_from_filename(self, filename: str) -> List[str]:
        """Izvlači naponske nivoe iz naziva fajla.
        
        Npr: '8.20 UP-NI2_2022 Uputstvo za pogon TS 400_220_110 kV Niš 2.txt'
             -> ['400kV', '220kV', '110kV']
        """
        voltages = []
        # Traži pattern: brojevi razdvojeni _ ili / ispred 'kV'
        # npr. "400_220_110 kV" ili "220/35 kV"
        match = re.search(r'([\d_/,]+)\s*kV', filename, re.IGNORECASE)
        if match:
            voltage_str = match.group(1)
            # Razdvoji po _ ili /
            parts = re.split(r'[_/]', voltage_str)
            for p in parts:
                p = p.strip().replace(',', '.')
                if p:
                    voltages.append(f"{p}kV")
        # Sortiraj po veličini (descending)
        try:
            voltages = sorted(voltages, key=lambda x: float(x.replace('kV', '').replace(',', '.')), reverse=True)
        except:
            pass
        return voltages
    
    def extract_year(self, filename: str) -> Optional[int]:
        """Izvlači godinu."""
        match = re.search(r'_(\d{4})', filename)
        if match:
            return int(match.group(1))
        return None
    
    def extract_voltages(self, text: str) -> List[str]:
        """Izvlači naponske nivoe."""
        voltages = set()
        for match in self.patterns['voltage'].finditer(text):
            voltage = match.group(1).replace(',', '.') + 'kV'
            voltages.add(voltage)
        return sorted(list(voltages), key=lambda x: float(x.replace('kV', '').replace(',', '.')), reverse=True)
    
    def extract_related_objects(self, text: str) -> List[str]:
        """Pronalazi reference na druge objekte."""
        related = set()
        text_lower = text.lower()
        text_latin = cyrillic_to_latin(text).lower()
        
        # Proveri registrovane objekte
        for code in self.object_codes:
            obj = self.object_codes[code]
            if code in text or obj.get('name_cyrillic', '') in text:
                related.add(code)
            # Proveri i aliase ako postoje
            for alias in obj.get('aliases', []):
                if alias.lower() in text_lower or alias.lower() in text_latin:
                    related.add(code)
        
        # Dodatna detekcija za elektrane (čak i ako nisu u registru)
        # TENT
        if any(p in text_lower or p in text_latin for p in ['tent a', 'тент а', 'tent-a']):
            related.add('TENT-A')
        if any(p in text_lower or p in text_latin for p in ['tent b', 'тент б', 'tent-b']):
            related.add('TENT-B')
        
        return list(related)
    
    def generate_keywords(self, text: str, section_number: str = None, object_name: str = None) -> List[str]:
        """Generiše ključne reči iz teksta."""
        keywords = set()
        # Konvertuj ćirilicu u latinicu za bolji matching
        text_latin = cyrillic_to_latin(text)
        text_lower = text_latin.lower()
        
        # Dodaj ime objekta kao ključnu reč (npr. "Kruševac 1", "Jagodina 4")
        if object_name:
            obj_name_latin = cyrillic_to_latin(object_name)
            keywords.add(obj_name_latin.lower())
            # Dodaj i samo ime grada bez broja
            parts = obj_name_latin.split()
            if len(parts) >= 2 and parts[0] in ['TS', 'RP', 'HE', 'TE', 'VE']:
                keywords.add(' '.join(parts[1:]).lower())  # npr. "Kruševac 1"
            elif len(parts) >= 1:
                keywords.add(parts[0].lower())  # npr. "Kruševac"
        
        # Dodaj skraćenice koje se pojavljuju
        for abbr in self.abbreviations:
            if abbr in text or abbr in text_latin:
                keywords.add(abbr)
        
        # Specifični termini - proširena lista (samo latinica jer konvertujemo tekst)
        key_terms = [
            # Osnovni termini (latinica - tekst je konvertovan)
            'ukljuceno', 'iskljuceno', 'ukljucenje', 'iskljucenje',
            'aktivna', 'diferencijalna',
            'spojno polje', 'sistem sabirnica',
            'zastita', 'paralel',
            # Oprema
            'prekidac', 'rastavljac', 'sabirnicki rastavljac', 'izlazni rastavljac',
            'dalekovod', 'transformator',
            # Manipulacije i nalozi
            'nalog', 'manipulacija',
            'dispecer', 'rukovalac',
            'potvrda', 'izvrsenje', 'informacija',
            # SCADA i signalizacija
            'scada', 'signalizacija', 'daljinsko',
            # Lokacije
            'postrojenje', 'prvi kraj', 'drugi kraj',
            # Uklopna stanja
            'uklopno stanje', 'pod naponom', 'bez napona',
            'normalno',
            # Obuka i komunikacija
            'obuk', 'naglasava', 'naznaci',
            'odgovorna osoba', 'komunikacija',
            'sagovornik', 'identifikacija',
            # Naponi i frekvencija u EES
            'napon', 'nazivni napon', 'nazivne vrednosti napona',
            'dozvoljeni napon', 'granica napona', 'granice napona',
            'opseg napona', 'naponski nivo', 'vrednost napona',
            'frekvencija', 'nazivna frekvencija',
            'opseg frekvencije', 'dozvoljeni opseg',
            # EES i prenosni sistem
            'ees', 'prenosni sistem', 'prenosna mreza', 'republika srbija'
        ]
        for term in key_terms:
            if term.lower() in text_lower:
                keywords.add(term)
        
        # Kontekstualno obogaćivanje za elektrane i generatore
        # TENT - Termoelektrana Nikola Tesla
        tent_patterns = ['tent', 'тент', 'nikola tesla', 'никола тесла']
        if any(p in text_lower for p in tent_patterns):
            keywords.update(['TENT', 'ТЕНТ', 'Nikola Tesla', 'termoelektrana', 'TE'])
            if any(p in text_lower for p in ['tent a', 'тент а', 'tent-a']):
                keywords.update(['TENT A', 'TENT-A', 'ТЕНТ А'])
            if any(p in text_lower for p in ['tent b', 'тент б', 'tent-b']):
                keywords.update(['TENT B', 'TENT-B', 'ТЕНТ Б'])
        
        # Generatori - prepoznaj G1-G6, Г1-Г6
        generator_pattern = re.compile(r'[ГG]\s*[1-6]|генератор|generator', re.IGNORECASE)
        if generator_pattern.search(text) or generator_pattern.search(text_latin):
            keywords.update(['generator', 'generatori', 'proizvodni modul'])
            # Dodaj konkretne generatore
            for i in range(1, 7):
                if f'Г{i}' in text or f'G{i}' in text_latin or f'g{i}' in text_lower:
                    keywords.add(f'G{i}')
                    keywords.add(f'Г{i}')
        
        # Hidroelektrane
        if any(p in text_lower for p in ['he ', 'хе ', 'hidroelektrana', 'хидроелектрана']):
            keywords.update(['hidroelektrana', 'HE'])
            if any(p in text_lower for p in ['djerdap', 'ђердап', 'đerdap']):
                keywords.update(['Đerdap', 'Djerdap', 'Ђердап'])
            if any(p in text_lower for p in ['bajina basta', 'бајина башта']):
                keywords.update(['Bajina Bašta', 'Bajina Basta', 'Бајина Башта'])
        
        # RHE - Reverzibilna hidroelektrana
        if any(p in text_lower for p in ['rhe', 'рхе', 'reverzibiln']):
            keywords.update(['RHE', 'reverzibilna hidroelektrana'])
        
        # Termoelektrane - ostale
        if any(p in text_lower for p in ['te kostolac', 'те костолац', 'kostolac']):
            keywords.update(['Kostolac', 'TE Kostolac', 'termoelektrana'])
        
        # Priključenje na prenosni sistem
        if any(p in text_lower for p in ['prikljuc', 'прикључ', 'povezan', 'повезан', 'napajan', 'напајањ']):
            keywords.update(['priključenje', 'prenosni sistem', 'povezivanje', 'napajanje'])
        
        # Kontekstualno obogaćivanje za sekcije o naponima i frekvenciji (Pravila o radu)
        if section_number:
            # Sekcija 3.3 - Naponi u prenosnoj mreži
            if section_number.startswith('3.3'):
                if any(w in text_lower for w in ['napon', 'kv', 'vrednost']):
                    keywords.update(['napon', 'nazivni napon', 'dozvoljeni napon', 'granica napona',
                                   'opseg napona', 'naponski nivo', 'EES', 'prenosna mreza',
                                   'dozvoljeni opseg napona', 'granice napona', 'Srbija'])
            # Sekcija 3.4 - Frekvencija
            if section_number.startswith('3.4'):
                if any(w in text_lower for w in ['frekvencij', 'hz']):
                    keywords.update(['frekvencija', 'nazivna frekvencija', 'opseg frekvencije',
                                   'dozvoljeni opseg frekvencije', 'EES', 'prenosni sistem'])
        
        # Kontekstualno obogaćivanje za specifične sekcije (manipulacije na dalekovodu)
        if section_number and section_number.startswith('6.3'):
            # Sekcija o davanju naloga - dodaj relevantne ključne reči
            if any(w in text_lower for w in ['dalekovod', 'nalog']):
                keywords.update(['dalekovod', 'nalog', 'dispecer'])
            if any(w in text_lower for w in ['informacij', 'izvrsen']):
                keywords.update(['potvrda izvrsenja', 'cekanje informacije', 'redosled manipulacija'])
            if any(w in text_lower for w in ['drug', 'kraj', 'prvom']):
                keywords.update(['prvi kraj dalekovoda', 'drugi kraj dalekovoda', 'postrojenje A', 'postrojenje B'])
            if any(w in text_lower for w in ['scada', 'signal']):
                keywords.update(['SCADA', 'signalizacija'])
        
        # Kontekstualno obogaćivanje za sekciju 6.5.5 (prelazak sa sistema na sistem)
        if section_number == '6.5.5':
            keywords.update(['prelazak sa sistema na sistem', 'prebacivanje sa sistema sabirnica',
                           'redosled manipulacija', 'prelazak na drugi sistem sabirnica',
                           'prvi sistem sabirnica', 'drugi sistem sabirnica',
                           'prebaciti izvode', 'aktivni izvodi', 'spojno polje ukljuciti',
                           'sabirnicki rastavljac', 'prelazak SS1 SS2', 'promena sistema sabirnica',
                           'redosled koraka prelazak', 'postupak prelaska sistema',
                           'manipulacije prelazak sabirnica', '400 kV prelazak', '220 kV prelazak',
                           '110 kV prelazak', 'rezervni sistem sabirnica'])
        
        # Kontekstualno obogaćivanje za sekciju 6.2 (identifikacija sagovornika)
        if section_number and section_number.startswith('6.2'):
            if any(w in text_lower for w in ['obuc', 'obuka']):
                # Ako se pominje obuka, dodaj relevantne ključne reči
                keywords.update(['dispecer na obuci', 'rukovalac na obuci', 'obuka', 
                                'nalog za manipulacije', 'izdavanje naloga', 'naznaciti rukovaocu',
                                'odgovorna osoba', 'prati komunikaciju', 'sagovornik na obuci'])
            if any(w in text_lower for w in ['naglas', 'naznac']):
                keywords.update(['neophodno naznaciti', 'posebno naglasava', 'pre pocetka manipulacija'])
        
        # Kontekstualno obogaćivanje za sekcije 7.x (neraspoloživost diferencijalne zaštite)
        # Ovo je posebno uklopno stanje u Uputstvima za pogon
        if section_number and section_number.startswith('7.'):
            if any(w in text_lower for w in ['neraspoloziv', 'diferencijaln', 'zastit', 'sabirnic']):
                keywords.update(['neraspoloziva diferencijalna zastita', 'diferencijalna zastita sabirnica',
                               'neraspoloziost', 'uklopno stanje', 'posebno uklopno stanje',
                               'pogon bez diferencijalne zastite', 'spojno polje isključeno'])
            # 7.1.1 - Kvar na sabirnicama visokog napona - detekcija distantnom zaštitom
            if section_number == '7.1.1':
                if any(w in text_lower for w in ['distantn', 'sabirnic', 'vodov', 'prekidac']):
                    keywords.update(['kvar na sabirnicama', 'ispad svih dalekovoda', 'svi dalekovodi ispadnu',
                                   'distantna zastita drugi stepen', 'potencijalni kvar sabirnice',
                                   'svi vodovi ispadnu', 'ispad dalekovoda distantnom zastitom',
                                   'gde je kvar', 'lokacija kvara sabirnice', 'sistem sabirnica'])
        
        # Kontekstualno obogaćivanje za sekciju 5.1.x (vrsta i priroda kvara na dalekovodima)
        if section_number and section_number.startswith('5.1'):
            # 5.1.3 - APU i priroda kvara (prolazni/trajni)
            if any(w in text_lower for w in ['apu', 'апу', 'uspesan', 'успешан', 'neuspesan', 'неуспешан', 'prolaz', 'пролаз', 'trajn', 'трајн']):
                keywords.update(['APU', 'automatsko ponovno ukljucenje', 'uspesan APU', 'uspesan ciklus APU',
                               'neuspesan APU', 'priroda kvara', 'prolazni kvar', 'trajni kvar',
                               'da li je dalekovod u pogonu', 'dalekovod u pogonu', 'ispad dalekovoda',
                               'ispad sa APU', 'ispad sa uspesnim APU', 'kvar prolaznog karaktera',
                               'kvar trajnog karaktera', 'vrsta kvara', 'utvrdjivanje prirode kvara'])
        
        # Kontekstualno obogaćivanje za sekciju 5.2.x (postupci nakon ispada dalekovoda)
        # Ključno za pitanja o stepenima zaštite i lokatorima kvara
        if section_number and section_number.startswith('5.2'):
            # 5.2.1 - Povratni napon i prolazni kvar
            if any(w in text_lower for w in ['povratn', 'повратн', 'prolaz', 'пролаз', 'ukljucen', 'укључен', 'iskljucen', 'искључен']):
                keywords.update(['povratni napon', 'prolazni kvar', 'jedna strana ukljucena',
                               'prekidac ukljucen', 'prekidac iskljucen', 'kvar prolazan',
                               'dalekovod u pogonu', 'uspesan APU', 'APU uspesan sa jedne strane',
                               'da li je dalekovod u pogonu', 'ispad sa uspesnim APU'])
            # 5.2.2 - Neuspešan APU sa obe strane
            if any(w in text_lower for w in ['neuspesan', 'неуспешан', 'obe strane', 'обе стране', '3 minut', '3 минут']):
                keywords.update(['neuspesan APU', 'APU neuspesan', 'neuspesan APU sa obe strane',
                               'obostrani ispad', 'cekanje 3 minuta', 'nalog za ukljucenje',
                               'probno ukljucenje', 'trajni kvar', 'ispad dalekovoda APU'])
            # 5.2.9 - Različiti stepeni distantne zaštite
            if any(w in text_lower for w in ['razlicit', 'stepen', 'visi', 'visem']):
                keywords.update(['prvi stepen', 'drugi stepen', 'I stepen', 'II stepen',
                               'razliciti stepeni', 'visi stepen', 'nizi stepen',
                               'distantna zastita stepen', 'odakle ukljuciti', 'odakle energisati',
                               'ko ukljucuje', 'koja strana ukljucuje'])
            # 5.2.9 - Lokator kvara i udaljenost
            if any(w in text_lower for w in ['lokator', 'lokacij', 'udaljen', 'mesto kvara']):
                keywords.update(['lokator kvara', 'pokazivanje lokatora', 'udaljenost kvara',
                               'km', 'kilometar', 'udaljenija strana', 'bliza strana',
                               'mesto kvara', 'lokacija kvara'])
            # 5.2.9 - Elektrane i hidroelektrane
            if any(w in text_lower for w in ['elektran', 'hidro', 'postrojenje']):
                keywords.update(['hidroelektrana', 'termoelektrana', 'elektrana',
                               'postrojenje sa elektranom', 'ka elektrani'])
            # 5.2.5 - Dvostruki dalekovod i radovi
            if any(w in text_lower for w in ['dvostruk', 'radov', 'blizin']):
                keywords.update(['dvostruki dalekovod', 'radovi u blizini napona',
                               'drugi sistem', 'ispad sistema', 'pробno ukljucenje'])
        
        # Kontekstualno obogaćivanje za sekcije o normalnom uklopnom stanju (raspored dalekovoda po sabirnicama)
        # Ove sekcije opisuju koji dalekovodi su na kom sistemu sabirnica
        if any(w in text_lower for w in ['sistem sabirnic', '1. sistem', '2. sistem', 'prvi sistem', 'drugi sistem']):
            if any(w in text_lower for w in ['dv ', 'dv1', 'dv2', 'dalekovod', 'mv ', 'tr1', 'tr2']):
                keywords.update(['koji dalekovodi', 'dalekovodi na sistemu sabirnica', 'raspored dalekovoda',
                               'prvi sistem sabirnica', 'drugi sistem sabirnica', '1. sistem sabirnica',
                               '2. sistem sabirnica', 'koji dalekovodi polaze', 'dalekovodi sa sabirnica',
                               'normalno uklopno stanje', 'postrojenje 110 kv', 'postrojenje 400 kv',
                               'postrojenje 220 kv', 'povezani na sistem sabirnica'])
        
        return list(keywords)
    
    def augment_content(self, content: str, section_number: str, text_lower: str) -> str:
        """
        Obogaćuje sadržaj chunk-a sa tipičnim formulacijama pitanja.
        Ovo pomaže i semantičkom i BM25 pretraživanju bez query expansion-a.
        """
        augmentations = []
        
        # 5.1.3 - APU i priroda kvara (prolazni/trajni)
        if section_number == '5.1.3':
            augmentations.extend([
                "Tipična pitanja: Došlo je do ispada dalekovoda sa uspešnim ciklusom APU, da li je dalekovod u pogonu?",
                "Ispad DV sa uspešnim APU - kakav je kvar, prolazni ili trajni?",
                "APU uspešan bar sa jednog kraja - priroda kvara?",
                "Uspešan APU = prolazni kvar, dalekovod u pogonu.",
                "Neuspešan APU = trajni kvar, potrebna provera."
            ])
        
        # 5.2.1 - Povratni napon i prolazni kvar
        if section_number == '5.2.1':
            augmentations.extend([
                "Tipična pitanja: Prekidač sa jedne strane iskljucen, sa druge ukljucen - da li je dalekovod u pogonu?",
                "Postoji povratni napon na dalekovodu - kakav je kvar?",
                "Ispad sa uspešnim APU sa jedne strane - kvar je prolazan.",
                "Dalekovod u pogonu jer ima povratni napon sa drugog kraja."
            ])
        
        # 5.2.2 - Neuspešan APU sa obe strane
        if section_number == '5.2.2':
            augmentations.extend([
                "Tipična pitanja: Neuspešan APU sa obe strane dalekovoda - koliko čekati pre ukljucenja?",
                "Obostrani ispad bez uspešnog APU - postupak dispečera?",
                "Najamanje 3 minuta čekanja posle ispada, jedan nalog za ukljucenje.",
                "Neuspešan APU - probno ukljucenje posle 3 minuta."
            ])
        
        # 5.2.9 - Različiti stepeni distantne zaštite i lokatori
        if section_number == '5.2.9':
            augmentations.extend([
                # Formulacije za stepene zaštite
                "Tipična pitanja: Distantna zaštita prvi stepen u A, drugi stepen u B - odakle energisati?",
                "A ima I stepen, B ima II stepen reagovanje - ko treba da uključi dalekovod?",
                "Ispad DV sa različitim stepenima zaštite na krajevima.",
                # Formulacije za lokatore
                "Lokator kvara pokazuje različite udaljenosti - koja strana uključuje?",
                "Pokazivanja lokatora: jedna strana bliža kvaru, druga udaljenija.",
                "Udaljenost kvara prema lokatorima - odakle ukljuciti u prazan hod?",
                "Drmno 100 km, Đerdap 55 km - koja strana uključuje dalekovod?",
                "Lokator pokazuje 100 km i 55 km - sa koje strane energisati?",
                "Pokazivanja: 100 km i 55 km - koja strana uključuje isključeni DV?",
                # Generičke formulacije sa postrojenjima A i B
                "Ispad dalekovoda koji spaja postrojenja A i B - iz kog postrojenja dispečer treba da stavi dalekovod pod napon?",
                "Lokator u postrojenju A pokazuje 40 km, u postrojenju B pokazuje 20 km - ko uključuje?",
                "Iz kog postrojenja dispečer stavlja dalekovod pod napon na osnovu lokatora kvara?",
                "Dalekovod ispao, lokator pokazuje različite km sa dve strane - odakle energisati?",
                "Lokator pokazuje da je kvar bliži jednom postrojenju - dispečer uključuje sa udaljenije strane.",
                # Specifični primeri sa Drmno i Đerdap
                "Ispad DV 401/2 između RP Drmno i RP Đerdap 1 - iz kog postrojenja dispečer stavlja pod napon?",
                "TE Kostolac B i HE Đerdap 1 - sa koje strane uključiti ispali dalekovod?",
                "Dalekovod 401/2 ispao, Drmno 100 km, Đerdap 55 km - koja strana uključuje?"
            ])
        
        # 5.2.5 - Dvostruki DV i radovi u blizini napona
        if section_number == '5.2.5':
            augmentations.extend([
                "Tipična pitanja: Jedan sistem DV isključen za radove, drugi ispada - da li je dozvoljeno probno uključenje?",
                "Dvostruki dalekovod - radovi na jednom sistemu, ispad drugog sistema.",
                "Radovi u blizini napona na jednom sistemu dvosturkog DV."
            ])
        
        # 6.5.1 (2.01) - Rastavljači kada je prekidač isključen samo sa jedne strane
        if section_number == '6.5.1':
            augmentations.extend([
                "Tipična pitanja: Prekidač u A isključen, u B uključen - mogu li se isključiti rastavljači?",
                "Da li smemo isključiti rastavljače kada je prekidač samo sa jedne strane isključen?",
                "Rastavljači u postrojenju gde je prekidač uključen - dozvoljeno isključenje?"
            ])
        
        # 6.3.1 (2.01) - Rukovalac greškom isključio prekidač
        if section_number == '6.3.1':
            augmentations.extend([
                "Tipična pitanja: Rukovalac greškom isključio pogrešan prekidač - može li sam da ga uključi?",
                "Greška rukovaoca - isključen pogrešan DV prekidač, sme li ponovo ukljuciti bez dispečera?",
                "Samostalno uključenje nakon greške rukovaoca."
            ])
        
        # 3.1.19 (2.01) - Rastavljač za vidno odvajanje
        if section_number == '3.1.19':
            augmentations.extend([
                "Tipična pitanja: Koji element služi da vidno odvoji neki element od drugog koji je pod naponom?",
                "Šta vidno odvaja element od dela koji je naponit?",
                "Uređaj za vidno odvajanje elementa od onog pod naponom."
            ])
        
        # 6.7.2 (2.01) - Upravljanje iz pogonskog mehanizma
        if section_number == '6.7.2':
            augmentations.extend([
                "Tipična pitanja: DV naponit i opterećen - dopušteno upravljanje iz pogonskog mehanizma prekidača?",
                "Kad je dozvoljeno upravljanje prekidačem iz pogonskog mehanizma?",
                "Isključenje/uključenje iz pogonskog mehanizma - uslovi."
            ])
        
        # 6.3.7 (2.01) - SCADA signalizacija i potvrda rukovaoca
        if section_number == '6.3.7':
            augmentations.extend([
                "Tipična pitanja: SCADA pokazuje da su rastavljači isključeni ali rukovalac nije javio - može li dispečer dati nalog?",
                "Čekanje potvrde rukovaoca pre nego dispečer da sledeći nalog.",
                "SCADA signalizacija bez potvrde rukovaoca."
            ])
        
        # 6.5.5 (2.01) - Prelazak sa sistema na sistem (sa jednog na drugi sistem sabirnica)
        if section_number == '6.5.5':
            augmentations.extend([
                "Tipična pitanja: Kako se vrši prelazak sa jednog na drugi sistem sabirnica?",
                "Redosled manipulacija za prelazak sa prvog na drugi sistem sabirnica.",
                "Redosled manipulacija za prebacivanje sa sistema sabirnica 1 na sistem sabirnica 2.",
                "Prelazak sa SS1 na SS2 - redosled koraka.",
                "Koji je postupak za prebacivanje izvoda sa jednog sistema sabirnica na drugi?",
                "Kako prebaciti dalekovode sa prvog na drugi sistem sabirnica?",
                "Prelazak TS na drugi sistem sabirnica 400 kV - redosled.",
                "Prelazak TS na drugi sistem sabirnica 220 kV - redosled.",
                "Prelazak TS na drugi sistem sabirnica 110 kV - redosled.",
                "Postupak za prelazak na rezervni sistem sabirnica.",
                "Manipulacije za promenu sistema sabirnica u postrojenju.",
                "Napiši redosled manipulacija za prelazak sa prvog na drugi sistem sabirnica.",
                "Kako se prebacuju aktivni izvodi sa jednog na drugi sistem sabirnica?",
                "Spojno polje - ukljucenje za prelazak na drugi sistem."
            ])
        
        if augmentations:
            aug_text = "\n\n[Kontekst za pretragu: " + " | ".join(augmentations) + "]"
            return content + aug_text
        
        return content
    
    def generate_chunk_id(self, doc_id: str, section: str, index: int = 0) -> str:
        """Generiše jedinstveni ID."""
        base = f"{doc_id}_{section}_{index}"
        return hashlib.md5(base.encode()).hexdigest()[:12]
    
    def detect_section_type(self, title: str) -> str:
        """Detektuje tip sekcije."""
        title_lower = title.lower()
        
        if any(kw in title_lower for kw in ['експлоатациони', 'eksploatacioni']):
            return 'eksploatacioni_uslovi'
        elif any(kw in title_lower for kw in ['анализ', 'сигурност', 'кратк']):
            return 'analiza_sigurnosti'
        elif any(kw in title_lower for kw in ['паралел', 'paralel', 'суседн']):
            return 'paralelan_rad'
        elif any(kw in title_lower for kw in ['нормално уклопно', 'normalno uklopno']):
            return 'normalno_uklopno_stanje'
        elif any(kw in title_lower for kw in ['погон', 'без', 'нерасполож']):
            return 'posebno_uklopno_stanje'
        elif any(kw in title_lower for kw in ['речник', 'појм', 'дефиниц']):
            return 'recnik_pojmova'
        
        return 'general'
    
    def chunk_recnik(self, content: str, doc_id: str, doc_title: str) -> List[Chunk]:
        """Chunk-uje rečnik pojmova - svaka definicija = jedan chunk."""
        chunks = []
        file_num = self.extract_file_num(doc_title)
        matches = self.patterns['term_definition'].findall(content)
        
        for i, (num, term, definition) in enumerate(matches):
            definition = definition.strip()
            
            if len(definition) < 30:
                continue
            
            full_content = f"### {num}. {term}\n\n{definition}"
            
            chunk = Chunk(
                file_num=file_num,
                chunk_id=self.generate_chunk_id(doc_id, f"term_{num}", i),
                doc_title=doc_title,
                content=full_content,
                doc_id=doc_id,
                doc_type='recnik',
                object_code=None,
                object_name=None,
                voltage_levels=self.extract_voltages(definition),
                section_number=num,
                section_title=term.strip(),
                section_type='recnik_pojmova',
                chunk_type='A',
                related_objects=self.extract_related_objects(definition),
                keywords=self.generate_keywords(definition),
                year=2023,
                char_count=len(full_content),
                hierarchy=[],
                parent_section=None,
                parent_title=None
            )
            chunks.append(chunk)
        
        return chunks
    
    def chunk_uputstvo_pogon(self, content: str, doc_id: str, doc_title: str,
                             object_code: str, year: int) -> List[Chunk]:
        """
        Chunk-uje uputstvo za pogon - DELI PO ## (dve tarabe).
        Svaka podsekcija (## X.Y) postaje jedan chunk.
        Svaki chunk obavezno dobija roditeljski naslov (### X. ...).
        """
        chunks: List[Chunk] = []
        file_num = self.extract_file_num(doc_title)

        object_info = self.object_codes.get(object_code, {})
        # Pokušaj da izvučeš pravo ime iz doc_title, inače fallback na registry/code
        object_name = self.extract_object_name(doc_title) or object_info.get('name') or f'Objekat {object_code}'
        
        # Izvuci naponske nivoe iz naziva fajla (pouzdanije nego iz teksta)
        doc_voltage_levels = self.extract_voltage_levels_from_filename(doc_title)

        # Pronađi sve roditeljske naslove (### X. NASLOV) sa pozicijama u tekstu
        parent_headers: List[Tuple[int, str, str]] = []  # (pos, num, title)
        for m in re.finditer(r'^[\t ]*###\s*(\d+)\.\s*(.+)$', content, flags=re.MULTILINE):
            parent_headers.append((m.start(), m.group(1), m.group(2).strip()))

        # Ako postoji barem jedna ## podsekcija, chunkuj po ##.
        # U suprotnom fallback na staro ponašanje (### sekcije).
        has_subsections = re.search(r'^[\t ]*##\s*\d+\.\d+', content, flags=re.MULTILINE) is not None
        if not has_subsections:
            # Fallback: zadrži postojeće ponašanje (### = chunk)
            sections = re.split(r'(?=^### \d+\.)', content, flags=re.MULTILINE)
            for i, section in enumerate(sections):
                section = section.strip()
                if not section:
                    continue
                match = re.match(r'^### (\d+)\.\s*(.+)', section)
                if not match:
                    continue
                section_num = match.group(1)
                section_title = match.group(2).strip()
                section_type = self.detect_section_type(section_title)

                if 'uklopno' in section_type:
                    chunk_type = 'C' if 'normalno' in section_type else 'D'
                elif 'paralelan' in section_type:
                    chunk_type = 'E'
                elif 'eksploatacioni' in section_type:
                    chunk_type = 'B'
                elif 'analiza' in section_type:
                    chunk_type = 'F'
                else:
                    chunk_type = 'G'

                if len(section) > self.MAX_CHUNK_SIZE:
                    sub_chunks = self._split_large_section(
                        section, doc_id, doc_title, object_code, object_name,
                        section_num, section_title, section_type, chunk_type, year, doc_voltage_levels
                    )
                    chunks.extend(sub_chunks)
                else:
                    chunks.append(
                        Chunk(
                            file_num=file_num,
                            chunk_id=self.generate_chunk_id(doc_id, f"sec_{section_num}", i),
                            doc_title=doc_title,
                            content=section,
                            doc_id=doc_id,
                            doc_type='uputstvo_pogon',
                            object_code=object_code,
                            object_name=object_name,
                            voltage_levels=doc_voltage_levels or self.extract_voltages(section),
                            section_number=section_num,
                            section_title=section_title,
                            section_type=section_type,
                            chunk_type=chunk_type,
                            related_objects=self.extract_related_objects(section),
                            keywords=self.generate_keywords(section, section_num, object_name),
                            year=year,
                            char_count=len(section),
                            hierarchy=[],
                            parent_section=None,
                            parent_title=None,
                        )
                    )
            return chunks

        # Chunkovanje po ## podsekcijama (2 tarabe)
        # Lookahead da sačuvamo delimiter
        subsections = re.split(r'(?=^[\t ]*##\s*\d+\.\d+)', content, flags=re.MULTILINE)
        
        # NOVO: Prvo obradimo sekcije koje NEMAJU ## podsekcije ali imaju - X.Y stavke
        # (npr. sekcija 2. EKSPLOATACIONI USLOVI i 3. REZULTATI ANALIZE)
        processed_sections = set()  # Pratimo koje ### sekcije imaju ## podsekcije
        for block in subsections:
            sub_match = re.search(r'^[\t ]*##\s*(\d+)\.\d+', block, flags=re.MULTILINE)
            if sub_match:
                processed_sections.add(sub_match.group(1))
        
        # Obradi ### sekcije koje nemaju ## podsekcije
        for ppos, pnum, ptitle in parent_headers:
            if pnum in processed_sections:
                continue  # Ova sekcija ima ## podsekcije, biće obrađena dole
            
            # Pronađi kraj ove ### sekcije (do sledeće ### ili kraja)
            next_pos = len(content)
            for npos, nnum, _ in parent_headers:
                if npos > ppos:
                    next_pos = npos
                    break
            
            section_content = content[ppos:next_pos].strip()
            if not section_content or len(section_content) < self.MIN_CHUNK_SIZE:
                continue
            
            section_type = self.detect_section_type(ptitle)
            
            # Proveri da li ima - X.Y ili - X.Y. stavke (bullet liste)
            # Regex podržava oba formata: "- 2.1 tekst" i "- 2.1. tekst"
            bullet_items = re.findall(r'^-\s*(\d+\.\d+\.?)\s+(.+?)(?=\n-\s*\d+\.\d+|\n###|\Z)', 
                                     section_content, re.MULTILINE | re.DOTALL)
            
            if bullet_items:
                # Obradi svaku stavku kao poseban chunk
                for item_num, item_content in bullet_items:
                    item_content = item_content.strip()
                    if len(item_content) < 30:
                        continue
                    
                    full_content = f"### {pnum}. {ptitle}\n\n- {item_num} {item_content}"
                    
                    if 'uklopno' in section_type:
                        chunk_type = 'C' if 'normalno' in section_type else 'D'
                    elif 'paralelan' in section_type:
                        chunk_type = 'E'
                    elif 'eksploatacioni' in section_type:
                        chunk_type = 'B'
                    elif 'analiza' in section_type:
                        chunk_type = 'F'
                    else:
                        chunk_type = 'G'
                    
                    chunks.append(
                        Chunk(
                            file_num=file_num,
                            chunk_id=self.generate_chunk_id(doc_id, f"item_{item_num}"),
                            doc_title=doc_title,
                            content=full_content,
                            doc_id=doc_id,
                            doc_type='uputstvo_pogon',
                            object_code=object_code,
                            object_name=object_name,
                            voltage_levels=doc_voltage_levels or self.extract_voltages(full_content),
                            section_number=item_num,
                            section_title=ptitle,
                            section_type=section_type,
                            chunk_type=chunk_type,
                            related_objects=self.extract_related_objects(item_content),
                            keywords=self.generate_keywords(item_content, item_num, object_name),
                            year=year,
                            char_count=len(full_content),
                            hierarchy=[{'number': pnum, 'title': ptitle}],
                            parent_section=pnum,
                            parent_title=ptitle,
                        )
                    )
            else:
                # Nema bullet stavki, cela sekcija = jedan chunk
                if 'uklopno' in section_type:
                    chunk_type = 'C' if 'normalno' in section_type else 'D'
                elif 'paralelan' in section_type:
                    chunk_type = 'E'
                elif 'eksploatacioni' in section_type:
                    chunk_type = 'B'
                elif 'analiza' in section_type:
                    chunk_type = 'F'
                else:
                    chunk_type = 'G'
                
                chunks.append(
                    Chunk(
                        file_num=file_num,
                        chunk_id=self.generate_chunk_id(doc_id, f"sec_{pnum}"),
                        doc_title=doc_title,
                        content=section_content,
                        doc_id=doc_id,
                        doc_type='uputstvo_pogon',
                        object_code=object_code,
                        object_name=object_name,
                        voltage_levels=doc_voltage_levels or self.extract_voltages(section_content),
                        section_number=pnum,
                        section_title=ptitle,
                        section_type=section_type,
                        chunk_type=chunk_type,
                        related_objects=self.extract_related_objects(section_content),
                        keywords=self.generate_keywords(section_content, pnum, object_name),
                        year=year,
                        char_count=len(section_content),
                        hierarchy=[],
                        parent_section=None,
                        parent_title=None,
                    )
                )

        # Pronađi sve međunaslove (## X.Y bez treće cifre, npr. ## 7.1 NERASPOLOŽIVOST...)
        intermediate_headers: List[Tuple[int, str, str]] = []  # (pos, num, title)
        for m in re.finditer(r'^[\t ]*##\s*(\d+\.\d+)\s+([A-ZА-ЯČĆŽŠĐЉЊ].+)$', content, flags=re.MULTILINE):
            # Proveri da nije ## X.Y.Z (ima tačku i treću cifru)
            num = m.group(1)
            if not re.match(r'^\d+\.\d+\.$', num):  # Nije X.Y. (sa tačkom na kraju)
                intermediate_headers.append((m.start(), num, m.group(2).strip()))

        def _parent_for_pos(pos: int) -> Tuple[Optional[str], Optional[str]]:
            parent_num = None
            parent_title = None
            for ppos, pnum, ptitle in parent_headers:
                if ppos <= pos:
                    parent_num = pnum
                    parent_title = ptitle
                else:
                    break
            return parent_num, parent_title

        def _intermediate_for_pos(pos: int, sub_num: str) -> Tuple[Optional[str], Optional[str]]:
            """Pronađi najbliži međunaslov (## X.Y) iznad pozicije koji odgovara sub_num."""
            # sub_num je npr. "7.1.1" - tražimo međunaslov "7.1"
            parts = sub_num.rstrip('.').split('.')
            if len(parts) >= 2:
                target_prefix = f"{parts[0]}.{parts[1]}"
                for ipos, inum, ititle in reversed(intermediate_headers):
                    if ipos < pos and inum == target_prefix:
                        return inum, ititle
            return None, None

        chunk_index = 0
        for block in subsections:
            block = block.strip()
            if not block or len(block) < self.MIN_CHUNK_SIZE:
                continue
            
            # Preseci block ako sadrži ### X. (parent header) - ne dozvoljavamo da chunk prelazi u novu glavnu sekciju
            parent_break = re.search(r'^[\t ]*###\s*\d+\.', block, flags=re.MULTILINE)
            if parent_break and parent_break.start() > 0:
                # Uzmi samo deo pre ### X.
                block = block[:parent_break.start()].strip()
                if not block or len(block) < self.MIN_CHUNK_SIZE:
                    continue

            # Pronađi broj i naslov podsekcije
            # Match samo prve linije (block je višelinijski)
            sub_match = re.match(r'^[\t ]*##\s*(\d+\.\d+\.?\d*)\s*(.+)', block)
            if not sub_match:
                continue

            sub_num = sub_match.group(1)
            sub_title = sub_match.group(2).strip()

            # Odredi roditelja po poziciji u originalnom tekstu (najbliži ### iznad)
            pos = content.find(block.splitlines()[0])
            parent_num, parent_title = _parent_for_pos(pos if pos >= 0 else 0)
            
            # Pronađi međunaslov (## X.Y) ako postoji (npr. ## 7.1 NERASPOLOŽIVOST...)
            inter_num, inter_title = _intermediate_for_pos(pos if pos >= 0 else 0, sub_num)
            
            # Gradi header koji će se dodati na početak chunka
            headers_to_add = []
            hierarchy = []
            
            if parent_num and parent_title:
                headers_to_add.append(f"### {parent_num}. {parent_title}")
                hierarchy.append({'number': parent_num, 'title': parent_title})
            
            if inter_num and inter_title:
                headers_to_add.append(f"## {inter_num} {inter_title}")
                hierarchy.append({'number': inter_num, 'title': inter_title})
            
            # Dodaj headere na početak bloka ako već nisu tu
            if headers_to_add and not block.startswith('###'):
                block = "\n\n".join(headers_to_add) + "\n\n" + block

            # Tip sekcije i chunk-a proceni iz međunaslova, roditeljskog ili child naslova
            basis_title = inter_title if inter_title else (parent_title if parent_title else sub_title)
            section_type = self.detect_section_type(basis_title)
            if 'uklopno' in section_type:
                chunk_type = 'C' if 'normalno' in section_type else 'D'
            elif 'paralelan' in section_type:
                chunk_type = 'E'
            elif 'eksploatacioni' in section_type:
                chunk_type = 'B'
            elif 'analiza' in section_type:
                chunk_type = 'F'
            else:
                chunk_type = 'G'

            chunks.append(
                Chunk(
                    file_num=file_num,
                    chunk_id=self.generate_chunk_id(doc_id, f"subsec_{sub_num}", chunk_index),
                    doc_title=doc_title,
                    content=block,
                    doc_id=doc_id,
                    doc_type='uputstvo_pogon',
                    object_code=object_code,
                    object_name=object_name,
                    voltage_levels=doc_voltage_levels or self.extract_voltages(block),
                    section_number=sub_num,
                    section_title=sub_title,
                    section_type=section_type,
                    chunk_type=chunk_type,
                    related_objects=self.extract_related_objects(block),
                    keywords=self.generate_keywords(block, sub_num, object_name),
                    year=year,
                    char_count=len(block),
                    hierarchy=hierarchy,
                    parent_section=parent_num,
                    parent_title=parent_title,
                )
            )
            chunk_index += 1

        return chunks
    
    def _split_large_section(self, section: str, doc_id: str, doc_title: str,
                             object_code: str, object_name: str,
                             parent_num: str, parent_title: str,
                             section_type: str, chunk_type: str, year: int,
                             doc_voltage_levels: List[str] = None) -> List[Chunk]:
        """Deli veliku sekciju po ## (dve tarabe) podsekcijama."""
        chunks = []
        file_num = self.extract_file_num(doc_title)
        
        # Izvuci header sekcije (### X. NASLOV)
        header_match = re.match(r'^(### \d+\.\s*.+?)(?=\n##|\n-|\Z)', section, re.DOTALL)
        header = header_match.group(1).strip() if header_match else f"### {parent_num}. {parent_title}"
        
        # Podeli po ## (dve tarabe)
        subsections = re.split(r'(?=^## \d+\.\d+)', section, flags=re.MULTILINE)
        
        for j, subsec in enumerate(subsections):
            subsec = subsec.strip()
            if not subsec or len(subsec) < self.MIN_CHUNK_SIZE:
                continue
            
            # Pronađi broj i naslov podsekcije
            sub_match = re.match(r'^## (\d+\.\d+\.?\d*)\s*(.+)', subsec)
            if sub_match:
                sub_num = sub_match.group(1)
                sub_title = sub_match.group(2).strip()
            else:
                sub_num = f"{parent_num}.{j}"
                sub_title = parent_title
            
            # Dodaj header ako nije prisutan
            if not subsec.startswith('###'):
                subsec = f"{header}\n\n{subsec}"
            
            chunk = Chunk(
                file_num=file_num,
                chunk_id=self.generate_chunk_id(doc_id, f"subsec_{sub_num}", j),
                doc_title=doc_title,
                content=subsec,
                doc_id=doc_id,
                doc_type='uputstvo_pogon',
                object_code=object_code,
                object_name=object_name,
                voltage_levels=doc_voltage_levels or self.extract_voltages(subsec),
                section_number=sub_num,
                section_title=sub_title,
                section_type=section_type,
                chunk_type=chunk_type,
                related_objects=self.extract_related_objects(subsec),
                keywords=self.generate_keywords(subsec, sub_num, object_name),
                year=year,
                char_count=len(subsec),
                hierarchy=[{'number': parent_num, 'title': parent_title}],
                parent_section=parent_num,
                parent_title=parent_title
            )
            chunks.append(chunk)
        
        return chunks
    
    def chunk_tehnicko_uputstvo(self, content: str, doc_id: str, doc_title: str, year: int) -> List[Chunk]:
        """Chunk-uje tehničko uputstvo po ## podsekcijama.
        
        Ako dokument ima ### X. i ## X.Y format, svaka ## podsekcija = chunk.
        Ako dokument ima samo ## X. format bez ###, svaka ## sekcija = chunk.
        """
        chunks = []
        file_num = self.extract_file_num(doc_title)
        
        # Pronađi sve ### roditeljske naslove
        parent_headers: List[Tuple[int, str, str]] = []  # (pos, num, title)
        for m in re.finditer(r'^[\t ]*###\s*(\d+)\.\s*(.+)$', content, flags=re.MULTILINE):
            parent_headers.append((m.start(), m.group(1), m.group(2).strip()))
        
        # Pronađi sve ## headere - podržava i headere bez naslova (npr. "## 6.7.2. Sadržaj...")
        # Regex: ## broj. (opcionalno naslov)
        sub_headers: List[Tuple[int, str, str]] = []  # (pos, num, title)
        for m in re.finditer(r'^[\t ]*##\s*(\d+(?:\.\d+)+)\.?\s*(.*)$', content, flags=re.MULTILINE):
            num = m.group(1).rstrip('.')
            title = m.group(2).strip()
            # Ako "naslov" počinje malim slovom, to je sadržaj - tretiraj kao header bez naslova
            if title and not title[0].isupper():
                title = ""  # Nema naslova, samo broj
            sub_headers.append((m.start(), num, title))
        
        # Proveri da li postoje ## X.Y podsekcije
        has_subsections = len(sub_headers) > 0
        
        if has_subsections and parent_headers:
            # Imamo ### X. i ## X.Y strukturu
            # Svaki ## chunk treba da ima SVE headere iznad sebe u hijerarhiji
            
            # Kombinuj sve headere
            all_headers = [(pos, num, title, '###') for pos, num, title in parent_headers]
            all_headers += [(pos, num, title, '##') for pos, num, title in sub_headers]
            all_headers.sort(key=lambda x: x[0])
            
            def _get_hierarchy_headers(target_num: str, target_pos: int) -> List[Tuple[str, str, str]]:
                """Pronađi sve headere iznad target_num u hijerarhiji."""
                hierarchy = []
                parts = target_num.split('.')
                
                # Za 4.1.1, tražimo ### 4. i ## 4.1
                # Prvo dodaj ### X. parent
                for ppos, pnum, ptitle in parent_headers:
                    if ppos < target_pos and parts[0] == pnum:
                        hierarchy.append((pnum, ptitle, '###'))
                        break
                
                # Zatim dodaj ## X.Y intermediate headere
                for i in range(2, len(parts)):
                    prefix = '.'.join(parts[:i])
                    for hpos, hnum, htitle in sub_headers:
                        if hpos < target_pos and hnum == prefix:
                            hierarchy.append((hnum, htitle, '##'))
                            break
                
                return hierarchy
            
            chunk_index = 0
            for pos, num, title in sub_headers:
                # Pronađi kraj ovog headera
                end_pos = len(content)
                for hpos, hnum, htitle in sub_headers:
                    if hpos > pos:
                        end_pos = hpos
                        break
                # Takođe proveri ### headere
                for hpos, hnum, htitle in parent_headers:
                    if hpos > pos and hpos < end_pos:
                        end_pos = hpos
                        break
                
                block = content[pos:end_pos].strip()
                if not block or len(block) < self.MIN_CHUNK_SIZE:
                    continue
                
                # Pronađi sve headere iznad u hijerarhiji
                hierarchy_headers = _get_hierarchy_headers(num, pos)
                
                # Proveri da li ima bullet stavke (- X.Y.Z) unutar bloka
                # Podržavamo DVA scenarija:
                # 1. Potomci: ## 6.2 ima potomke - 6.2.1, - 6.2.2 (startswith num + '.')
                # 2. Sestre: ## 4.1.2 ima sestre - 4.1.3, - 4.1.4 (isti parent, veći broj)
                all_bullet_items = re.findall(r'^-\s*(\d+(?:\.\d+)+\.?)\s+(.+?)(?=\n-\s*\d+(?:\.\d+)+\.?\s+|\n##|\n###|\Z)', 
                                         block, re.MULTILINE | re.DOTALL)
                header_depth = len(num.split('.'))
                header_parts = num.split('.')
                
                # Scenario 1: Potomci (npr. 6.2 -> 6.2.1, 6.2.2)
                bullet_items = [(item_num, item_content) for item_num, item_content in all_bullet_items 
                               if item_num.rstrip('.').startswith(num + '.') and 
                                  len(item_num.rstrip('.').split('.')) == header_depth + 1]
                
                # Scenario 2: Sestre (npr. 4.1.2 -> 4.1.3, 4.1.4 itd.)
                # Ako nema potomaka, proveri da li ima sestre na istom nivou
                if not bullet_items and header_depth >= 2:
                    parent_prefix = '.'.join(header_parts[:-1]) + '.'  # npr. "4.1."
                    current_last = int(header_parts[-1])  # npr. 2 za "4.1.2"
                    sibling_items = []
                    for item_num, item_content in all_bullet_items:
                        item_clean = item_num.rstrip('.')
                        item_parts = item_clean.split('.')
                        # Proveri da li je ista dubina i isti parent
                        if len(item_parts) == header_depth and item_clean.startswith(parent_prefix):
                            try:
                                item_last = int(item_parts[-1])
                                # Sestre imaju veći poslednji broj od header-a
                                if item_last > current_last:
                                    sibling_items.append((item_num, item_content))
                            except ValueError:
                                pass
                    bullet_items = sibling_items
                
                if bullet_items:
                    # PRVO: Kreiraj chunk za sadržaj pre prve bullet stavke (ako postoji)
                    # Dinamički konstruiši regex za prvi bullet match
                    if bullet_items:
                        first_item_num = bullet_items[0][0].rstrip('.')
                        first_bullet_match = re.search(r'^-\s*' + re.escape(first_item_num) + r'\.?\s+', block, re.MULTILINE)
                    else:
                        first_bullet_match = None
                    if first_bullet_match and first_bullet_match.start() > 0:
                        pre_bullet_content = block[:first_bullet_match.start()].strip()
                        # Proveri da li ima dovoljno sadržaja (ne samo header)
                        header_end = pre_bullet_content.find('\n')
                        if header_end > 0:
                            actual_content = pre_bullet_content[header_end:].strip()
                            if len(actual_content) >= 30:
                                # Gradi headers text sa svim headerima iznad
                                headers_text = ""
                                hierarchy_list = []
                                for hnum, htitle, htype in hierarchy_headers:
                                    headers_text += f"{htype} {hnum}. {htitle}\n\n"
                                    hierarchy_list.append({'number': hnum, 'title': htitle})
                                
                                full_content = headers_text + pre_bullet_content
                                
                                chunk = Chunk(
                                    file_num=file_num,
                                    chunk_id=self.generate_chunk_id(doc_id, f"tu_sub_{num}", chunk_index),
                                    doc_title=doc_title,
                                    content=full_content,
                                    doc_id=doc_id,
                                    doc_type='tehnicko_uputstvo',
                                    object_code=None,
                                    object_name=None,
                                    voltage_levels=self.extract_voltages(actual_content),
                                    section_number=num,
                                    section_title=title if title else f"Sekcija {num}",
                                    section_type='tehnicko_uputstvo',
                                    chunk_type='T',
                                    related_objects=self.extract_related_objects(actual_content),
                                    keywords=self.generate_keywords(actual_content, num),
                                    year=year,
                                    char_count=len(full_content),
                                    hierarchy=hierarchy_list,
                                    parent_section=hierarchy_headers[-1][0] if hierarchy_headers else None,
                                    parent_title=hierarchy_headers[-1][1] if hierarchy_headers else None
                                )
                                chunks.append(chunk)
                                chunk_index += 1
                    
                    # ZATIM: Obradi svaku bullet stavku kao poseban chunk
                    for item_num, item_content in bullet_items:
                        item_num = item_num.rstrip('.')
                        item_content = item_content.strip()
                        if len(item_content) < 30:
                            continue
                        
                        # Gradi headers text sa svim headerima iznad + trenutni ## header
                        headers_text = ""
                        hierarchy_list = []
                        for hnum, htitle, htype in hierarchy_headers:
                            headers_text += f"{htype} {hnum}. {htitle}\n\n"
                            hierarchy_list.append({'number': hnum, 'title': htitle})
                        
                        # Dodaj trenutni ## header
                        headers_text += f"## {num}. {title}\n\n"
                        hierarchy_list.append({'number': num, 'title': title})
                        
                        full_content = headers_text + f"- {item_num}. {item_content}"
                        
                        chunk = Chunk(
                            file_num=file_num,
                            chunk_id=self.generate_chunk_id(doc_id, f"tu_item_{item_num}", chunk_index),
                            doc_title=doc_title,
                            content=full_content,
                            doc_id=doc_id,
                            doc_type='tehnicko_uputstvo',
                            object_code=None,
                            object_name=None,
                            voltage_levels=self.extract_voltages(item_content),
                            section_number=item_num,
                            section_title=title,  # naslov parent sekcije
                            section_type='tehnicko_uputstvo',
                            chunk_type='T',
                            related_objects=self.extract_related_objects(item_content),
                            keywords=self.generate_keywords(item_content, item_num),
                            year=year,
                            char_count=len(full_content),
                            hierarchy=hierarchy_list,
                            parent_section=num,
                            parent_title=title
                        )
                        chunks.append(chunk)
                        chunk_index += 1
                else:
                    # Nema bullet stavki - ceo block je jedan chunk
                    # Gradi puni sadržaj sa svim headerima
                    headers_text = ""
                    hierarchy_list = []
                    for hnum, htitle, htype in hierarchy_headers:
                        headers_text += f"{htype} {hnum}. {htitle}\n\n"
                        hierarchy_list.append({'number': hnum, 'title': htitle})
                    
                    full_content = headers_text + block
                    
                    # Parent je direktni roditelj
                    parent_num, parent_title = None, None
                    if hierarchy_headers:
                        parent_num, parent_title, _ = hierarchy_headers[-1]
                    
                    chunk = Chunk(
                        file_num=file_num,
                        chunk_id=self.generate_chunk_id(doc_id, f"tu_sub_{num}", chunk_index),
                        doc_title=doc_title,
                        content=full_content,
                        doc_id=doc_id,
                        doc_type='tehnicko_uputstvo',
                        object_code=None,
                        object_name=None,
                        voltage_levels=self.extract_voltages(block),
                        section_number=num,
                        section_title=title,
                        section_type='tehnicko_uputstvo',
                        chunk_type='T',
                        related_objects=self.extract_related_objects(block),
                        keywords=self.generate_keywords(block, num),
                        year=year,
                        char_count=len(full_content),
                        hierarchy=hierarchy_list,
                        parent_section=parent_num,
                        parent_title=parent_title
                    )
                    chunks.append(chunk)
                    chunk_index += 1
            
            # Obradi ### sekcije koje nemaju ## podsekcije (npr. sekcije 1, 2, 3 koje su kratke)
            processed_parents = set()
            for _, num, _ in sub_headers:
                processed_parents.add(num.split('.')[0])
            
            for ppos, pnum, ptitle in parent_headers:
                if pnum in processed_parents:
                    continue
                
                # Pronađi kraj ove ### sekcije
                next_pos = len(content)
                for npos, nnum, _ in parent_headers:
                    if npos > ppos:
                        next_pos = npos
                        break
                
                section_content = content[ppos:next_pos].strip()
                if not section_content or len(section_content) < self.MIN_CHUNK_SIZE:
                    continue
                
                chunk = Chunk(
                    file_num=file_num,
                    chunk_id=self.generate_chunk_id(doc_id, f"tu_sec_{pnum}", chunk_index),
                    doc_title=doc_title,
                    content=section_content,
                    doc_id=doc_id,
                    doc_type='tehnicko_uputstvo',
                    object_code=None,
                    object_name=None,
                    voltage_levels=self.extract_voltages(section_content),
                    section_number=pnum,
                    section_title=ptitle,
                    section_type='tehnicko_uputstvo',
                    chunk_type='T',
                    related_objects=self.extract_related_objects(section_content),
                    keywords=self.generate_keywords(section_content, pnum),
                    year=year,
                    char_count=len(section_content),
                    hierarchy=[],
                    parent_section=None,
                    parent_title=None
                )
                chunks.append(chunk)
                chunk_index += 1
        
        else:
            # Nema ### - proveri da li ima ## X.Y.Z podsekcije
            # Svaki chunk treba da ima SVE headere iznad sebe u hijerarhiji
            
            # Sakupi SVE ## headere sa njihovim pozicijama - podržava i headere bez naslova
            all_headers: List[Tuple[int, str, str]] = []  # (pos, num, title)
            for m in re.finditer(r'^[\t ]*##\s*(\d+(?:\.\d+)*\.?)\s*(.*)$', content, flags=re.MULTILINE):
                num = m.group(1).rstrip('.')
                title = m.group(2).strip()
                # Ako "naslov" počinje malim slovom, to je sadržaj - tretiraj kao header bez naslova
                if title and not title[0].isupper():
                    title = ""
                all_headers.append((m.start(), num, title))
            
            if not all_headers:
                return chunks
            
            # Sortiraj po poziciji
            all_headers.sort(key=lambda x: x[0])
            
            def _get_hierarchy_headers(target_num: str, target_pos: int) -> List[Tuple[str, str]]:
                """Pronađi sve headere iznad target_num u hijerarhiji."""
                hierarchy = []
                parts = target_num.split('.')
                
                # Za 6.5.1, tražimo 6 i 6.5
                for i in range(1, len(parts)):
                    prefix = '.'.join(parts[:i])
                    # Pronađi header sa ovim brojem koji je PRE target_pos
                    for hpos, hnum, htitle in all_headers:
                        if hpos >= target_pos:
                            break
                        if hnum == prefix:
                            hierarchy.append((hnum, htitle))
                            break
                
                return hierarchy
            
            # Deli po najnižim podsekcijama (## X.Y.Z ili ## X.Y ako nema Z)
            # Pronađi koji je najdublji nivo
            max_depth = max(len(h[1].split('.')) for h in all_headers)
            
            # Pronađi headere koji imaju child headere (ne treba da budu zasebni chunkovi)
            parents_with_children = set()
            for _, num, _ in all_headers:
                parts = num.split('.')
                for i in range(1, len(parts)):
                    parent = '.'.join(parts[:i])
                    parents_with_children.add(parent)
            
            chunk_index = 0
            for i, (pos, num, title) in enumerate(all_headers):
                depth = len(num.split('.'))
                
                # Preskoči headere koji imaju child headere (oni nisu leaf chunkovi)
                if num in parents_with_children:
                    continue
                
                # Pronađi kraj ovog headera (do sledećeg headera bilo kog nivoa)
                end_pos = len(content)
                for j in range(i + 1, len(all_headers)):
                    next_pos, next_num, _ = all_headers[j]
                    # Zaustavi na bilo kom sledećem headeru
                    end_pos = next_pos
                    break
                
                block = content[pos:end_pos].strip()
                if not block or len(block) < self.MIN_CHUNK_SIZE:
                    continue
                
                # Pronađi sve headere iznad u hijerarhiji
                hierarchy_headers = _get_hierarchy_headers(num, pos)
                
                # Proveri da li ima bullet stavke (- X.Y.Z) unutar bloka
                # Podržavamo DVA scenarija:
                # 1. Potomci: ## 6.2 ima potomke - 6.2.1, - 6.2.2 (startswith num + '.')
                # 2. Sestre: ## 4.1.2 ima sestre - 4.1.3, - 4.1.4 (isti parent, veći broj)
                all_bullet_items = re.findall(r'^-\s*(\d+(?:\.\d+)+\.?)\s+(.+?)(?=\n-\s*\d+(?:\.\d+)+\.?\s+|\n##|\n###|\Z)', 
                                         block, re.MULTILINE | re.DOTALL)
                header_depth = len(num.split('.'))
                header_parts = num.split('.')
                
                # Scenario 1: Potomci (npr. 6.2 -> 6.2.1, 6.2.2)
                bullet_items = [(item_num, item_content) for item_num, item_content in all_bullet_items 
                               if item_num.rstrip('.').startswith(num + '.') and 
                                  len(item_num.rstrip('.').split('.')) == header_depth + 1]
                
                # Scenario 2: Sestre (npr. 4.1.2 -> 4.1.3, 4.1.4 itd.)
                # Ako nema potomaka, proveri da li ima sestre na istom nivou
                if not bullet_items and header_depth >= 2:
                    parent_prefix = '.'.join(header_parts[:-1]) + '.'  # npr. "4.1."
                    current_last = int(header_parts[-1])  # npr. 2 za "4.1.2"
                    sibling_items = []
                    for item_num, item_content in all_bullet_items:
                        item_clean = item_num.rstrip('.')
                        item_parts = item_clean.split('.')
                        # Proveri da li je ista dubina i isti parent
                        if len(item_parts) == header_depth and item_clean.startswith(parent_prefix):
                            try:
                                item_last = int(item_parts[-1])
                                # Sestre imaju veći poslednji broj od header-a
                                if item_last > current_last:
                                    sibling_items.append((item_num, item_content))
                            except ValueError:
                                pass
                    bullet_items = sibling_items
                
                if bullet_items:
                    # PRVO: Kreiraj chunk za sadržaj pre prve bullet stavke (ako postoji)
                    # Dinamički konstruiši regex za prvi bullet match
                    if bullet_items:
                        first_item_num = bullet_items[0][0].rstrip('.')
                        first_bullet_match = re.search(r'^-\s*' + re.escape(first_item_num) + r'\.?\s+', block, re.MULTILINE)
                    else:
                        first_bullet_match = None
                    if first_bullet_match and first_bullet_match.start() > 0:
                        pre_bullet_content = block[:first_bullet_match.start()].strip()
                        # Proveri da li ima dovoljno sadržaja (ne samo header)
                        # Izvuci sadržaj posle ## X.Y.Z. linije
                        header_end = pre_bullet_content.find('\n')
                        if header_end > 0:
                            actual_content = pre_bullet_content[header_end:].strip()
                            if len(actual_content) >= 30:
                                # Gradi headers text sa svim headerima iznad
                                headers_text = ""
                                hierarchy_list = []
                                for hnum, htitle in hierarchy_headers:
                                    headers_text += f"## {hnum}. {htitle}\n\n"
                                    hierarchy_list.append({'number': hnum, 'title': htitle})
                                
                                full_content = headers_text + pre_bullet_content
                                
                                chunk = Chunk(
                                    file_num=file_num,
                                    chunk_id=self.generate_chunk_id(doc_id, f"tu_sub_{num}", chunk_index),
                                    doc_title=doc_title,
                                    content=full_content,
                                    doc_id=doc_id,
                                    doc_type='tehnicko_uputstvo',
                                    object_code=None,
                                    object_name=None,
                                    voltage_levels=self.extract_voltages(actual_content),
                                    section_number=num,
                                    section_title=title if title else f"Sekcija {num}",
                                    section_type='tehnicko_uputstvo',
                                    chunk_type='T',
                                    related_objects=self.extract_related_objects(actual_content),
                                    keywords=self.generate_keywords(actual_content, num),
                                    year=year,
                                    char_count=len(full_content),
                                    hierarchy=hierarchy_list,
                                    parent_section=hierarchy_headers[-1][0] if hierarchy_headers else None,
                                    parent_title=hierarchy_headers[-1][1] if hierarchy_headers else None
                                )
                                chunks.append(chunk)
                                chunk_index += 1
                    
                    # ZATIM: Obradi svaku bullet stavku kao poseban chunk
                    for item_num, item_content in bullet_items:
                        item_num = item_num.rstrip('.')
                        item_content = item_content.strip()
                        if len(item_content) < 30:
                            continue
                        
                        # Gradi headers text sa svim headerima iznad + trenutni ## header
                        headers_text = ""
                        hierarchy_list = []
                        for hnum, htitle in hierarchy_headers:
                            headers_text += f"## {hnum}. {htitle}\n\n"
                            hierarchy_list.append({'number': hnum, 'title': htitle})
                        
                        # Dodaj trenutni ## header
                        headers_text += f"## {num}. {title}\n\n"
                        hierarchy_list.append({'number': num, 'title': title})
                        
                        full_content = headers_text + f"- {item_num}. {item_content}"
                        
                        chunk = Chunk(
                            file_num=file_num,
                            chunk_id=self.generate_chunk_id(doc_id, f"tu_item_{item_num}", chunk_index),
                            doc_title=doc_title,
                            content=full_content,
                            doc_id=doc_id,
                            doc_type='tehnicko_uputstvo',
                            object_code=None,
                            object_name=None,
                            voltage_levels=self.extract_voltages(item_content),
                            section_number=item_num,
                            section_title=title,
                            section_type='tehnicko_uputstvo',
                            chunk_type='T',
                            related_objects=self.extract_related_objects(item_content),
                            keywords=self.generate_keywords(item_content, item_num),
                            year=year,
                            char_count=len(full_content),
                            hierarchy=hierarchy_list,
                            parent_section=num,
                            parent_title=title
                        )
                        chunks.append(chunk)
                        chunk_index += 1
                else:
                    # Nema bullet stavki - ceo block je jedan chunk
                    # Gradi puni sadržaj sa svim headerima
                    headers_text = ""
                    hierarchy_list = []
                    for hnum, htitle in hierarchy_headers:
                        headers_text += f"## {hnum}. {htitle}\n\n"
                        hierarchy_list.append({'number': hnum, 'title': htitle})
                    
                    full_content = headers_text + block
                    
                    # Parent je direktni roditelj (npr. za 6.5.1 parent je 6.5)
                    parent_num, parent_title = None, None
                    if hierarchy_headers:
                        parent_num, parent_title = hierarchy_headers[-1]
                    
                    chunk = Chunk(
                        file_num=file_num,
                        chunk_id=self.generate_chunk_id(doc_id, f"tu_sub_{num}", chunk_index),
                        doc_title=doc_title,
                        content=full_content,
                        doc_id=doc_id,
                        doc_type='tehnicko_uputstvo',
                        object_code=None,
                        object_name=None,
                        voltage_levels=self.extract_voltages(block),
                        section_number=num,
                        section_title=title,
                        section_type='tehnicko_uputstvo',
                        chunk_type='T',
                        related_objects=self.extract_related_objects(block),
                        keywords=self.generate_keywords(block, num),
                        year=year,
                        char_count=len(full_content),
                        hierarchy=hierarchy_list,
                        parent_section=parent_num,
                        parent_title=parent_title
                    )
                    chunks.append(chunk)
                    chunk_index += 1
        
        # Post-processing: Augmentuj content chunk-ova sa tipičnim formulacijama pitanja
        for chunk in chunks:
            text_lower = cyrillic_to_latin(chunk.content).lower()
            augmented = self.augment_content(chunk.content, chunk.section_number, text_lower)
            if augmented != chunk.content:
                chunk.content = augmented
                chunk.char_count = len(augmented)
        
        return chunks
    
    def chunk_pravila(self, content: str, doc_id: str, doc_title: str, year: int) -> List[Chunk]:
        """
        Chunk-uje pravila dokumente po svim nivoima:
        - ## X. Glavno poglavlje
        - ### X.Y. Podpoglavlje  
        - #### X.Y.Z. ili #### X.Y.Z.D. Tačke
        
        Svaki #### chunk sadrži sve parent naslove.
        """
        chunks = []
        file_num = self.extract_file_num(doc_title)
        
        # Regex za detekciju svih nivoa naslova
        # ## X. - Glavno poglavlje
        # ### X.Y. - Podpoglavlje
        # #### X.Y.Z. ili X.Y.Z.D. - Tačke (najniži nivo koji postaje chunk)
        
        chapter_pattern = re.compile(r'^##\s+(\d+)\.\s+(.+?)(?=\n|$)', re.MULTILINE)
        section_pattern = re.compile(r'^###\s+(\d+\.\d+)\.?\s+(.+?)(?=\n|$)', re.MULTILINE)
        point_pattern = re.compile(r'^####\s+(\d+\.\d+\.\d+\.?\d*)\.?\s+(.+?)(?=\n####|\n###|\n##|\Z)', re.MULTILINE | re.DOTALL)
        
        # Pronađi sve glavne poglavlje (## X.)
        chapters = {}
        for match in chapter_pattern.finditer(content):
            num = match.group(1)
            title = match.group(2).strip()
            chapters[num] = {'title': title, 'pos': match.start()}
        
        # Pronađi sva podpoglavlja (### X.Y.)
        sections = {}
        for match in section_pattern.finditer(content):
            num = match.group(1)
            title = match.group(2).strip()
            sections[num] = {'title': title, 'pos': match.start()}
        
        def get_chapter_for_point(point_num: str) -> Tuple[Optional[str], Optional[str]]:
            """Vraća (broj, naslov) poglavlja za datu tačku."""
            parts = point_num.split('.')
            if len(parts) >= 1:
                chapter_num = parts[0]
                if chapter_num in chapters:
                    return chapter_num, chapters[chapter_num]['title']
            return None, None
        
        def get_section_for_point(point_num: str) -> Tuple[Optional[str], Optional[str]]:
            """Vraća (broj, naslov) podpoglavlja za datu tačku."""
            parts = point_num.split('.')
            if len(parts) >= 2:
                section_num = f"{parts[0]}.{parts[1]}"
                if section_num in sections:
                    return section_num, sections[section_num]['title']
            return None, None
        
        def get_parent_point(point_num: str) -> Tuple[Optional[str], Optional[str]]:
            """Za X.Y.Z.D vraća X.Y.Z ako postoji."""
            parts = point_num.rstrip('.').split('.')
            if len(parts) == 4:  # X.Y.Z.D
                parent_num = f"{parts[0]}.{parts[1]}.{parts[2]}"
                # Traži parent point u content
                parent_pattern = re.compile(rf'^####\s+{re.escape(parent_num)}\.?\s+(.+?)(?=\n|$)', re.MULTILINE)
                parent_match = parent_pattern.search(content)
                if parent_match:
                    return parent_num, parent_match.group(1).strip()
            return None, None
        
        # Pronađi sve tačke (#### X.Y.Z. ili X.Y.Z.D.)
        chunk_idx = 0
        for match in point_pattern.finditer(content):
            point_num = match.group(1).rstrip('.')
            point_content = match.group(0).strip()
            
            # Preskoči ako je prekratko
            if len(point_content) < self.MIN_CHUNK_SIZE:
                continue
            
            # Izgradi hijerarhiju naslova
            hierarchy_headers = []
            
            # Dodaj glavno poglavlje ## X.
            chapter_num, chapter_title = get_chapter_for_point(point_num)
            if chapter_num and chapter_title:
                hierarchy_headers.append(f"## {chapter_num}. {chapter_title}")
            
            # Dodaj podpoglavlje ### X.Y.
            section_num, section_title = get_section_for_point(point_num)
            if section_num and section_title:
                hierarchy_headers.append(f"### {section_num}. {section_title}")
            
            # Za X.Y.Z.D dodaj i parent #### X.Y.Z.
            parent_num, parent_title = get_parent_point(point_num)
            if parent_num and parent_title:
                # Skrati parent_title ako je predugačak
                short_title = parent_title[:100] + '...' if len(parent_title) > 100 else parent_title
                hierarchy_headers.append(f"#### {parent_num}. {short_title}")
            
            # Sastavi finalni content sa hijerarhijom
            if hierarchy_headers:
                final_content = '\n\n'.join(hierarchy_headers) + '\n\n' + point_content
            else:
                final_content = point_content
            
            # Izvuci naslov tačke (prva linija posle broja)
            first_line = point_content.split('\n')[0]
            title_match = re.match(rf'^####\s+{re.escape(point_num)}\.?\s*(.+)', first_line)
            point_title = title_match.group(1).strip() if title_match else ''
            
            # Odredi section_type
            parts = point_num.split('.')
            if len(parts) == 4:
                section_type = 'tacka_4nivoa'
            else:
                section_type = 'tacka_3nivoa'
            
            chunk = Chunk(
                file_num=file_num,
                chunk_id=self.generate_chunk_id(doc_id, f"pravila_{point_num}", chunk_idx),
                doc_title=doc_title,
                content=final_content,
                doc_id=doc_id,
                doc_type='pravila',
                object_code=None,
                object_name=None,
                voltage_levels=self.extract_voltages(point_content),
                section_number=point_num,
                section_title=point_title[:100],
                section_type=section_type,
                chunk_type='P',
                related_objects=self.extract_related_objects(point_content),
                keywords=self.generate_keywords(point_content, point_num),
                year=year,
                char_count=len(final_content),
                hierarchy=[{'number': h.split()[1].rstrip('.'), 'title': ' '.join(h.split()[2:])} for h in hierarchy_headers],
                parent_section=section_num,
                parent_title=section_title
            )
            chunks.append(chunk)
            chunk_idx += 1
        
        return chunks
    
    def process_file(self, filepath: str) -> List[Chunk]:
        """Procesira jedan fajl i vraća chunk-ove."""
        filename = os.path.basename(filepath)
        doc_type = self.detect_document_type(filename)
        doc_id = filename.replace(' ', '_').replace('.txt', '')
        year = self.extract_year(filename) or 2023
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if doc_type == 'recnik':
            return self.chunk_recnik(content, doc_id, filename)
        elif doc_type == 'uputstvo_pogon':
            object_code = self.extract_object_code(filename) or 'UNKNOWN'
            return self.chunk_uputstvo_pogon(content, doc_id, filename, object_code, year)
        elif doc_type == 'tehnicko_uputstvo':
            return self.chunk_tehnicko_uputstvo(content, doc_id, filename, year)
        elif doc_type == 'pravila':
            return self.chunk_pravila(content, doc_id, filename, year)
        else:
            # Generički chunking
            return self._chunk_generic(content, doc_id, filename, year)
    
    def _chunk_generic(self, content: str, doc_id: str, doc_title: str, year: int) -> List[Chunk]:
        """Generičko chunking po paragrafima."""
        chunks = []
        file_num = self.extract_file_num(doc_title)
        paragraphs = content.split('\n\n')
        
        current_chunk = []
        current_size = 0
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            
            if current_size + len(para) > self.MAX_CHUNK_SIZE and current_chunk:
                chunk_content = '\n\n'.join(current_chunk)
                chunk = Chunk(
                    file_num=file_num,
                    chunk_id=self.generate_chunk_id(doc_id, f"para_{len(chunks)}"),
                    doc_title=doc_title,
                    content=chunk_content,
                    doc_id=doc_id,
                    doc_type='generic',
                    object_code=None,
                    object_name=None,
                    voltage_levels=self.extract_voltages(chunk_content),
                    section_number=str(len(chunks) + 1),
                    section_title='',
                    section_type='generic',
                    chunk_type='G',
                    related_objects=self.extract_related_objects(chunk_content),
                    keywords=self.generate_keywords(chunk_content),
                    year=year,
                    char_count=len(chunk_content),
                    hierarchy=[],
                    parent_section=None,
                    parent_title=None
                )
                chunks.append(chunk)
                current_chunk = []
                current_size = 0
            
            current_chunk.append(para)
            current_size += len(para)
        
        # Poslednji chunk
        if current_chunk:
            chunk_content = '\n\n'.join(current_chunk)
            chunk = Chunk(
                file_num=file_num,
                chunk_id=self.generate_chunk_id(doc_id, f"para_{len(chunks)}"),
                doc_title=doc_title,
                content=chunk_content,
                doc_id=doc_id,
                doc_type='generic',
                object_code=None,
                object_name=None,
                voltage_levels=self.extract_voltages(chunk_content),
                section_number=str(len(chunks) + 1),
                section_title='',
                section_type='generic',
                chunk_type='G',
                related_objects=self.extract_related_objects(chunk_content),
                keywords=self.generate_keywords(chunk_content),
                year=year,
                char_count=len(chunk_content),
                hierarchy=[],
                parent_section=None,
                parent_title=None
            )
            chunks.append(chunk)
        
        return chunks
    
    def process_directory(self, input_dir: str, output_path: str):
        """Procesira sve fajlove u direktorijumu."""
        all_chunks = []
        files = sorted(Path(input_dir).glob('*.txt'))
        
        print(f"\n{'='*60}")
        print(f"CHUNKER V3 - Deljenje po ## podsekcijama")
        print(f"{'='*60}\n")
        
        for filepath in files:
            print(f"Procesiranje: {filepath.name}")
            chunks = self.process_file(str(filepath))
            all_chunks.extend(chunks)
            print(f"  -> {len(chunks)} chunk-ova")
        
        # Sačuvaj chunk-ove (konvertuj u latinicu)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            for chunk in all_chunks:
                latin_chunk = chunk.to_latin()
                f.write(json.dumps(latin_chunk.to_dict(), ensure_ascii=False) + '\n')
        
        # Statistike
        print(f"\n{'='*60}")
        print(f"ZAVRŠENO")
        print(f"{'='*60}")
        print(f"  Ukupno fajlova: {len(files)}")
        print(f"  Ukupno chunk-ova: {len(all_chunks)}")
        print(f"  Prosečna veličina: {sum(c.char_count for c in all_chunks) / len(all_chunks):.0f} karaktera")
        print(f"  Izlaz: {output_path}")
        
        return all_chunks


def main():
    """Glavna funkcija."""
    base_dir = Path(__file__).parent.parent
    
    config_path = base_dir / 'config' / 'chunking_config.json'
    input_dir = base_dir.parent / 'files'
    output_path = base_dir / 'output' / 'all_chunks.jsonl'
    
    chunker = EESChunkerV3(str(config_path))
    chunker.process_directory(str(input_dir), str(output_path))


if __name__ == '__main__':
    main()
