"""
GridKnowledgeGraph - Glavni Knowledge Graph za elektroenergetsku opremu.

Implementacija prema: Metodologija Relejne zaštite - GridMind 15-02.md

Koristi NetworkX za reprezentaciju grafa.
"""

import logging
from typing import Dict, List, Optional, Set, Tuple, Any, Iterator
from dataclasses import asdict
from collections import defaultdict

import networkx as nx

from .schema.node_types import (
    NODE_TYPES, 
    VOLTAGE_LEVELS,
    FIELD_TYPES,
    BOUNDARY_ELEMENTS,
    EEONode,
    BusbarNode, 
    FieldNode,
    ElementNode,
    TransformerNode,
    LineNode,
)
from .schema.edge_types import (
    EDGE_TYPES,
    DVP_CHAIN_NO_PSS,
    DVP_CHAIN_WITH_PSS,
    TRP_CHAIN,
    GSP_CHAIN,
    ConnectivityMatrixEntry,
)
from .schema.enums import SwitchStatus, FieldType, VoltageLevel

logger = logging.getLogger(__name__)


class GridKnowledgeGraph:
    """
    Knowledge Graph za modelovanje elektroenergetske opreme PS.
    
    Struktura:
    - Čvorovi: EEO, GSS, PSS, DVP, KBP, TR, P, SR, IRSU, SMT, NMT, DV, KB
    - Ivice: GALVANSKI_VEZAN, SADRZI, PRIPADA, POVEZUJE
    
    Graf kombinuje:
    - Hijerarhijsku strukturu (EEO -> Polje -> Element)
    - Topološku strukturu (galvanske veze između elemenata)
    - Međuobjektne veze (DV/KB koji povezuju EEO)
    """
    
    def __init__(self):
        """Inicijalizacija praznog grafa."""
        # NetworkX MultiGraph - podržava višestruke ivice između čvorova
        self._graph = nx.MultiGraph()
        
        # Indeksi za brži pristup
        self._eeo_index: Dict[str, EEONode] = {}           # eeo_id -> EEONode
        self._nodes_by_type: Dict[str, Set[str]] = defaultdict(set)  # type -> set(node_ids)
        self._nodes_by_eeo: Dict[str, Set[str]] = defaultdict(set)   # eeo_id -> set(node_ids)
        
        # Matrica povezanosti
        self._connectivity_matrix: List[ConnectivityMatrixEntry] = []
        
        logger.info("[KG] GridKnowledgeGraph initialized")
    
    # =========================================================================
    # DODAVANJE ČVOROVA
    # =========================================================================
    
    def add_eeo(
        self,
        id: str,
        name: str,
        code: str,
        type: str,
        voltage_levels: List[int],
        **kwargs
    ) -> str:
        """
        Dodaje EEO (Elektroenergetski objekat) u graf.
        
        Args:
            id: Jedinstveni identifikator (npr. "NI2")
            name: Puno ime (npr. "TS 400/220/110 kV Niš 2")
            code: Skraćeni kod (npr. "NI2")
            type: Tip objekta ("TS", "RP", "PRP")
            voltage_levels: Lista naponskih nivoa [400, 220, 110]
        
        Returns:
            ID dodatog čvora
        """
        node = EEONode(
            id=id,
            name=name,
            code=code,
            type=type,
            voltage_levels=voltage_levels,
            **kwargs
        )
        
        self._graph.add_node(id, **asdict(node), node_type="EEO")
        self._eeo_index[id] = node
        self._nodes_by_type["EEO"].add(id)
        
        logger.debug(f"[KG] Added EEO: {id} ({name})")
        return id
    
    def add_busbar(
        self,
        eeo_id: str,
        type: str,  # "GSS" ili "PSS"
        voltage_kv: int,
        index: int,
    ) -> str:
        """
        Dodaje sistem sabirnica (GSS/PSS) u graf.
        
        Args:
            eeo_id: ID pripadajućeg EEO
            type: "GSS" ili "PSS"
            voltage_kv: Naponski nivo (400, 220, 110)
            index: Redni broj sabirnice
        
        Returns:
            ID dodatog čvora (format: "{eeo_id}_{type}_{voltage}_{index}")
        """
        node_id = f"{eeo_id}_{type}_{voltage_kv}_{index}"
        
        node = BusbarNode(
            id=node_id,
            eeo_id=eeo_id,
            type=type,
            voltage_kv=voltage_kv,
            index=index,
        )
        
        self._graph.add_node(node_id, **asdict(node), node_type=type)
        self._nodes_by_type[type].add(node_id)
        self._nodes_by_eeo[eeo_id].add(node_id)
        
        # Dodaj SADRZI ivicu: EEO -> Busbar
        self._graph.add_edge(eeo_id, node_id, edge_type="SADRZI")
        
        logger.debug(f"[KG] Added {type}: {node_id}")
        return node_id
    
    def add_field(
        self,
        eeo_id: str,
        type: str,  # "DVP", "KBP", "TRPVN", "TRPNN", "GSP", "PSP"
        voltage_kv: int,
        index: int,
        line_name: Optional[str] = None,
        transformer_id: Optional[str] = None,
        connects_busbars: Optional[List[str]] = None,
        gss_index: Optional[int] = None,
    ) -> str:
        """
        Dodaje polje (DVP, KBP, TRPVN, TRPNN, GSP, PSP) u graf.
        
        Returns:
            ID dodatog čvora (format: "{eeo_id}_{type}_{voltage}_{index}")
        """
        node_id = f"{eeo_id}_{type}_{voltage_kv}_{index}"
        
        node = FieldNode(
            id=node_id,
            eeo_id=eeo_id,
            type=type,
            voltage_kv=voltage_kv,
            index=index,
            line_name=line_name,
            gss_index=gss_index,
            transformer_id=transformer_id,
            connects_busbars=connects_busbars or [],
        )
        
        self._graph.add_node(node_id, **asdict(node), node_type=type)
        self._nodes_by_type[type].add(node_id)
        self._nodes_by_eeo[eeo_id].add(node_id)
        
        # Dodaj SADRZI ivicu: EEO -> Field
        self._graph.add_edge(eeo_id, node_id, edge_type="SADRZI")
        
        logger.debug(f"[KG] Added {type}: {node_id}")
        return node_id
    
    def add_element(
        self,
        field_id: str,
        type: str,  # "P", "SR", "IRSU", "SMT", "NMT"
        connected_busbar: Optional[str] = None,
        connected_busbar_id: Optional[str] = None,
        status: Optional[int] = 1,  # 1=uključen, 0=isključen
    ) -> str:
        """
        Dodaje osnovni element (P, SR, IRSU, SMT, NMT) u graf.
        
        Args:
            field_id: ID pripadajućeg polja
            type: Tip elementa
            connected_busbar: Za SR - oznaka sabirnice ("GSS_1", "PSS_1")
            status: Status uklopnog stanja (samo za RO)
        
        Returns:
            ID dodatog čvora
        """
        # Izvuci informacije iz field_id
        parts = field_id.split("_")
        eeo_id = parts[0]
        voltage_kv = int(parts[2])
        
        # Generiši ID elementa
        if type == "SR" and connected_busbar:
            node_id = f"{field_id}_{type}_{connected_busbar}"
        else:
            node_id = f"{field_id}_{type}"
        
        # Odredi da li je granični element
        is_boundary = type in BOUNDARY_ELEMENTS
        
        # Odredi da li ima status (samo RO)
        has_status = NODE_TYPES.get(type, {}).get("has_status", False)
        
        node = ElementNode(
            id=node_id,
            eeo_id=eeo_id,
            field_id=field_id,
            type=type,
            voltage_kv=voltage_kv,
            connected_busbar=connected_busbar,
            connected_busbar_id=connected_busbar_id,
            status=status if has_status else None,
            is_boundary=is_boundary,
        )
        
        self._graph.add_node(node_id, **asdict(node), node_type=type)
        self._nodes_by_type[type].add(node_id)
        self._nodes_by_eeo[eeo_id].add(node_id)
        
        # Dodaj SADRZI ivicu: Field -> Element
        self._graph.add_edge(field_id, node_id, edge_type="SADRZI")
        
        logger.debug(f"[KG] Added {type}: {node_id}")
        return node_id
    
    def add_transformer(
        self,
        eeo_id: str,
        name: str,
        vn_kv: int,
        nn_kv: int,
        index: int,
        power_mva: Optional[float] = None,
    ) -> str:
        """
        Dodaje energetski transformator u graf.
        
        Returns:
            ID dodatog čvora (format: "{eeo_id}_TR_{index}")
        """
        node_id = f"{eeo_id}_TR_{index}"
        
        node = TransformerNode(
            id=node_id,
            eeo_id=eeo_id,
            name=name,
            vn_kv=vn_kv,
            nn_kv=nn_kv,
            index=index,
            power_mva=power_mva,
        )
        
        self._graph.add_node(node_id, **asdict(node), node_type="TR")
        self._nodes_by_type["TR"].add(node_id)
        self._nodes_by_eeo[eeo_id].add(node_id)
        
        # Dodaj SADRZI ivicu: EEO -> TR
        self._graph.add_edge(eeo_id, node_id, edge_type="SADRZI")
        
        logger.debug(f"[KG] Added TR: {node_id}")
        return node_id
    
    def add_line(
        self,
        type: str,  # "DV", "KB", "MV"
        name: str,
        voltage_kv: int,
        from_eeo_id: str,
        from_field_id: str,
        from_field_index: int,
        to_eeo_id: str,
        to_field_id: str,
        to_field_index: int,
        length_km: Optional[float] = None,
        mv_type: Optional[str] = None,
    ) -> str:
        """
        Dodaje vod (DV, KB, MV) u graf.
        
        Returns:
            ID dodatog čvora (format: "{type}_{from_eeo}_{to_eeo}_{voltage}")
        """
        node_id = f"{type}_{from_eeo_id}_{to_eeo_id}_{voltage_kv}"
        
        node = LineNode(
            id=node_id,
            type=type,
            name=name,
            voltage_kv=voltage_kv,
            from_eeo_id=from_eeo_id,
            from_field_id=from_field_id,
            from_field_index=from_field_index,
            to_eeo_id=to_eeo_id,
            to_field_id=to_field_id,
            to_field_index=to_field_index,
            length_km=length_km,
            mv_type=mv_type,
        )
        
        self._graph.add_node(node_id, **asdict(node), node_type=type)
        self._nodes_by_type[type].add(node_id)
        
        # Dodaj u matricu povezanosti
        entry = ConnectivityMatrixEntry(
            eeo_x_id=from_eeo_id,
            dvp_x_index=from_field_index,
            eeo_y_id=to_eeo_id,
            dvp_y_index=to_field_index,
            voltage_kv=voltage_kv,
            line_type=type,
            line_id=node_id,
        )
        self._connectivity_matrix.append(entry)
        
        logger.debug(f"[KG] Added {type}: {node_id}")
        return node_id
    
    # =========================================================================
    # DODAVANJE IVICA
    # =========================================================================
    
    def add_galvanska_veza(
        self,
        source_id: str,
        target_id: str,
        condition: Optional[str] = None,
    ) -> None:
        """
        Dodaje galvansku vezu između dva elementa.
        
        Ovo je osnovna veza iz metodologije:
        "prethodnik <-> osnovni element <-> sledbenik"
        """
        self._graph.add_edge(
            source_id, 
            target_id, 
            edge_type="GALVANSKI_VEZAN",
            condition=condition,
        )
        logger.debug(f"[KG] Added GALVANSKI_VEZAN: {source_id} <-> {target_id}")
    
    def add_povezuje(
        self,
        element_id: str,
        line_id: str,
        side: str,  # "from" ili "to"
    ) -> None:
        """
        Dodaje vezu između graničnog elementa i voda.
        
        IRSU (EEO1) --POVEZUJE--> DV --POVEZUJE--> IRSU (EEO2)
        """
        self._graph.add_edge(
            element_id,
            line_id,
            edge_type="POVEZUJE",
            side=side,
        )
        logger.debug(f"[KG] Added POVEZUJE: {element_id} -- {line_id} ({side})")
    
    # =========================================================================
    # KREIRANJE KOMPLETNOG POLJA SA ELEMENTIMA
    # =========================================================================
    
    def create_dvp_with_elements(
        self,
        eeo_id: str,
        voltage_kv: int,
        index: int,
        line_name: str,
        gss_index: int = 1,
        pss_index: Optional[int] = None,
        all_status: int = 1,
    ) -> Dict[str, str]:
        """
        Kreira kompletno dalekovodno polje sa svim elementima i vezama.
        
        Lanac veza (bez PSS):
        GSS <-> SR <-> P <-> SMT <-> IRSU <-> (NMT, KRAJ)
        
        Args:
            eeo_id: ID EEO
            voltage_kv: Naponski nivo
            index: Redni broj polja
            line_name: Ime dalekovoda
            gss_index: Indeks GSS na koju se povezuje
            pss_index: Indeks PSS (ako postoji)
            all_status: Default status svih RO (1=uključen)
        
        Returns:
            Dict sa ID-jevima kreiranih elemenata
        """
        # 1. Kreiraj polje
        field_id = self.add_field(
            eeo_id=eeo_id,
            type="DVP",
            voltage_kv=voltage_kv,
            index=index,
            line_name=line_name,
            gss_index=gss_index,
        )
        
        result = {"field_id": field_id}
        
        # 2. Kreiraj elemente
        gss_id = f"{eeo_id}_GSS_{voltage_kv}_{gss_index}"
        
        # SR ka GSS
        sr_gss_id = self.add_element(
            field_id=field_id,
            type="SR",
            connected_busbar=f"GSS_{gss_index}",
            connected_busbar_id=gss_id,
            status=all_status,
        )
        result["sr_gss"] = sr_gss_id
        
        # Prekidač
        p_id = self.add_element(field_id=field_id, type="P", status=all_status)
        result["p"] = p_id
        
        # SMT
        smt_id = self.add_element(field_id=field_id, type="SMT")
        result["smt"] = smt_id
        
        # IRSU
        irsu_id = self.add_element(field_id=field_id, type="IRSU", status=all_status)
        result["irsu"] = irsu_id
        
        # NMT
        nmt_id = self.add_element(field_id=field_id, type="NMT")
        result["nmt"] = nmt_id
        
        # 3. Kreiraj galvanske veze (lanac)
        # GSS <-> SR
        self.add_galvanska_veza(gss_id, sr_gss_id)
        # SR <-> P
        self.add_galvanska_veza(sr_gss_id, p_id)
        # P <-> SMT
        self.add_galvanska_veza(p_id, smt_id)
        # SMT <-> IRSU
        self.add_galvanska_veza(smt_id, irsu_id)
        # IRSU <-> NMT
        self.add_galvanska_veza(irsu_id, nmt_id)
        
        # Ako ima PSS, dodaj SR ka PSS
        if pss_index is not None:
            pss_id = f"{eeo_id}_PSS_{voltage_kv}_{pss_index}"
            sr_pss_id = self.add_element(
                field_id=field_id,
                type="SR",
                connected_busbar=f"PSS_{pss_index}",
                connected_busbar_id=pss_id,
                status=all_status,
            )
            result["sr_pss"] = sr_pss_id
            # IRSU <-> SR_PSS <-> PSS
            self.add_galvanska_veza(irsu_id, sr_pss_id)
            self.add_galvanska_veza(sr_pss_id, pss_id)
        
        logger.info(f"[KG] Created DVP with elements: {field_id}")
        return result
    
    def create_trpvn_with_elements(
        self,
        eeo_id: str,
        voltage_kv: int,
        index: int,
        line_name: str,
        gss_index: int = 1,
        tr_node_id: Optional[str] = None,
        all_status: int = 1,
    ) -> Dict[str, str]:
        """
        Kreira transformatorsko polje višeg napona (TRPVN) sa elementima.
        
        Lanac veza (bez PSS, iz metodologije):
        GSS <-> SR <-> P <-> SMT <-> {TR, OP}
        OP <-> UEEO
        """
        field_id = self.add_field(
            eeo_id=eeo_id,
            type="TRPVN",
            voltage_kv=voltage_kv,
            index=index,
            line_name=line_name,
            gss_index=gss_index,
            transformer_id=tr_node_id,
        )
        
        result = {"field_id": field_id}
        
        # SR ka GSS
        gss_id = f"{eeo_id}_GSS_{voltage_kv}_{gss_index}"
        sr_gss_id = self.add_element(
            field_id=field_id, type="SR",
            connected_busbar=f"GSS_{gss_index}",
            connected_busbar_id=gss_id,
            status=all_status,
        )
        result["sr_gss"] = sr_gss_id
        
        # P (prekidač)
        p_id = self.add_element(field_id=field_id, type="P", status=all_status)
        result["p"] = p_id
        
        # SMT
        smt_id = self.add_element(field_id=field_id, type="SMT")
        result["smt"] = smt_id
        
        # OP (uzemljivač / zaštitna oprema)
        op_id = self.add_element(field_id=field_id, type="OP", status=all_status)
        result["op"] = op_id
        
        # Galvanske veze - lanac
        self.add_galvanska_veza(gss_id, sr_gss_id)    # GSS <-> SR
        self.add_galvanska_veza(sr_gss_id, p_id)       # SR <-> P
        self.add_galvanska_veza(p_id, smt_id)           # P <-> SMT
        self.add_galvanska_veza(smt_id, op_id)          # SMT <-> OP
        
        # Veze sa TR (ako je poznat)
        if tr_node_id and self.get_node(tr_node_id):
            self.add_galvanska_veza(smt_id, tr_node_id)  # SMT <-> TR
            self.add_galvanska_veza(op_id, tr_node_id)    # OP <-> TR
        
        # OP <-> UEEO
        ueeo_id = f"{eeo_id}_UEEO"
        if self.get_node(ueeo_id):
            self.add_galvanska_veza(op_id, ueeo_id)
        
        logger.info(f"[KG] Created TRPVN with elements: {field_id}")
        return result
    
    def create_trpnn_with_elements(
        self,
        eeo_id: str,
        voltage_kv: int,
        index: int,
        line_name: str,
        gss_index: int = 1,
        tr_node_id: Optional[str] = None,
        all_status: int = 1,
    ) -> Dict[str, str]:
        """
        Kreira transformatorsko polje nižeg napona (TRPNN) sa elementima.
        
        Lanac veza (bez PSS, iz metodologije):
        GSS <-> SR <-> P <-> SMT <-> {NMT, OP, TR}
        NMT <-> {OP, TR, UEEO}
        OP <-> UEEO
        """
        field_id = self.add_field(
            eeo_id=eeo_id,
            type="TRPNN",
            voltage_kv=voltage_kv,
            index=index,
            line_name=line_name,
            gss_index=gss_index,
            transformer_id=tr_node_id,
        )
        
        result = {"field_id": field_id}
        
        # SR ka GSS
        gss_id = f"{eeo_id}_GSS_{voltage_kv}_{gss_index}"
        sr_gss_id = self.add_element(
            field_id=field_id, type="SR",
            connected_busbar=f"GSS_{gss_index}",
            connected_busbar_id=gss_id,
            status=all_status,
        )
        result["sr_gss"] = sr_gss_id
        
        # P
        p_id = self.add_element(field_id=field_id, type="P", status=all_status)
        result["p"] = p_id
        
        # SMT
        smt_id = self.add_element(field_id=field_id, type="SMT")
        result["smt"] = smt_id
        
        # NMT
        nmt_id = self.add_element(field_id=field_id, type="NMT")
        result["nmt"] = nmt_id
        
        # OP
        op_id = self.add_element(field_id=field_id, type="OP", status=all_status)
        result["op"] = op_id
        
        # Galvanske veze - lanac
        self.add_galvanska_veza(gss_id, sr_gss_id)    # GSS <-> SR
        self.add_galvanska_veza(sr_gss_id, p_id)       # SR <-> P
        self.add_galvanska_veza(p_id, smt_id)           # P <-> SMT
        self.add_galvanska_veza(smt_id, nmt_id)         # SMT <-> NMT
        self.add_galvanska_veza(smt_id, op_id)          # SMT <-> OP
        self.add_galvanska_veza(nmt_id, op_id)          # NMT <-> OP
        
        # Veze sa TR (ako je poznat)
        if tr_node_id and self.get_node(tr_node_id):
            self.add_galvanska_veza(smt_id, tr_node_id)  # SMT <-> TR
            self.add_galvanska_veza(nmt_id, tr_node_id)   # NMT <-> TR
            self.add_galvanska_veza(op_id, tr_node_id)    # OP <-> TR
        
        # NMT/OP <-> UEEO
        ueeo_id = f"{eeo_id}_UEEO"
        if self.get_node(ueeo_id):
            self.add_galvanska_veza(nmt_id, ueeo_id)
            self.add_galvanska_veza(op_id, ueeo_id)
        
        logger.info(f"[KG] Created TRPNN with elements: {field_id}")
        return result
    
    def create_gsp_with_elements(
        self,
        eeo_id: str,
        voltage_kv: int,
        index: int = 1,
        gss_from_index: int = 1,
        gss_to_index: int = 2,
        all_status: int = 1,
    ) -> Dict[str, str]:
        """
        Kreira glavno spojno polje (GSP) sa elementima.
        
        Lanac veza (iz metodologije):
        GSS_i <-> SR_1 <-> P <-> SMT <-> SR_2 <-> GSS_(i+1)
        """
        field_id = self.add_field(
            eeo_id=eeo_id,
            type="GSP",
            voltage_kv=voltage_kv,
            index=index,
            line_name=f"SP {voltage_kv}kV",
            gss_index=gss_from_index,
            connects_busbars=[f"GSS_{gss_from_index}", f"GSS_{gss_to_index}"],
        )
        
        result = {"field_id": field_id}
        
        # SR ka GSS 1
        gss_from_id = f"{eeo_id}_GSS_{voltage_kv}_{gss_from_index}"
        sr_from_id = self.add_element(
            field_id=field_id, type="SR",
            connected_busbar=f"GSS_{gss_from_index}",
            connected_busbar_id=gss_from_id,
            status=all_status,
        )
        result["sr_from"] = sr_from_id
        
        # P
        p_id = self.add_element(field_id=field_id, type="P", status=all_status)
        result["p"] = p_id
        
        # SMT
        smt_id = self.add_element(field_id=field_id, type="SMT")
        result["smt"] = smt_id
        
        # SR ka GSS 2
        gss_to_id = f"{eeo_id}_GSS_{voltage_kv}_{gss_to_index}"
        sr_to_id = self.add_element(
            field_id=field_id, type="SR",
            connected_busbar=f"GSS_{gss_to_index}",
            connected_busbar_id=gss_to_id,
            status=all_status,
        )
        result["sr_to"] = sr_to_id
        
        # Galvanske veze - lanac
        self.add_galvanska_veza(gss_from_id, sr_from_id)  # GSS_1 <-> SR_1
        self.add_galvanska_veza(sr_from_id, p_id)          # SR_1 <-> P
        self.add_galvanska_veza(p_id, smt_id)              # P <-> SMT
        self.add_galvanska_veza(smt_id, sr_to_id)          # SMT <-> SR_2
        self.add_galvanska_veza(sr_to_id, gss_to_id)       # SR_2 <-> GSS_2
        
        logger.info(f"[KG] Created GSP with elements: {field_id}")
        return result
    
    # =========================================================================
    # UPITI NAD GRAFOM
    # =========================================================================
    
    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        """Vraća atribute čvora."""
        if node_id in self._graph:
            return dict(self._graph.nodes[node_id])
        return None
    
    def get_nodes_by_type(self, node_type: str) -> List[str]:
        """Vraća listu ID-jeva čvorova datog tipa."""
        return list(self._nodes_by_type.get(node_type, set()))
    
    def get_nodes_by_eeo(self, eeo_id: str) -> List[str]:
        """Vraća listu ID-jeva čvorova koji pripadaju datom EEO."""
        return list(self._nodes_by_eeo.get(eeo_id, set()))
    
    def get_neighbors(self, node_id: str, edge_type: Optional[str] = None) -> List[str]:
        """
        Vraća susede čvora.
        
        Args:
            node_id: ID čvora
            edge_type: Ako je zadat, filtrira samo ivice tog tipa
        """
        if node_id not in self._graph:
            return []
        
        neighbors = []
        for neighbor in self._graph.neighbors(node_id):
            if edge_type is None:
                neighbors.append(neighbor)
            else:
                # Proveri tip ivice
                edge_data = self._graph.get_edge_data(node_id, neighbor)
                for key, data in edge_data.items():
                    if data.get("edge_type") == edge_type:
                        neighbors.append(neighbor)
                        break
        
        return neighbors
    
    def get_galvanski_povezani(self, node_id: str) -> List[str]:
        """Vraća čvorove galvanski povezane sa datim čvorom."""
        return self.get_neighbors(node_id, edge_type="GALVANSKI_VEZAN")
    
    def get_boundary_elements(self, eeo_id: str) -> List[str]:
        """Vraća granične elemente (IRSU, SMT, NMT) za dati EEO."""
        boundary = []
        for node_id in self._nodes_by_eeo.get(eeo_id, set()):
            node = self.get_node(node_id)
            if node and node.get("is_boundary"):
                boundary.append(node_id)
        return boundary
    
    def get_connectivity_matrix(
        self, 
        voltage_kv: Optional[int] = None,
        line_type: Optional[str] = None,
    ) -> List[ConnectivityMatrixEntry]:
        """
        Vraća matricu povezanosti.
        
        Args:
            voltage_kv: Filtrira po naponskom nivou
            line_type: Filtrira po tipu voda (DV, KB, MV)
        """
        result = self._connectivity_matrix
        
        if voltage_kv is not None:
            result = [e for e in result if e.voltage_kv == voltage_kv]
        
        if line_type is not None:
            result = [e for e in result if e.line_type == line_type]
        
        return result
    
    # =========================================================================
    # ANALIZA NAPAJANJA
    # =========================================================================
    
    def find_path(
        self,
        source_id: str,
        target_id: str,
        respect_status: bool = True,
    ) -> Optional[List[str]]:
        """
        Pronalazi putanju između dva čvora.
        
        Args:
            source_id: Početni čvor
            target_id: Krajnji čvor
            respect_status: Ako True, ne prolazi kroz isključene RO
        
        Returns:
            Lista ID-jeva čvorova na putanji ili None ako nema puta
        """
        if not respect_status:
            try:
                return nx.shortest_path(self._graph, source_id, target_id)
            except nx.NetworkXNoPath:
                return None
        
        # Sa poštovanjem statusa - BFS sa filterom
        from collections import deque
        
        visited = set()
        queue = deque([(source_id, [source_id])])
        
        while queue:
            current, path = queue.popleft()
            
            if current == target_id:
                return path
            
            if current in visited:
                continue
            visited.add(current)
            
            for neighbor in self._graph.neighbors(current):
                if neighbor in visited:
                    continue
                
                # Proveri status (ako je RO)
                node = self.get_node(neighbor)
                if node and node.get("status") == 0:  # Isključen
                    continue
                
                queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def is_energized(self, node_id: str, source_nodes: Set[str]) -> bool:
        """
        Proverava da li je čvor napajan iz bilo kog izvora.
        
        Args:
            node_id: ID čvora za proveru
            source_nodes: Skup čvorova koji su izvori napajanja
        """
        for source in source_nodes:
            if self.find_path(source, node_id, respect_status=True):
                return True
        return False
    
    # =========================================================================
    # STATISTIKE
    # =========================================================================
    
    def get_stats(self) -> Dict[str, Any]:
        """Vraća statistike grafa."""
        stats = {
            "total_nodes": self._graph.number_of_nodes(),
            "total_edges": self._graph.number_of_edges(),
            "nodes_by_type": {t: len(ids) for t, ids in self._nodes_by_type.items()},
            "eeo_count": len(self._eeo_index),
            "connectivity_matrix_entries": len(self._connectivity_matrix),
        }
        return stats
    
    def __repr__(self) -> str:
        stats = self.get_stats()
        return (
            f"GridKnowledgeGraph("
            f"nodes={stats['total_nodes']}, "
            f"edges={stats['total_edges']}, "
            f"eeo={stats['eeo_count']})"
        )
