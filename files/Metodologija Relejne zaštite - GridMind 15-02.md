






















# Skraćenice
DS – distributivni sistem;
DV - dalekovod;
DVP - dalekovodno polje;
EEO - elektroenergetski objekat;
EES - elektroenergetski sistem;
ET – energetski transformator;
GSP - spojno polje;
GSS - glavni sistem sabirnica;
IR - izlazni rastavljač;
IRSU – izlazni rastavljač sa sistemskim uzemljenjem;
KB - kabal;
KBP - kablovsko polje;
KDS – korisnik distributivnog sistema;
KPS – korisnik prenosnog sistema;
MO – merna oprema;
MV - mešoviti vod;
NMT – naponski merni transformator;
OP – odvodnik prenapona;
OPGW – akronim od engleskog naziva Optical Power Ground Wire. U srpskom jeziku koristi se kao optički zemljovodni provodnik (ređe se upotrebljava) ili zemljovodno uže (češće se upotrebljava);
P - prekidač;
PO – polje;
PS – prenosni sistem;
PSP – pomoćno spojno polje;
PSS - pomoćni sistem sabirnica;
RO – rasklopna oprema;
RP - razvodno postrojenje;
SMT – strujni merni transformator;
SR – sabirnički rastavljač;
SS - sistem sabirnica;
TR - transformator;
TRP - transformatorsko polje;
TRPNN – transformatorsko polje na nižem naponu;
TRPVN – transformatorsko polje na višem naponu;
UEEO – uzemljenje EEO
VO – vod;
ZO – zaštitna oprema;

# Struktura PS
EES Republike Srbije se sastoji od:
PS,
DS,
KPS,
KDS.
Električna energija se kroz PS prenosi na 400 kV, 220 kV i 110 kV naponskom nivou. Električna energija se kroz DS prenosi na 35 kV, 20 kV, 10 kV i 0.4 kV naponskom nivou. Naponi u DS nisu od važnosti za upravljanje prenosnim sistemom, pa se označavaju sa x kV. EES Republike Srbije je trofazni EES. Trofazni EES se sastoji od tri faze koje se označavaju sa:
Faza L1 (ravnopravno se koristi i oznaka - faza "0"),
Faza L2 (ravnopravno se koristi i oznaka - faza "4"),
Faza L3 (ravnopravno se koristi i oznaka - faza "8").
## Podela elektroenergetske opreme PS
Naredno objašnjenje podele elektroenergetske opreme PS nije definisano kroz stručnu literaturu. Rezultat je razumevanja funkcionisanja PS od strane autora ovog teksta i uprošćava objašnjenje od čega se PS sastoji. Podela po tipu odgovara strukturi stabla sa nejednakim grananjem. Podela je napisana kroz nivoe. Grana stabla za koju nije definisano novo grananje kroz naredni nivo podele predstavlja list. Listovi stabla predstavljaju osnovne elemente.
Osnovna podela elektroenergetske opreme PS je na elektroenergetsku opremu koja pripada EEO in a elektroenergetsku opremu koja ne pripada EEO.
### Elektroenergetska oprema PS koja pripada EEO
Elektroenergetska oprema PS koja pripada EEO označava opremu koja se po mestu ugradnje, odnosno fizički nalazi unutar EEO.
Nivo 1
Nivo 1 podele Elektroenergetska oprema PS koja pripada EEO:
PO,
ET,
SS,
UEEO.
Nivo 2
Nivo 2 podele PO:
DVP,
KBP,
TRPVN,
TRPNN,
GSP,
PSP.
Nivo 2 podele ET:
TR 400/220 kV/kV,
TR 400/110 kV/kV,
TR 220/110 kV/kV,
TR 400/x kV/kV,
TR 220/x kV/kV,
TR 110/x kV/kV.
Nivo 2 podele SS:
GSS sa pripadajućom opremom,
PSS.
Nivo 3
Nivo 3 podele DVP:
DVP 400 kV,
DVP 220 kV,
DVP 110 kV,
DVP x kV.
Nivo 3 podele KBP:
KBP 400 kV,
KBP 220 kV,
KBP 110 kV,
KBP x kV.
Nivo 3 podele TRPVN:
TRPVN TR 400/220 kV/kV,
TRPVN TR 400/110 kV/kV,
TRPVN TR 220/110 kV/kV,
TRPVN TR 400/x kV/kV,
TRPVN TR 220/x kV/kV,
TRPVN TR 110/x kV/kV.
Nivo 3 podele TRPNN:
TRPNN TR 400/220 kV/kV,
TRPNN TR 400/110 kV/kV,
TRPNN TR 220/110 kV/kV,
TRPNN TR 400/x kV/kV,
TRPNN TR 220/x kV/kV,
TRPNN TR 110/x kV/kV.
Nivo 3 podele GSP:
GSP 400 kV,
GSP 220 kV,
GSP 110 kV,
GSP x kV.
Nivo 3 podele PSP:
PSP 400 kV,
PSP 220 kV,
PSP 110 kV,
PSP x kV.
Nivo 3 podele TR 400/220 kV/kV:
TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TR 400/220 kV/kV} za n_TR 400/220 kV/kV>0, i∈{0} za n_TR 400/220 kV/kV=0; n_TR 400/220 kV/kV∈N0.
Nivo 3 podele TR 400/110 kV/kV:
TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TR 400/110 kV/kV} za n_TR 400/110 kV/kV>0, i∈{0} za n_TR 400/110 kV/kV=0; n_TR 400/110 kV/kV∈N0.
Nivo 3 podele TR 220/110 kV/kV:
TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TR 220/110 kV/kV} za n_TR 220/110 kV/kV>0, i∈{0} za n_TR 220/110 kV/kV=0; n_TR 220/110 kV/kV∈N0.
Nivo 3 podele TR 400/x kV/kV:
TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TR 400/x kV/kV} za n_TR 400/x kV/kV>0, i∈{0} za n_TR 400/x kV/kV=0; n_TR 400/x kV/kV∈N0.
Nivo 3 podele TR 220/x kV/kV:
TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TR 220/x kV/kV} za n_TR 220/x kV/kV>0, i∈{0} za n_TR 220/x kV/kV=0; n_TR 220/x kV/kV∈N0.
Nivo 3 podele TR 110/x kV/kV:
TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TR 110/x kV/kV} za n_TR 110/x kV/kV>0, i∈{0} za n_TR 110/x kV/kV=0; n_TR 110/x kV/kV∈N0.
Nivo 3 podele GSS sa pripadajućom opremom:
GSS sa pripadajućom opremom 400 kV,
GSS sa pripadajućom opremom 220 kV,
GSS sa pripadajućom opremom 110 kV,
GSS sa pripadajućom opremom x kV.
Nivo 3 podele PSS:
PSS 400 kV,
PSS 220 kV,
PSS 110 kV,
PSS x kV.
Nivo 4
Nivo 4 podele DVP 400 kV:
DVP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 400 kV} za n_DVP 400 kV>0, i∈{0} za n_DVP 400 kV=0; n_DVP 400 kV∈N0.
Nivo 4 podele DVP 220 kV:
DVP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 220 kV} za n_DVP 220 kV>0, i∈{0} za n_DVP 220 kV=0; n_DVP 220 kV∈N0.
Nivo 4 podele DVP 110 kV:
DVP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 110 kV} za n_DVP 110 kV>0, i∈{0} za n_DVP 110 kV=0; n_DVP 110 kV∈N0.
Nivo 4 podele DVP x kV:
DVP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP x kV} za n_DVP x kV>0, i∈{0} za n_DVP x kV=0; n_DVP x kV∈N0.
Nivo 4 podele KBP 400 kV:
KBP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 400 kV} za n_KBP 400 kV>0, i∈{0} za n_KBP 400 kV=0; n_KBP 400 kV∈N0.
Nivo 4 podele KBP 220 kV:
KBP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 220 kV} za n_KBP 220 kV>0, i∈{0} za n_KBP 220 kV=0; n_KBP 220 kV∈N0.
Nivo 4 podele KBP 110 kV:
KBP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 110 kV} za n_KBP 110 kV>0, i∈{0} za n_KBP 110 kV=0; n_KBP 110 kV∈N0.
Nivo 4 podele KBP x kV:
KBP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP x kV} za n_KBP x kV>0, i∈{0} za n_KBP x kV=0; n_KBP x kV∈N0.
Nivo 4 podele TRPVN TR 400/220 kV/kV:
TRPVN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/220 kV/kV} za n_TRPVN TR 400/220 kV/kV>0, i∈{0} za n_TRPVN TR 400/220 kV/kV=0; n_TRPVN TR 400/220 kV/kV∈N0.
Nivo 4 podele TRPVN TR 400/110 kV/kV:
TRPVN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/110 kV/kV} za n_TRPVN TR 400/110 kV/kV>0, i∈{0} za n_TRPVN TR 400/110 kV/kV=0; n_TRPVN TR 400/110 kV/kV∈N0.
Nivo 4 podele TRPVN TR 220/110 kV/kV:
TRPVN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/110 kV/kV} za n_TRPVN TR 220/110 kV/kV>0, i∈{0} za n_TRPVN TR 220/110 kV/kV=0; n_TRPVN TR 220/110 kV/kV∈N0.
Nivo 4 podele TRPVN TR 400/x kV/kV:
TRPVN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/x kV/kV} za n_TRPVN TR 400/x kV/kV>0, i∈{0} za n_TRPVN TR 400/x kV/kV=0; n_TRPVN TR 400/x kV/kV∈N0.
Nivo 4 podele TRPVN TR 220/x kV/kV:
TRPVN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/x kV/kV} za n_TRPVN TR 220/x kV/kV>0, i∈{0} za n_TRPVN TR 220/x kV/kV=0; n_TRPVN TR 220/x kV/kV∈N0.
Nivo 4 podele TRPVN TR 110/x kV/kV:
TRPVN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 110/x kV/kV} za n_TRPVN TR 110/x kV/kV>0, i∈{0} za n_TRPVN TR 110/x kV/kV=0; n_TRPVN TR 110/x kV/kV∈N0.
Nivo 4 podele TRPNN TR 400/220 kV/kV:
TRPNN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/220 kV/kV} za n_TRPNN TR 400/220 kV/kV>0, i∈{0} za n_TRPNN TR 400/220 kV/kV=0; n_TRPNN TR 400/220 kV/kV∈N0.
Nivo 4 podele TRPNN TR 400/110 kV/kV:
TRPNN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/110 kV/kV} za n_TRPNN TR 400/110 kV/kV>0, i∈{0} za n_TRPNN TR 400/110 kV/kV=0; n_TRPNN TR 400/110 kV/kV∈N0.
Nivo 4 podele TRPNN TR 220/110 kV/kV:
TRPNN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/110 kV/kV} za n_TRPNN TR 220/110 kV/kV>0, i∈{0} za n_TRPNN TR 220/110 kV/kV=0; n_TRPNN TR 220/110 kV/kV∈N0.
Nivo 4 podele TRPNN TR 400/x kV/kV:
TRPNN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/x kV/kV} za n_TRPNN TR 400/x kV/kV>0, i∈{0} za n_TRPNN TR 400/x kV/kV=0; n_TRPNN TR 400/x kV/kV∈N0.
Nivo 4 podele TRPNN TR 220/x kV/kV:
TRPNN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/x kV/kV} za n_TRPNN TR 220/x kV/kV>0, i∈{0} za n_TRPNN TR 220/x kV/kV=0; n_TRPNN TR 220/x kV/kV∈N0.
Nivo 4 podele TRPNN TR 110/x kV/kV:
TRPNN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 110/x kV/kV} za n_TRPNN TR 110/x kV/kV>0, i∈{0} za n_TRPNN TR 110/x kV/kV=0; n_TRPNN TR 110/x kV/kV∈N0.
Nivo 4 podele GSP 400 kV:
GSP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 400 kV} za n_GSP 400 kV>0, i∈{0} za n_GSP 400 kV=0; n_GSP 400 kV∈N0.
Nivo 4 podele GSP 220 kV:
GSP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 220 kV} za n_GSP 220 kV>0, i∈{0} za n_GSP 220 kV=0; n_GSP 220 kV∈N0.
Nivo 4 podele GSP 110 kV:
GSP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 110 kV} za n_GSP 110 kV>0, i∈{0} za n_GSP 110 kV=0; n_GSP 110 kV∈N0.
Nivo 4 podele GSP x kV:
GSP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP x kV} za n_GSP x kV>0, i∈{0} za n_GSP x kV=0; n_GSP x kV∈N0.
Nivo 4 podele PSP 400 kV:
PSP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 400 kV} za n_PSP 400 kV>0, i∈{0} za n_PSP 400 kV=0; n_PSP 400 kV∈N0.
Nivo 4 podele PSP 220 kV:
PSP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 220 kV} za n_PSP 220 kV>0, i∈{0} za n_PSP 220 kV=0; n_PSP 220 kV∈N0.
Nivo 4 podele PSP 110 kV:
PSP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 110 kV} za n_PSP 110 kV>0, i∈{0} za n_PSP 110 kV=0; n_PSP 110 kV∈N0.
Nivo 4 podele PSP x kV:
PSP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP x kV} za n_PSP x kV>0, i∈{0} za n_PSP x kV=0; n_PSP x kV∈N0.
Nivo 4 podele GSS sa pripadajućom opremom 400 kV:
GSS sa pripadajućom opremom 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, i∈{0} za n_GSS 400 kV=0; n_GSS 400 kV∈N0.
Nivo 4 podele GSS sa pripadajućom opremom 220 kV:
GSS sa pripadajućom opremom 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, i∈{0} za n_GSS 220 kV=0; n_GSS 220 kV∈N0.
Nivo 4 podele GSS sa pripadajućom opremom 110 kV:
GSS sa pripadajućom opremom 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, i∈{0} za n_GSS 110 kV=0; n_GSS 110 kV∈N0.
Nivo 4 podele GSS sa pripadajućom opremom x kV:
GSS sa pripadajućom opremom x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS x kV} za n_GSS x kV>0, i∈{0} za n_GSS x kV=0; n_GSS x kV∈N0.
Nivo 4 podele PSS 400 kV:
PSS 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSS 400 kV} za n_PSS 400 kV>0, i∈{0} za n_PSS 400 kV=0; n_PSS 400 kV∈N0.
Nivo 4 podele PSS 220 kV:
PSS 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSS 220 kV} za n_PSS 220 kV>0, i∈{0} za n_PSS 220 kV=0; n_PSS 220 kV∈N0.
Nivo 4 podele PSS 110 kV:
PSS 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSS 110 kV} za n_PSS 110 kV>0, i∈{0} za n_PSS 110 kV=0; n_PSS 110 kV∈N0.
Nivo 4 podele PSS x kV:
PSS x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSS x kV} za n_PSS x kV>0, i∈{0} za n_PSS x kV=0; n_PSS x kV∈N0.
Nivo 5
Nivo 5 podele DVP 400 kV i:
RO DVP 400 kV i,
MO DVP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 400 kV} za n_DVP 400 kV>0, i∈{0} za n_DVP 400 kV=0; n_DVP 400 kV∈N0.
Nivo 5 podele DVP 220 kV i:
RO DVP 220 kV i,
MO DVP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 220 kV} za n_DVP 220 kV>0, i∈{0} za n_DVP 220 kV=0; n_DVP 220 kV∈N0.
Nivo 5 podele DVP 110 kV i:
RO DVP 110 kV i,
MO DVP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 110 kV} za n_DVP 110 kV>0, i∈{0} za n_DVP 110 kV=0; n_DVP 110 kV∈N0.
Nivo 5 podele DVP x kV i:
RO DVP x kV i,
MO DVP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP x kV} za n_DVP x kV>0, i∈{0} za n_DVP x kV=0; n_DVP x kV∈N0.
Nivo 5 podele KBP 400 kV i:
RO KBP 400 kV i,
MO KBP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 400 kV} za n_KBP 400 kV>0, i∈{0} za n_KBP 400 kV=0; n_KBP 400 kV∈N0.
Nivo 5 podele KBP 220 kV i:
RO KBP 220 kV i,
MO KBP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 220 kV} za n_KBP 220 kV>0, i∈{0} za n_KBP 220 kV=0; n_KBP 220 kV∈N0.
Nivo 5 podele KBP 110 kV i:
RO KBP 110 kV i,
MO KBP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 110 kV} za n_KBP 110 kV>0, i∈{0} za n_KBP 110 kV=0; n_KBP 110 kV∈N0.
Nivo 5 podele KBP x kV i:
RO KBP x kV i,
MO KBP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP x kV} za n_KBP x kV>0, i∈{0} za n_KBP x kV=0; n_KBP x kV∈N0.
Nivo 5 podele TRPVN TR 400/220 kV/kV i:
RO TRPVN TR 400/220 kV/kV i,
MO TRPVN TR 400/220 kV/kV i,
ZO TRPVN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/220 kV/kV} za n_TRPVN TR 400/220 kV/kV>0, i∈{0} za n_TRPVN TR 400/220 kV/kV=0; n_TRPVN TR 400/220 kV/kV∈N0.
Nivo 5 podele TRPVN TR 400/110 kV/kV i:
RO TRPVN TR 400/110 kV/kV i,
MO TRPVN TR 400/110 kV/kV i,
ZO TRPVN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/110 kV/kV} za n_TRPVN TR 400/110 kV/kV>0, i∈{0} za n_TRPVN TR 400/110 kV/kV=0; n_TRPVN TR 400/110 kV/kV∈N0.
Nivo 5 podele TRPVN TR 220/110 kV/kV i:
RO TRPVN TR 220/110 kV/kV i,
MO TRPVN TR 220/110 kV/kV i,
ZO TRPVN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/110 kV/kV} za n_TRPVN TR 220/110 kV/kV>0, i∈{0} za n_TRPVN TR 220/110 kV/kV=0; n_TRPVN TR 220/110 kV/kV∈N0.
Nivo 5 podele TRPVN TR 400/x kV/kV i:
RO TRPVN TR 400/x kV/kV i,
MO TRPVN TR 400/x kV/kV i,
ZO TRPVN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/x kV/kV} za n_TRPVN TR 400/x kV/kV>0, i∈{0} za n_TRPVN TR 400/x kV/kV=0; n_TRPVN TR 400/x kV/kV∈N0.
Nivo 5 podele TRPVN TR 220/x kV/kV i:
RO TRPVN TR 220/x kV/kV i,
MO TRPVN TR 220/x kV/kV i,
ZO TRPVN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/x kV/kV} za n_TRPVN TR 220/x kV/kV>0, i∈{0} za n_TRPVN TR 220/x kV/kV=0; n_TRPVN TR 220/x kV/kV∈N0.
Nivo 5 podele TRPVN TR 110/x kV/kV i:
RO TRPVN TR 110/x kV/kV i,
MO TRPVN TR 110/x kV/kV i,
ZO TRPVN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 110/x kV/kV} za n_TRPVN TR 110/x kV/kV>0, i∈{0} za n_TRPVN TR 110/x kV/kV=0; n_TRPVN TR 110/x kV/kV∈N0.
Nivo 5 podele TRPNN TR 400/220 kV/kV i:
RO TRPNN TR 400/220 kV/kV i,
MO TRPNN TR 400/220 kV/kV i,
ZO TRPNN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/220 kV/kV} za n_TRPNN TR 400/220 kV/kV>0, i∈{0} za n_TRPNN TR 400/220 kV/kV=0; n_TRPNN TR 400/220 kV/kV∈N0.
Nivo 5 podele TRPNN TR 400/110 kV/kV i:
RO TRPNN TR 400/110 kV/kV i,
MO TRPNN TR 400/110 kV/kV i,
ZO TRPNN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/110 kV/kV} za n_TRPNN TR 400/110 kV/kV>0, i∈{0} za n_TRPNN TR 400/110 kV/kV=0; n_TRPNN TR 400/110 kV/kV∈N0.
Nivo 5 podele TRPNN TR 220/110 kV/kV i:
RO TRPNN TR 220/110 kV/kV i,
MO TRPNN TR 220/110 kV/kV i,
ZO TRPNN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/110 kV/kV} za n_TRPNN TR 220/110 kV/kV>0, i∈{0} za n_TRPNN TR 220/110 kV/kV=0; n_TRPNN TR 220/110 kV/kV∈N0.
Nivo 5 podele TRPNN TR 400/x kV/kV i:
RO TRPNN TR 400/x kV/kV i,
MO TRPNN TR 400/x kV/kV i,
ZO TRPNN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/x kV/kV} za n_TRPNN TR 400/x kV/kV>0, i∈{0} za n_TRPNN TR 400/x kV/kV=0; n_TRPNN TR 400/x kV/kV∈N0.
Nivo 5 podele TRPNN TR 220/x kV/kV i:
RO TRPNN TR 220/x kV/kV i,
MO TRPNN TR 220/x kV/kV i,
ZO TRPNN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/x kV/kV} za n_TRPNN TR 220/x kV/kV>0, i∈{0} za n_TRPNN TR 220/x kV/kV=0; n_TRPNN TR 220/x kV/kV∈N0.
Nivo 5 podele TRPNN TR 110/x kV/kV i:
RO TRPNN TR 110/x kV/kV i,
MO TRPNN TR 110/x kV/kV i,
ZO TRPNN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 110/x kV/kV} za n_TRPNN TR 110/x kV/kV>0, i∈{0} za n_TRPNN TR 110/x kV/kV=0; n_TRPNN TR 110/x kV/kV∈N0.
Nivo 5 podele GSP 400 kV i:
RO GSP 400 kV i,
MO GSP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 400 kV} za n_GSP 400 kV>0, i∈{0} za n_GSP 400 kV=0; n_GSP 400 kV∈N0.
Nivo 5 podele GSP 220 kV i:
RO GSP 220 kV i,
MO GSP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 220 kV} za n_GSP 220 kV>0, i∈{0} za n_GSP 220 kV=0; n_GSP 220 kV∈N0.
Nivo 5 podele GSP 110 kV i:
RO GSP 110 kV i,
MO GSP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 110 kV} za n_GSP 110 kV>0, i∈{0} za n_GSP 110 kV=0; n_GSP 110 kV∈N0.
Nivo 5 podele GSP x kV i:
RO GSP x kV i,
MO GSP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP x kV} za n_GSP x kV>0, i∈{0} za n_GSP x kV=0; n_GSP x kV∈N0.
Nivo 5 podele PSP 400 kV i:
RO PSP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 400 kV} za n_PSP 400 kV>0, i∈{0} za n_PSP 400 kV=0; n_PSP 400 kV∈N0.
Nivo 5 podele PSP 220 kV i:
RO PSP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 220 kV} za n_PSP 220 kV>0, i∈{0} za n_PSP 220 kV=0; n_PSP 220 kV∈N0.
Nivo 5 podele PSP 110 kV i:
RO PSP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 110 kV} za n_PSP 110 kV>0, i∈{0} za n_PSP 110 kV=0; n_PSP 110 kV∈N0.
Nivo 5 podele PSP x kV i:
RO PSP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP x kV} za n_PSP x kV>0, i∈{0} za n_PSP x kV=0; n_PSP x kV∈N0.
Nivo 5 podele GSS sa pripadajućom opremom 400 kV i:
GSS 400 kV i,
MO GSS 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, i∈{0} za n_GSS 400 kV=0; n_GSS 400 kV∈N0.
Nivo 5 podele GSS sa pripadajućom opremom 220 kV i:
GSS 220 kV i,
MO GSS 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, i∈{0} za n_GSS 220 kV=0; n_GSS 220 kV∈N0.
Nivo 5 podele GSS sa pripadajućom opremom 110 kV i:
GSS 110 kV i,
MO GSS 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, i∈{0} za n_GSS 110 kV=0; n_GSS 110 kV∈N0.
Nivo 5 podele GSS sa pripadajućom opremom x kV i:
GSS x kV i,
MO GSS x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS x kV} za n_GSS x kV>0, i∈{0} za n_GSS x kV=0; n_GSS x kV∈N0.
Nivo 6
Nivo 6 podele RO DVP 400 kV i:
SR DVP 400 kV i,
P DVP 400 kV i,
IRSU DVP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 400 kV} za n_DVP 400 kV>0, i∈{0} za n_DVP 400 kV=0; n_DVP 400 kV∈N0.
Nivo 6 podele MO DVP 400 kV i:
SMT DVP 400 kV i,
NMT DVP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 400 kV} za n_DVP 400 kV>0, i∈{0} za n_DVP 400 kV=0; n_DVP 400 kV∈N0.
Nivo 6 podele RO DVP 220 kV i:
SR DVP 220 kV i,
P DVP 220 kV i,
IRSU DVP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 220 kV} za n_DVP 220 kV>0, i∈{0} za n_DVP 220 kV=0; n_DVP 220 kV∈N0.
Nivo 6 podele MO DVP 220 kV i:
SMT DVP 220 kV i,
NMT DVP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 220 kV} za n_DVP 220 kV>0, i∈{0} za n_DVP 220 kV=0; n_DVP 220 kV∈N0.
Nivo 6 podele RO DVP 110 kV i:
SR DVP 110 kV i,
P DVP 110 kV i,
IRSU DVP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 110 kV} za n_DVP 110 kV>0, i∈{0} za n_DVP 110 kV=0; n_DVP 110 kV∈N0.
Nivo 6 podele MO DVP 110 kV i:
SMT DVP 110 kV i,
NMT DVP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP 110 kV} za n_DVP 110 kV>0, i∈{0} za n_DVP 110 kV=0; n_DVP 110 kV∈N0.
Nivo 6 podele RO DVP x kV i:
SR DVP x kV i,
P DVP x kV i,
IRSU DVP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP x kV} za n_DVP x kV>0, i∈{0} za n_DVP x kV=0; n_DVP x kV∈N0.
Nivo 6 podele MO DVP x kV i:
SMT DVP x kV i,
NMT DVP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_DVP x kV} za n_DVP x kV>0, i∈{0} za n_DVP x kV=0; n_DVP x kV∈N0.
Nivo 6 podele RO KBP 400 kV i:
SR KBP 400 kV i,
P KBP 400 kV i,
IRSU KBP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 400 kV} za n_KBP 400 kV>0, i∈{0} za n_KBP 400 kV=0; n_KBP 400 kV∈N0.
Nivo 6 podele MO KBP 400 kV i:
SMT KBP 400 kV i,
NMT KBP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 400 kV} za n_KBP 400 kV>0, i∈{0} za n_KBP 400 kV=0; n_KBP 400 kV∈N0.
Nivo 6 podele RO KBP 220 kV i:
SR KBP 220 kV i,
P KBP 220 kV i,
IRSU KBP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 220 kV} za n_KBP 220 kV>0, i∈{0} za n_KBP 220 kV=0; n_KBP 220 kV∈N0.
Nivo 6 podele MO KBP 220 kV i:
SMT KBP 220 kV i,
NMT KBP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 220 kV} za n_KBP 220 kV>0, i∈{0} za n_KBP 220 kV=0; n_KBP 220 kV∈N0.
Nivo 6 podele RO KBP 110 kV i:
SR KBP 110 kV i,
P KBP 110 kV i,
IRSU KBP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 110 kV} za n_KBP 110 kV>0, i∈{0} za n_KBP 110 kV=0; n_KBP 110 kV∈N0.
Nivo 6 podele MO KBP 110 kV i:
SMT KBP 110 kV i,
NMT KBP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP 110 kV} za n_KBP 110 kV>0, i∈{0} za n_KBP 110 kV=0; n_KBP 110 kV∈N0.
Nivo 6 podele RO KBP x kV i:
SR KBP x kV i,
P KBP x kV i,
IRSU KBP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP x kV} za n_KBP x kV>0, i∈{0} za n_KBP x kV=0; n_KBP x kV∈N0.
Nivo 6 podele MO KBP x kV i:
SMT KBP x kV i,
NMT KBP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_KBP x kV} za n_KBP x kV>0, i∈{0} za n_KBP x kV=0; n_KBP x kV∈N0.
Nivo 6 podele RO TRPVN TR 400/220 kV/kV i:
SR TRPVN TR 400/220 kV/kV i,
P TRPVN TR 400/220 kV/kV i,
IR TRPVN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/220 kV/kV} za n_TRPVN TR 400/220 kV/kV>0, i∈{0} za n_TRPVN TR 400/220 kV/kV=0; n_TRPVN TR 400/220 kV/kV∈N0.
Nivo 6 podele MO TRPVN TR 400/220 kV/kV i:
SMT TRPVN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/220 kV/kV} za n_TRPVN TR 400/220 kV/kV>0, i∈{0} za n_TRPVN TR 400/220 kV/kV=0; n_TRPVN TR 400/220 kV/kV∈N0.
Nivo 6 podele ZO TRPVN TR 400/220 kV/kV i:
OP TRPVN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/220 kV/kV} za n_TRPVN TR 400/220 kV/kV>0, i∈{0} za n_TRPVN TR 400/220 kV/kV=0; n_TRPVN TR 400/220 kV/kV∈N0.
Nivo 6 podele RO TRPVN TR 400/110 kV/kV i:
SR TRPVN TR 400/110 kV/kV i,
P TRPVN TR 400/110 kV/kV i,
IR TRPVN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/110 kV/kV} za n_TRPVN TR 400/110 kV/kV>0, i∈{0} za n_TRPVN TR 400/110 kV/kV=0; n_TRPVN TR 400/110 kV/kV∈N0.
Nivo 6 podele MO TRPVN TR 400/110 kV/kV i:
SMT TRPVN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/110 kV/kV} za n_TRPVN TR 400/110 kV/kV>0, i∈{0} za n_TRPVN TR 400/110 kV/kV=0; n_TRPVN TR 400/110 kV/kV∈N0.
Nivo 6 podele ZO TRPVN TR 400/110 kV/kV i:
OP TRPVN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/110 kV/kV} za n_TRPVN TR 400/110 kV/kV>0, i∈{0} za n_TRPVN TR 400/110 kV/kV=0; n_TRPVN TR 400/110 kV/kV∈N0.
Nivo 6 podele RO TRPVN TR 220/110 kV/kV i:
SR TRPVN TR 220/110 kV/kV i,
P TRPVN TR 220/110 kV/kV i,
IR TRPVN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/110 kV/kV} za n_TRPVN TR 220/110 kV/kV>0, i∈{0} za n_TRPVN TR 220/110 kV/kV=0; n_TRPVN TR 220/110 kV/kV∈N0.
Nivo 6 podele MO TRPVN TR 220/110 kV/kV i:
SMT TRPVN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/110 kV/kV} za n_TRPVN TR 220/110 kV/kV>0, i∈{0} za n_TRPVN TR 220/110 kV/kV=0; n_TRPVN TR 220/110 kV/kV∈N0.
Nivo 6 podele ZO TRPVN TR 220/110 kV/kV i:
OP TRPVN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/110 kV/kV} za n_TRPVN TR 220/110 kV/kV>0, i∈{0} za n_TRPVN TR 220/110 kV/kV=0; n_TRPVN TR 220/110 kV/kV∈N0.
Nivo 6 podele RO TRPVN TR 400/x kV/kV i:
SR TRPVN TR 400/x kV/kV i,
P TRPVN TR 400/x kV/kV i,
IR TRPVN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/x kV/kV} za n_TRPVN TR 400/x kV/kV>0, i∈{0} za n_TRPVN TR 400/x kV/kV=0; n_TRPVN TR 400/x kV/kV∈N0.
Nivo 6 podele MO TRPVN TR 400/x kV/kV i:
SMT TRPVN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/x kV/kV} za n_TRPVN TR 400/x kV/kV>0, i∈{0} za n_TRPVN TR 400/x kV/kV=0; n_TRPVN TR 400/x kV/kV∈N0.
Nivo 6 podele ZO TRPVN TR 400/x kV/kV i:
OP TRPVN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 400/x kV/kV} za n_TRPVN TR 400/x kV/kV>0, i∈{0} za n_TRPVN TR 400/x kV/kV=0; n_TRPVN TR 400/x kV/kV∈N0.
Nivo 6 podele RO TRPVN TR 220/x kV/kV i:
SR TRPVN TR 220/x kV/kV i,
P TRPVN TR 220/x kV/kV i,
IR TRPVN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/x kV/kV} za n_TRPVN TR 220/x kV/kV>0, i∈{0} za n_TRPVN TR 220/x kV/kV=0; n_TRPVN TR 220/x kV/kV∈N0.
Nivo 6 podele MO TRPVN TR 220/x kV/kV i:
SMT TRPVN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/x kV/kV} za n_TRPVN TR 220/x kV/kV>0, i∈{0} za n_TRPVN TR 220/x kV/kV=0; n_TRPVN TR 220/x kV/kV∈N0.
Nivo 6 podele ZO TRPVN TR 220/x kV/kV i:
OP TRPVN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 220/x kV/kV} za n_TRPVN TR 220/x kV/kV>0, i∈{0} za n_TRPVN TR 220/x kV/kV=0; n_TRPVN TR 220/x kV/kV∈N0.
Nivo 6 podele RO TRPVN TR 110/x kV/kV i:
SR TRPVN TR 110/x kV/kV i,
P TRPVN TR 110/x kV/kV i,
IR TRPVN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 110/x kV/kV} za n_TRPVN TR 110/x kV/kV>0, i∈{0} za n_TRPVN TR 110/x kV/kV=0; n_TRPVN TR 110/x kV/kV∈N0.
Nivo 6 podele MO TRPVN TR 110/x kV/kV i:
SMT TRPVN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 110/x kV/kV} za n_TRPVN TR 110/x kV/kV>0, i∈{0} za n_TRPVN TR 110/x kV/kV=0; n_TRPVN TR 110/x kV/kV∈N0.
Nivo 6 podele ZO TRPVN TR 110/x kV/kV i:
OP TRPVN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPVN TR 110/x kV/kV} za n_TRPVN TR 110/x kV/kV>0, i∈{0} za n_TRPVN TR 110/x kV/kV=0; n_TRPVN TR 110/x kV/kV∈N0.
Nivo 6 podele RO TRPNN TR 400/220 kV/kV i:
SR TRPNN TR 400/220 kV/kV i,
P TRPNN TR 400/220 kV/kV i,
IR TRPNN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/220 kV/kV} za n_TRPNN TR 400/220 kV/kV>0, i∈{0} za n_TRPNN TR 400/220 kV/kV=0; n_TRPNN TR 400/220 kV/kV∈N0.
Nivo 6 podele MO TRPNN TR 400/220 kV/kV i:
SMT TRPNN TR 400/220 kV/kV i,
NMT TRPNN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/220 kV/kV} za n_TRPNN TR 400/220 kV/kV>0, i∈{0} za n_TRPNN TR 400/220 kV/kV=0; n_TRPNN TR 400/220 kV/kV∈N0.
Nivo 6 podele ZO TRPNN TR 400/220 kV/kV i:
OP TRPNN TR 400/220 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/220 kV/kV} za n_TRPNN TR 400/220 kV/kV>0, i∈{0} za n_TRPNN TR 400/220 kV/kV=0; n_TRPNN TR 400/220 kV/kV∈N0.
Nivo 6 podele RO TRPNN TR 400/110 kV/kV i:
SR TRPNN TR 400/110 kV/kV i,
P TRPNN TR 400/110 kV/kV i,
IR TRPNN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/110 kV/kV} za n_TRPNN TR 400/110 kV/kV>0, i∈{0} za n_TRPNN TR 400/110 kV/kV=0; n_TRPNN TR 400/110 kV/kV∈N0.
Nivo 6 podele MO TRPNN TR 400/110 kV/kV i:
SMT TRPNN TR 400/110 kV/kV i,
NMT TRPNN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/110 kV/kV} za n_TRPNN TR 400/110 kV/kV>0, i∈{0} za n_TRPNN TR 400/110 kV/kV=0; n_TRPNN TR 400/110 kV/kV∈N0.
Nivo 6 podele ZO TRPNN TR 400/110 kV/kV i:
OP TRPNN TR 400/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/110 kV/kV} za n_TRPNN TR 400/110 kV/kV>0, i∈{0} za n_TRPNN TR 400/110 kV/kV=0; n_TRPNN TR 400/110 kV/kV∈N0.
Nivo 6 podele RO TRPNN TR 220/110 kV/kV i:
SR TRPNN TR 220/110 kV/kV i,
P TRPNN TR 220/110 kV/kV i,
IR TRPNN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/110 kV/kV} za n_TRPNN TR 220/110 kV/kV>0, i∈{0} za n_TRPNN TR 220/110 kV/kV=0; n_TRPNN TR 220/110 kV/kV∈N0.
Nivo 6 podele MO TRPNN TR 220/110 kV/kV i:
SMT TRPNN TR 220/110 kV/kV i,
NMT TRPNN TR 220/110 kV/kV i
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/110 kV/kV} za n_TRPNN TR 220/110 kV/kV>0, i∈{0} za n_TRPNN TR 220/110 kV/kV=0; n_TRPNN TR 220/110 kV/kV∈N0.
Nivo 6 podele ZO TRPNN TR 220/110 kV/kV i:
OP TRPNN TR 220/110 kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/110 kV/kV} za n_TRPNN TR 220/110 kV/kV>0, i∈{0} za n_TRPNN TR 220/110 kV/kV=0; n_TRPNN TR 220/110 kV/kV∈N0.
Nivo 6 podele RO TRPNN TR 400/x kV/kV i:
SR TRPNN TR 400/x kV/kV i,
P TRPNN TR 400/x kV/kV i,
IR TRPNN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/x kV/kV} za n_TRPNN TR 400/x kV/kV>0, i∈{0} za n_TRPNN TR 400/x kV/kV=0; n_TRPNN TR 400/x kV/kV∈N0.
Nivo 6 podele MO TRPNN TR 400/x kV/kV i:
SMT TRPNN TR 400/x kV/kV i,
NMT TRPNN TR 400/x kV/kV i
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/x kV/kV} za n_TRPNN TR 400/x kV/kV>0, i∈{0} za n_TRPNN TR 400/x kV/kV=0; n_TRPNN TR 400/x kV/kV∈N0.
Nivo 6 podele ZO TRPNN TR 400/x kV/kV i:
OP TRPNN TR 400/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 400/x kV/kV} za n_TRPNN TR 400/x kV/kV>0, i∈{0} za n_TRPNN TR 400/x kV/kV=0; n_TRPNN TR 400/x kV/kV∈N0.
Nivo 6 podele RO TRPNN TR 220/x kV/kV i:
SR TRPNN TR 220/x kV/kV i,
P TRPNN TR 220/x kV/kV i,
IR TRPNN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/x kV/kV} za n_TRPNN TR 220/x kV/kV>0, i∈{0} za n_TRPNN TR 220/x kV/kV=0; n_TRPNN TR 220/x kV/kV∈N0.
Nivo 6 podele MO TRPNN TR 220/x kV/kV i:
SMT TRPNN TR 220/x kV/kV i,
NMT TRPNN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/x kV/kV} za n_TRPNN TR 220/x kV/kV>0, i∈{0} za n_TRPNN TR 220/x kV/kV=0; n_TRPNN TR 220/x kV/kV∈N0.
Nivo 6 podele ZO TRPNN TR 220/x kV/kV i:
OP TRPNN TR 220/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 220/x kV/kV} za n_TRPNN TR 220/x kV/kV>0, i∈{0} za n_TRPNN TR 220/x kV/kV=0; n_TRPNN TR 220/x kV/kV∈N0.
Nivo 6 podele RO TRPNN TR 110/x kV/kV i:
SR TRPNN TR 110/x kV/kV i,
P TRPNN TR 110/x kV/kV i,
IR TRPNN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 110/x kV/kV} za n_TRPNN TR 110/x kV/kV>0, i∈{0} za n_TRPNN TR 110/x kV/kV=0; n_TRPNN TR 110/x kV/kV∈N0.
Nivo 6 podele MO TRPNN TR 110/x kV/kV i:
SMT TRPNN TR 110/x kV/kV i,
NMT TRPNN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 110/x kV/kV} za n_TRPNN TR 110/x kV/kV>0, i∈{0} za n_TRPNN TR 110/x kV/kV=0; n_TRPNN TR 110/x kV/kV∈N0.
Nivo 6 podele ZO TRPNN TR 110/x kV/kV i:
OP TRPNN TR 110/x kV/kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_TRPNN TR 110/x kV/kV} za n_TRPNN TR 110/x kV/kV>0, i∈{0} za n_TRPNN TR 110/x kV/kV=0; n_TRPNN TR 110/x kV/kV∈N0.
Nivo 6 podele RO GSP 400 kV i:
SR GSP 400 kV i,
P GSP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 400 kV} za n_GSP 400 kV>0, i∈{0} za n_GSP 400 kV=0; n_GSP 400 kV∈N0.
Nivo 6 podele MO GSP 400 kV i:
SMT GSP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 400 kV} za n_GSP 400 kV>0, i∈{0} za n_GSP 400 kV=0; n_GSP 400 kV∈N0.
Nivo 6 podele RO GSP 220 kV i:
SR GSP 220 kV i,
P GSP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 220 kV} za n_GSP 220 kV>0, i∈{0} za n_GSP 220 kV=0; n_GSP 220 kV∈N0.
Nivo 6 podele MO GSP 220 kV i:
SMT GSP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 220 kV} za n_GSP 220 kV>0, i∈{0} za n_GSP 220 kV=0; n_GSP 220 kV∈N0.
Nivo 6 podele RO GSP 110 kV i:
SR GSP 110 kV i,
P GSP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 110 kV} za n_GSP 110 kV>0, i∈{0} za n_GSP 110 kV=0; n_GSP 110 kV∈N0.
Nivo 6 podele MO GSP 110 kV i:
SMT GSP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP 110 kV} za n_GSP 110 kV>0, i∈{0} za n_GSP 110 kV=0; n_GSP 110 kV∈N0.
Nivo 6 podele RO GSP x kV i:
SR GSP x kV i,
P GSP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP x kV} za n_GSP x kV>0, i∈{0} za n_GSP x kV=0; n_GSP x kV∈N0.
Nivo 6 podele MO GSP x kV i:
SMT GSP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSP x kV} za n_GSP x kV>0, i∈{0} za n_GSP x kV=0; n_GSP x kV∈N0.
Nivo 6 podele RO PSP 400 kV i:
SR PSP 400 kV i,
P PSP 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 400 kV} za n_PSP 400 kV>0, i∈{0} za n_PSP 400 kV=0; n_PSP 400 kV∈N0.
Nivo 6 podele RO PSP 220 kV i:
SR PSP 220 kV i,
P PSP 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 220 kV} za n_PSP 220 kV>0, i∈{0} za n_PSP 220 kV=0; n_PSP 220 kV∈N0.
Nivo 6 podele RO PSP 110 kV i:
SR PSP 110 kV i,
P PSP 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 110 kV} za n_PSP 110 kV>0, i∈{0} za n_PSP 110 kV=0; n_PSP 110 kV∈N0.
Nivo 6 podele RO PSP x kV i:
SR PSP x kV i,
P PSP x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP x kV} za n_PSP x kV>0, i∈{0} za n_PSP x kV=0; n_PSP x kV∈N0.
Nivo 6 podele MO GSS 400 kV i:
NMT GSS 400 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, i∈{0} za n_GSS 400 kV=0; n_GSS 400 kV∈N0.
Nivo 6 podele MO GSS 220 kV i:
NMT GSS 220 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, i∈{0} za n_GSS 220 kV=0; n_GSS 220 kV∈N0.
Nivo 6 podele MO GSS 110 kV i:
NMT GSS 110 kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, i∈{0} za n_GSS 110 kV=0; n_GSS 110 kV∈N0.
Nivo 6 podele MO GSS x kV i:
NMT GSS x kV i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_GSS x kV} za n_GSS x kV>0, i∈{0} za n_GSS x kV=0; n_GSS x kV∈N0.
Nivo 7
Nivo 7 podele SR DVP 400 kV i:
SR DVP 400 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_DVP 400 kV} za n_DVP 400 kV>0, i∈{0} za n_DVP 400 kV=0; j∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, j∈{0} za n_GSS 400 kV=0; n_DVP 400 kV, n_GSS 400 kV∈N0;
SR DVP 400 kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_DVP 400 kV} za n_DVP 400 kV>0, i∈{0} za n_DVP 400 kV=0; k∈{1, ..., n_PSS 400 kV} za n_PSS 400 kV>0, k∈{0} za n_PSS 400 kV=0; n_DVP 400 kV, n_PSS 400 kV∈N0.
Nivo 7 podele SR DVP 220 kV i:
SR DVP 220 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_DVP 220 kV} za n_DVP 220 kV>0, i∈{0} za n_DVP 220 kV=0; j∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, j∈{0} za n_GSS 220 kV=0; n_DVP 220 kV, n_GSS 220 kV∈N0;
SR DVP 220 kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_DVP 220 kV} za n_DVP 220 kV>0, i∈{0} za n_DVP 220 kV=0; k∈{1, ..., n_PSS 220 kV} za n_PSS 220 kV>0, k∈{0} za n_PSS 220 kV=0; n_DVP 220 kV, n_PSS 220 kV∈N0.
Nivo 7 podele SR DVP 110 kV i:
SR DVP 110 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_DVP 110 kV} za n_DVP 110 kV>0, i∈{0} za n_DVP 110 kV=0; j∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, j∈{0} za n_GSS 110 kV=0; n_DVP 110 kV, n_GSS 110 kV∈N0;
SR DVP 110 kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_DVP 110 kV} za n_DVP 110 kV>0, i∈{0} za n_DVP 110 kV=0; k∈{1, ..., n_PSS 110 kV} za n_PSS 110 kV>0, k∈{0} za n_PSS 110 kV=0; n_DVP 110 kV, n_PSS 110 kV∈N0.
Nivo 7 podele SR DVP x kV i:
SR DVP x kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_DVP x kV} za n_DVP x kV>0, i∈{0} za n_DVP x kV=0; j∈{1, ..., n_GSS x kV} za n_GSS x kV>0, j∈{0} za n_GSS x kV=0; n_DVP x kV, n_GSS x kV∈N0;
SR DVP x kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_DVP x kV} za n_DVP x kV>0, i∈{0} za n_DVP x kV=0; k∈{1, ..., n_PSS x kV} za n_PSS x kV>0, k∈{0} za n_PSS x kV=0; n_DVP x kV, n_PSS x kV∈N0.
Nivo 7 podele SR KBP 400 kV i:
SR KBP 400 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_KBP 400 kV} za n_KBP 400 kV>0, i∈{0} za n_KBP 400 kV=0; j∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, j∈{0} za n_GSS 400 kV=0; n_KBP 400 kV, n_GSS 400 kV∈N0;
SR KBP 400 kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_KBP 400 kV} za n_KBP 400 kV>0, i∈{0} za n_KBP 400 kV=0; k∈{1, ..., n_PSS 400 kV} za n_PSS 400 kV>0, k∈{0} za n_PSS 400 kV=0; n_KBP 400 kV, n_PSS 400 kV∈N0.
Nivo 7 podele SR KBP 220 kV i:
SR KBP 220 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_KBP 220 kV} za n_KBP 220 kV>0, i∈{0} za n_KBP 220 kV=0; j∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, j∈{0} za n_GSS 220 kV=0; n_KBP 220 kV, n_GSS 220 kV∈N0;
SR KBP 220 kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_KBP 220 kV} za n_KBP 220 kV>0, i∈{0} za n_KBP 220 kV=0; k∈{1, ..., n_PSS 220 kV} za n_PSS 220 kV>0, k∈{0} za n_PSS 220 kV=0; n_KBP 220 kV, n_PSS 220 kV∈N0.
Nivo 7 podele SR KBP 110 kV i:
SR KBP 110 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_KBP 110 kV} za n_KBP 110 kV>0, i∈{0} za n_KBP 110 kV=0; j∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, j∈{0} za n_GSS 110 kV=0; n_KBP 110 kV, n_GSS 110 kV∈N0;
SR KBP 110 kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_KBP 110 kV} za n_KBP 110 kV>0, i∈{0} za n_KBP 110 kV=0; k∈{1, ..., n_PSS 110 kV} za n_PSS 110 kV>0, k∈{0} za n_PSS 110 kV=0; n_KBP 110 kV, n_PSS 110 kV∈N0.
Nivo 7 podele SR KBP x kV i:
SR KBP x kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_KBP x kV} za n_KBP x kV>0, i∈{0} za n_KBP x kV=0; j∈{1, ..., n_GSS x kV} za n_GSS x kV>0, j∈{0} za n_GSS x kV=0; n_KBP x kV, n_GSS x kV∈N0;
SR KBP x kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_KBP x kV} za n_KBP x kV>0, i∈{0} za n_KBP x kV=0; k∈{1, ..., n_PSS x kV} za n_PSS x kV>0, k∈{0} za n_PSS x kV=0; n_KBP x kV, n_PSS x kV∈N0.
Nivo 7 podele SR TRPVN TR 400/220 kV/kV i:
SR TRPVN TR 400/220 kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 400/220 kV/kV} za n_TRPVN TR 400/220 kV/kV>0, i∈{0} za n_TRPVN TR 400/220 kV/kV=0; j∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, j∈{0} za n_GSS 400 kV=0; n_TRPVN TR 400/220 kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/220 kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 400/220 kV/kV} za n_TRPVN TR 400/220 kV/kV>0, i∈{0} za n_TRPVN TR 400/220 kV/kV=0; k∈{1, ..., n_PSS 400 kV} za n_PSS 400 kV>0, k∈{0} za n_PSS 400 kV=0; n_TRPVN TR 400/220 kV/kV, n_PSS 400 kV∈N0.
Nivo 7 podele SR TRPVN TR 400/110 kV/kV i:
SR TRPVN TR 400/110 kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 400/110 kV/kV} za n_TRPVN TR 400/110 kV/kV>0, i∈{0} za n_TRPVN TR 400/110 kV/kV=0; j∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, j∈{0} za n_GSS 400 kV=0; n_TRPVN TR 400/110 kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/110 kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 400/110 kV/kV} za n_TRPVN TR 400/110 kV/kV>0, i∈{0} za n_TRPVN TR 400/110 kV/kV=0; k∈{1, ..., n_PSS 400 kV} za n_PSS 400 kV>0, k∈{0} za n_PSS 400 kV=0; n_TRPVN TR 400/110 kV/kV, n_PSS 400 kV∈N0.
Nivo 7 podele SR TRPVN TR 220/110 kV/kV i:
SR TRPVN TR 220/110 kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 220/110 kV/kV} za n_TRPVN TR 220/110 kV/kV>0, i∈{0} za n_TRPVN TR 220/110 kV/kV=0; j∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, j∈{0} za n_GSS 220 kV=0; n_TRPVN TR 220/110 kV/kV, n_GSS 220 kV∈N0;
SR TRPVN TR 220/110 kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 220/110 kV/kV} za n_TRPVN TR 220/110 kV/kV>0, i∈{0} za n_TRPVN TR 220/110 kV/kV=0; k∈{1, ..., n_PSS 220 kV} za n_PSS 220 kV>0, k∈{0} za n_PSS 220 kV=0; n_TRPVN TR 220/110 kV/kV, n_PSS 220 kV∈N0.
Nivo 7 podele SR TRPVN TR 400/x kV/kV i:
SR TRPVN TR 400/x kV/kV i GSS j,z
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 400/x kV/kV} za n_TRPVN TR 400/x kV/kV>0, i∈{0} za n_TRPVN TR 400/x kV/kV=0; j∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, j∈{0} za n_GSS 400 kV=0; n_TRPVN TR 400/x kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/x kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 400/x kV/kV} za n_TRPVN TR 400/x kV/kV>0, i∈{0} za n_TRPVN TR 400/x kV/kV=0; k∈{1, ..., n_PSS 400 kV} za n_PSS 400 kV>0, k∈{0} za n_PSS 400 kV=0; n_TRPVN TR 400/x kV/kV, n_PSS 400 kV∈N0.
Nivo 7 podele SR TRPVN TR 220/x kV/kV i:
SR TRPVN TR 220/x kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 220/x kV/kV} za n_TRPVN TR 220/x kV/kV>0, i∈{0} za n_TRPVN TR 220/x kV/kV=0; j∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, j∈{0} za n_GSS 220 kV=0; n_TRPVN TR 220/x kV/kV, n_GSS 220 kV∈N0;
SR TRPVN TR 220/x kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 220/x kV/kV} za n_TRPVN TR 220/x kV/kV>0, i∈{0} za n_TRPVN TR 220/x kV/kV=0; k∈{1, ..., n_PSS 220 kV} za n_PSS 220 kV>0, k∈{0} za n_PSS 220 kV=0; n_TRPVN TR 220/x kV/kV, n_PSS 220 kV∈N0.
Nivo 7 podele SR TRPVN TR 110/x kV/kV i:
SR TRPVN TR 110/x kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 110/x kV/kV} za n_TRPVN TR 110/x kV/kV>0, i∈{0} za n_TRPVN TR 110/x kV/kV=0; j∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, j∈{0} za n_GSS 110 kV=0; n_TRPVN TR 110/x kV/kV, n_GSS 110 kV∈N0;
SR TRPVN TR 110/x kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPVN TR 110/x kV/kV} za n_TRPVN TR 110/x kV/kV>0, i∈{0} za n_TRPVN TR 110/x kV/kV=0; k∈{1, ..., n_PSS 110 kV} za n_PSS 110 kV>0, k∈{0} za n_PSS 110 kV=0; n_TRPVN TR 110/x kV/kV, n_PSS 110 kV∈N0.
Nivo 7 podele SR TRPNN TR 400/220 kV/kV i:
SR TRPNN TR 400/220 kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 400/220 kV/kV} za n_TRPNN TR 400/220 kV/kV>0, i∈{0} za n_TRPNN TR 400/220 kV/kV=0; j∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, j∈{0} za n_GSS 220 kV=0; n_TRPNN TR 400/220 kV/kV, n_GSS 220 kV∈N0;
SR TRPNN TR 400/220 kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 400/220 kV/kV} za n_TRPNN TR 400/220 kV/kV>0, i∈{0} za n_TRPNN TR 400/220 kV/kV=0; k∈{1, ..., n_PSS 220 kV} za n_PSS 220 kV>0, k∈{0} za n_PSS 220 kV=0; n_TRPNN TR 400/220 kV/kV, n_PSS 220 kV∈N0.
Nivo 7 podele SR TRPNN TR 400/110 kV/kV i:
SR TRPNN TR 400/110 kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 400/110 kV/kV} za n_TRPNN TR 400/110 kV/kV>0, i∈{0} za n_TRPNN TR 400/110 kV/kV=0; j∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, j∈{0} za n_GSS 110 kV=0; n_TRPNN TR 400/110 kV/kV, n_GSS 110 kV∈N0;
SR TRPNN TR 400/110 kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 400/110 kV/kV} za n_TRPNN TR 400/110 kV/kV>0, i∈{0} za n_TRPNN TR 400/110 kV/kV=0; k∈{1, ..., n_PSS 110 kV} za n_PSS 110 kV>0, k∈{0} za n_PSS 110 kV=0; n_TRPNN TR 400/110 kV/kV, n_PSS 110 kV∈N0.
Nivo 7 podele SR TRPNN TR 220/110 kV/kV i:
SR TRPNN TR 220/110 kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 220/110 kV/kV} za n_TRPNN TR 220/110 kV/kV>0, i∈{0} za n_TRPNN TR 220/110 kV/kV=0; j∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, j∈{0} za n_GSS 110 kV=0; n_TRPNN TR 220/110 kV/kV, n_GSS 110 kV∈N0;
SR TRPNN TR 220/110 kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 220/110 kV/kV} za n_TRPNN TR 220/110 kV/kV>0, i∈{0} za n_TRPNN TR 220/110 kV/kV=0; k∈{1, ..., n_PSS 110 kV} za n_PSS 110 kV>0, k∈{0} za n_PSS 110 kV=0; n_TRPNN TR 220/110 kV/kV, n_PSS 110 kV∈N0.
Nivo 7 podele SR TRPNN TR 400/x kV/kV i:
SR TRPNN TR 400/x kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 400/x kV/kV} za n_TRPNN TR 400/x kV/kV>0, i∈{0} za n_TRPNN TR 400/x kV/kV=0; j∈{1, ..., n_GSS x kV} za n_GSS x kV>0, j∈{0} za n_GSS x kV=0; n_TRPNN TR 400/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 400/x kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 400/x kV/kV} za n_TRPNN TR 400/x kV/kV>0, i∈{0} za n_TRPNN TR 400/x kV/kV=0; k∈{1, ..., n_PSS x kV} za n_PSS x kV>0, k∈{0} za n_PSS x kV=0; n_TRPNN TR 400/x kV/kV, n_PSS x kV∈N0.
Nivo 7 podele SR TRPNN TR 220/x kV/kV i:
SR TRPNN TR 220/x kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 220/x kV/kV} za n_TRPNN TR 220/x kV/kV>0, i∈{0} za n_TRPNN TR 220/x kV/kV=0; j∈{1, ..., n_GSS x kV} za n_GSS x kV>0, j∈{0} za n_GSS x kV=0; n_TRPNN TR 220/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 220/x kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 220/x kV/kV} za n_TRPNN TR 220/x kV/kV>0, i∈{0} za n_TRPNN TR 220/x kV/kV=0; k∈{1, ..., n_PSS x kV} za n_PSS x kV>0, k∈{0} za n_PSS x kV=0; n_TRPNN TR 220/x kV/kV, n_PSS x kV∈N0.
Nivo 7 podele SR TRPNN TR 110/x kV/kV i:
SR TRPNN TR 110/x kV/kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 110/x kV/kV} za n_TRPNN TR 110/x kV/kV>0, i∈{0} za n_TRPNN TR 110/x kV/kV=0; j∈{1, ..., n_GSS x kV} za n_GSS x kV>0, j∈{0} za n_GSS x kV=0; n_TRPNN TR 110/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 110/x kV/kV i PSS k,
gde i-ti element niza obuhvata sve k-te elemente niza, definisanih sa i∈{1, ..., n_TRPNN TR 110/x kV/kV} za n_TRPNN TR 110/x kV/kV>0, i∈{0} za n_TRPNN TR 110/x kV/kV=0; k∈{1, ..., n_PSS x kV} za n_PSS x kV>0, k∈{0} za n_PSS x kV=0; n_TRPNN TR 110/x kV/kV, n_PSS x kV∈N0.
Nivo 7 podele SR GSP 400 kV i:
SR GSP 400 kV i GSS j,
gde i-ti element niza obuhvata j-te elemente niza, definisanih sa i∈{1, ..., n_GSP 400 kV} za n_GSP 400 kV>0, i∈{0} za n_GSP 400 kV=0; j∈{i,i+1} za n_GSP 400 kV>0, j∈{0} za n_GSP 400 kV=0; n_GSP 400 kV∈N0.
Nivo 7 podele SR GSP 220 kV i:
SR GSP 220 kV i GSS j,
gde i-ti element niza obuhvata j-te elemente niza, definisanih sa i∈{1, ..., n_GSP 220 kV} za n_GSP 220 kV>0, i∈{0} za n_GSP 220 kV=0; j∈{i,i+1} za n_GSP 220 kV>0, j∈{0} za n_GSP 220 kV=0; n_GSP 220 kV∈N0.
Nivo 7 podele SR GSP 110 kV i:
SR GSP 110 kV i GSS j,
gde i-ti element niza obuhvata j-te elemente niza, definisanih sa i∈{1, ..., n_GSP 110 kV} za n_GSP 110 kV>0, i∈{0} za n_GSP 110 kV=0; j∈{i,i+1} za n_GSP 110 kV>0, j∈{0} za n_GSP 110 kV=0; n_GSP 110 kV∈N0.
Nivo 7 podele SR GSP x kV i:
SR GSP x kV i GSS j,
gde i-ti element niza obuhvata j-te elemente niza, definisanih sa i∈{1, ..., n_GSP x kV} za n_GSP x kV>0, i∈{0} za n_GSP x kV=0; j∈{i,i+1} za n_GSP x kV>0, j∈{0} za n_GSP x kV=0; n_GSP x kV∈N0.
Nivo 7 podele SR PSP 400 kV i:
SR PSP 400 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_PSP 400 kV} za n_PSP 400 kV>0, i∈{0} za n_PSP 400 kV=0; j∈{1, ..., n_GSS 400 kV} za n_GSS 400 kV>0, j∈{0} za n_GSS 400 kV=0; n_PSP 400 kV, n_GSS 400 kV∈N0;
SR PSP 400 kV i PSS i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 400 kV} za n_PSP 400 kV>0, i∈{0} za n_PSP 400 kV=0; n_PSP 400 kV∈N0.
Nivo 7 podele SR PSP 220 kV i:
SR PSP 220 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_PSP 220 kV} za n_PSP 220 kV>0, i∈{0} za n_PSP 220 kV=0; j∈{1, ..., n_GSS 220 kV} za n_GSS 220 kV>0, j∈{0} za n_GSS 220 kV=0; n_PSP 220 kV, n_GSS 220 kV∈N0;
SR PSP 220 kV i PSS i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 220 kV} za n_PSP 220 kV>0, i∈{0} za n_PSP 220 kV=0; n_PSP 220 kV∈N0.
Nivo 7 podele SR PSP 110 kV i:
SR PSP 110 kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_PSP 110 kV} za n_PSP 110 kV>0, i∈{0} za n_PSP 110 kV=0; j∈{1, ..., n_GSS 110 kV} za n_GSS 110 kV>0, j∈{0} za n_GSS 110 kV=0; n_PSP 110 kV, n_GSS 110 kV∈N0;
SR PSP 110 kV i PSS i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP 110 kV} za n_PSP 110 kV>0, i∈{0} za n_PSP 110 kV=0; n_PSP 110 kV∈N0.
Nivo 7 podele SR PSP x kV i:
SR PSP x kV i GSS j,
gde i-ti element niza obuhvata sve j-te elemente niza, definisanih sa i∈{1, ..., n_PSP x kV} za n_PSP x kV>0, i∈{0} za n_PSP x kV=0; j∈{1, ..., n_GSS x kV} za n_GSS x kV>0, j∈{0} za n_GSS x kV=0; n_PSP x kV, n_GSS x kV∈N0;
SR PSP x kV i PSS i,
gde i označava i-ti element niza definisan sa i∈{1, ..., n_PSP x kV} za n_PSP x kV>0, i∈{0} za n_PSP x kV=0; n_PSP x kV∈N0.
### Elektroenergetska oprema PS koja ne pripada EEO
Elektroenergetska oprema PS koja ne pripada EEO označava opremu koja se po mestu ugradnje, odnosno fizički ne nalazi unutar EEO.
Nivo 1
Nivo 1 podele Elektroenergetska oprema PS koja ne pripada EEO:
VO.
Nivo 2
Nivo 2 podele VO:
DV,
KB,
MV.
Nivo 3
Nivo 3 podele DV:
DV 400 kV,
DV 220 kV,
DV 110 kV,
DV x kV.
Nivo 3 podele KB:
KB 400 kV,
KB 220 kV,
KB 110 kV,
KB x kV.
Nivo 3 podele MV:
MV (DV+KB),
MV (KB+DV).
Nivo 4
Nivo 4 podele DV 400 kV:
DV 400 kV EEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 4 podele DV 220 kV:
DV 220 kV EEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 4 podele DV 110 kV:
DV 110 kV EEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 4 podele DV x kV:
DV x kV EEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 4 podele KB 400 kV:
KB 400 kV EEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 4 podele KB 220 kV:
KB 220 kV EEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 4 podele KB 110 kV:
KB 110 kV EEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 4 podele KB x kV:
KB x kV EEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 4 podele MV (DV+KB):
MV (DV+KB) 400 kV,
MV (DV+KB) 220 kV,
MV (DV+KB) 110 kV,
MV (DV+KB) x kV.
Nivo 4 podele MV (KB+DV):
MV (KB+DV) 400 kV,
MV (KB+DV) 220 kV,
MV (KB+DV) 110 kV,
MV (KB+DV) x kV.
Nivo 5
Nivo 5 podele DV 400 kV EEO x EEO y:
DV 400 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_DVP 400 kV} za EEO x n_DVP 400 kV>0, m∈{0} za EEO x n_DVP 400 kV=0; n∈{1, ..., EEO y n_DVP 400 kV} za EEO y n_DVP 400 kV>0, n∈{0} za EEO y n_DVP 400 kV=0; n_EEO∈N0, EEO x n_DVP 400 kV, EEO y n_DVP 400 kV∈N.
Nivo 5 podele DV 220 kV EEO x EEO y:
DV 220 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_DVP 220 kV} za EEO x n_DVP 220 kV>0, m∈{0} za EEO x n_DVP 220 kV=0; n∈{1, ..., EEO y n_DVP 220 kV} za EEO y n_DVP 220 kV>0, n∈{0} za EEO y n_DVP 220 kV=0; n_EEO∈N0, EEO x n_DVP 220 kV, EEO y n_DVP 220 kV∈N.
Nivo 5 podele DV 110 kV EEO x EEO y:
DV 110 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_DVP 110 kV} za EEO x n_DVP 110 kV>0, m∈{0} za EEO x n_DVP 110 kV=0; n∈{1, ..., EEO y n_DVP 110 kV} za EEO y n_DVP 110 kV>0, n∈{0} za EEO y n_DVP 110 kV=0; n_EEO∈N0, EEO x n_DVP 110 kV, EEO y n_DVP 110 kV∈N.
Nivo 5 podele DV x kV EEO x EEO y:
DV x kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_DVP x kV} za EEO x n_DVP x kV>0, m∈{0} za EEO x n_DVP x kV=0; n∈{1, ..., EEO y n_DVP x kV} za EEO y n_DVP x kV>0, n∈{0} za EEO y n_DVP x kV=0; n_EEO∈N0, EEO x n_DVP x kV, EEO y n_DVP x kV∈N.
Nivo 5 podele KB 400 kV EEO x EEO y:
KB 400 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_KBP 400 kV} za EEO x n_KBP 400 kV>0, m∈{0} za EEO x n_KBP 400 kV=0; n∈{1, ..., EEO y n_KBP 400 kV} za EEO y n_KBP 400 kV>0, n∈{0} za EEO y n_KBP 400 kV=0; n_EEO∈N0, EEO x n_KBP 400 kV, EEO y n_KBP 400 kV∈N.
Nivo 5 podele KB 220 kV EEO x EEO y:
KB 220 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_KBP 220 kV} za EEO x n_KBP 220 kV>0, m∈{0} za EEO x n_KBP 220 kV=0; n∈{1, ..., EEO y n_KBP 220 kV} za EEO y n_KBP 220 kV>0, n∈{0} za EEO y n_KBP 220 kV=0; n_EEO∈N0, EEO x n_KBP 220 kV, EEO y n_KBP 220 kV∈N.
Nivo 5 podele KB 110 kV EEO x EEO y:
KB 110 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_KBP 110 kV} za EEO x n_KBP 110 kV>0, m∈{0} za EEO x n_KBP 110 kV=0; n∈{1, ..., EEO y n_KBP 110 kV} za EEO y n_KBP 110 kV>0, n∈{0} za EEO y n_KBP 110 kV=0; n_EEO∈N0, EEO x n_KBP 110 kV, EEO y n_KBP 110 kV∈N.
Nivo 5 podele KB x kV EEO x EEO y:
KB x kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_KBP x kV} za EEO x n_KBP x kV>0, m∈{0} za EEO x n_KBP x kV=0; n∈{1, ..., EEO y n_KBP x kV} za EEO y n_KBP x kV>0, n∈{0} za EEO y n_KBP x kV=0; n_EEO∈N0, EEO x n_KBP x kV, EEO y n_KBP x kV∈N.
Nivo 5 podele MV (DV+KB) 400 kV:
MV (DV+KB) 400 kVEEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 5 podele MV (DV+KB) 220 kV:
MV (DV+KB) 220 kVEEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 5 podele MV (DV+KB) 110 kV:
MV (DV+KB) 110 kVEEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 5 podele MV (DV+KB) x kV:
MV (DV+KB) x kVEEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 5 podele MV (KB+DV) 400 kV:
MV (KB+DV) 400 kVEEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 5 podele MV (KB+DV) 220 kV:
MV (KB+DV) 220 kVEEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 5 podele MV (KB+DV) 110 kV:
MV (KB+DV) 110 kVEEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 5 podele MV (KB+DV) x kV:
MV (KB+DV) x kVEEO x EEO y,
gde uređena dvojka indeksa x i y odeđuje element niza. Indeksi x i y su definisani sa x, y∈{1, ..., n_EEO}, n_EEO>1; n_EEO∈N.
Nivo 6
Nivo 6 podele MV (KB+DV) 400 kV:
MV (DV+KB) 400 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_DVP 400 kV} za EEO x n_DVP 400 kV>0, m∈{0} za EEO x n_DVP 400 kV=0; n∈{1, ..., EEO y n_KBP 400 kV} za EEO y n_KBP 400 kV>0, n∈{0} za EEO y n_KBP 400 kV=0; n_EEO∈N0, EEO x n_DVP 400 kV, EEO y n_KBP 400 kV∈N.
Nivo 6 podele MV (KB+DV) 220 kV:
MV (DV+KB) 220 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_DVP 220 kV} za EEO x n_DVP 220 kV>0, m∈{0} za EEO x n_DVP 220 kV=0; n∈{1, ..., EEO y n_KBP 220 kV} za EEO y n_KBP 220 kV>0, n∈{0} za EEO y n_KBP 220 kV=0; n_EEO∈N0, EEO x n_DVP 220 kV, EEO y n_KBP 220 kV∈N.
Nivo 6 podele MV (KB+DV) 110 kV:
MV (DV+KB) 110 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_DVP 110 kV} za EEO x n_DVP 110 kV>0, m∈{0} za EEO x n_DVP 110 kV=0; n∈{1, ..., EEO y n_KBP 110 kV} za EEO y n_KBP 110 kV>0, n∈{0} za EEO y n_KBP 110 kV=0; n_EEO∈N0, EEO x n_DVP 110 kV, EEO y n_KBP 110 kV∈N.
Nivo 6 podele MV (KB+DV) x kV:
MV (DV+KB) x kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_DVP x kV} za EEO x n_DVP x kV>0, m∈{0} za EEO x n_DVP x kV=0; n∈{1, ..., EEO y n_KBP x kV} za EEO y n_KBP x kV>0, n∈{0} za EEO y n_KBP x kV=0; n_EEO∈N0, EEO x n_DVP x kV, EEO y n_KBP x kV∈N.
Nivo 6 podele MV (KB+DV) 400 kV EEO x EEO y:
MV (KB+DV) 400 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_KBP 400 kV} za EEO x n_KBP 400 kV>0, m∈{0} za EEO x n_KBP 400 kV=0; n∈{1, ..., EEO y n_DVP 400 kV} za EEO y n_DVP 400 kV>0, n∈{0} za EEO y n_DVP 400 kV=0; n_EEO∈N0, EEO x n_KBP 400 kV, EEO y n_DVP 400 kV∈N.

Nivo 6 podele MV (KB+DV) 220 kV EEO x EEO y:
MV (KB+DV) 220 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_KBP 220 kV} za EEO x n_KBP 220 kV>0, m∈{0} za EEO x n_KBP 220 kV=0; n∈{1, ..., EEO y n_DVP 220 kV} za EEO y n_DVP 220 kV>0, n∈{0} za EEO y n_DVP 220 kV=0; n_EEO∈N0, EEO x n_KBP 220 kV, EEO y n_DVP 220 kV∈N.
Nivo 6 podele MV (KB+DV) 110 kV EEO x EEO y:
MV (KB+DV) 110 kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_KBP 110 kV} za EEO x n_KBP 110 kV>0, m∈{0} za EEO x n_KBP 110 kV=0; n∈{1, ..., EEO y n_DVP 110 kV} za EEO y n_DVP 110 kV>0, n∈{0} za EEO y n_DVP 110 kV=0; n_EEO∈N0, EEO x n_KBP 110 kV, EEO y n_DVP 110 kV∈N.
Nivo 6 podele MV (KB+DV) x kV EEO x EEO y:
MV (KB+DV) x kV EEO x (m) EEO y (n),
gde uređena četvorka indeksa x, y, m i n odeđuje element niza. Indeksi x, y, m i n su definisani sa x, y∈{1, ..., n_EEO} n_EEO>1; m∈{1, ..., EEO x n_KBP x kV} za EEO x n_KBP x kV>0, m∈{0} za EEO x n_KBP x kV=0; n∈{1, ..., EEO y n_DVP x kV} za EEO y n_DVP x kV>0, n∈{0} za EEO y n_DVP x kV=0; n_EEO∈N0, EEO x n_KBP x kV, EEO y n_DVP x kV∈N.
### Osnovni elementi elektroenergetske opreme PS - listovi
Svaka grana u podeli tipa stablo koja nema dalje grananje predstavlja list. Jedan list predstavlja jedan odnosni element.
Osnovni elementi elektroenergetske opreme PS koja pripada EEO
Osnovi elementi podele, odnosno listovi elektroenergetske opreme koja pripada EEO sa definisanim postojanjem su:
SR DVP 400 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR DVP 400 kV i GSS j) ⟺ (n_DVP 400 kV>0 ∧ n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR DVP 400 kV i GSS j) ⟺ (n_DVP 400 kV=0 ∨ n_GSS 400 kV=0),
i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_DVP 400 kV, n_GSS 400 kV∈N0;
SR DVP 400 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR DVP 400 kV i PSS k) ⟺ (n_DVP 400 kV>0 ∧ n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR DVP 400 kV i PSS k) ⟺ (n_DVP 400 kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_DVP 400 kV, n_PSS 400 kV∈N0;
P DVP 400 kV i:
∀i (i≠0) ⟹ ∃ (P DVP 400 kV i) ⟺ (n_DVP 400 kV>0),
i=0 ⟹ ∄ (P DVP 400 kV i) ⟺ (n_DVP 400 kV=0),
i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
IRSU DVP 400 kV i:
∀i (i≠0) ⟹ ∃ (IRSU DVP 400 kV i) ⟺ (n_DVP 400 kV>0),
i=0 ⟹ ∄ (IRSU DVP 400 kV i) ⟺ (n_DVP 400 kV=0),
i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
SMT DVP 400 kV i:
∀i (i≠0) ⟹ ∃ (SMT DVP 400 kV i) ⟺ (n_DVP 400 kV>0),
i=0 ⟹ ∄ (SMT DVP 400 kV i) ⟺ (n_DVP 400 kV=0),
i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
NMT DVP 400 kV i:
∀i (i≠0) ⟹ ∃ (NMT DVP 400 kV i) ⟺ (n_DVP 400 kV>0),
i=0 ⟹ ∄ (NMT DVP 400 kV i) ⟺ (n_DVP 400 kV=0),
i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
SR DVP 220 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR DVP 220 kV i GSS j) ⟺ (n_DVP 220 kV>0 ∧ n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR DVP 220 kV i GSS j) ⟺ (n_DVP 220 kV=0 ∨ n_GSS 220 kV=0),
i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_DVP 220 kV, n_GSS 220 kV∈N0;
SR DVP 220 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR DVP 220 kV i PSS k) ⟺ (n_DVP 220 kV>0 ∧ n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR DVP 220 kV i PSS k) ⟺ (n_DVP 220 kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_DVP 220 kV, n_PSS 220 kV∈N0;
P DVP 220 kV i:
∀i (i≠0) ⟹ ∃ (P DVP 220 kV i) ⟺ (n_DVP 220 kV>0),
i=0 ⟹ ∄ (P DVP 220 kV i) ⟺ (n_DVP 220 kV=0),
i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
IRSU DVP 220 kV i:
∀i (i≠0) ⟹ ∃ (IRSU DVP 220 kV i) ⟺ (n_DVP 220 kV>0),
i=0 ⟹ ∄ (IRSU DVP 220 kV i) ⟺ (n_DVP 220 kV=0),
i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
SMT DVP 220 kV i:
∀i (i≠0) ⟹ ∃ (SMT DVP 220 kV i) ⟺ (n_DVP 220 kV>0),
i=0 ⟹ ∄ (SMT DVP 220 kV i) ⟺ (n_DVP 220 kV=0),
i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
NMT DVP 220 kV i:
∀i (i≠0) ⟹ ∃ (NMT DVP 220 kV i) ⟺ (n_DVP 220 kV>0),
i=0 ⟹ ∄ (NMT DVP 220 kV i) ⟺ (n_DVP 220 kV=0),
i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
SR DVP 110 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR DVP 110 kV i GSS j) ⟺ (n_DVP 110 kV>0 ∧ n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR DVP 110 kV i GSS j) ⟺ (n_DVP 110 kV=0 ∨ n_GSS 110 kV=0),
i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_DVP 110 kV, n_GSS 110 kV∈N0;
SR DVP 110 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR DVP 110 kV i PSS k) ⟺ (n_DVP 110 kV>0 ∧ n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR DVP 110 kV i PSS k) ⟺ (n_DVP 110 kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_DVP 110 kV, n_PSS 110 kV∈N0;
P DVP 110 kV i:
∀i (i≠0) ⟹ ∃ (P DVP 110 kV i) ⟺ (n_DVP 110 kV>0),
i=0 ⟹ ∄ (P DVP 110 kV i) ⟺ (n_DVP 110 kV=0),
i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
IRSU DVP 110 kV i:
∀i (i≠0) ⟹ ∃ (IRSU DVP 110 kV i) ⟺ (n_DVP 110 kV>0),
i=0 ⟹ ∄ (IRSU DVP 110 kV i) ⟺ (n_DVP 110 kV=0),
i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
SMT DVP 110 kV i:
∀i (i≠0) ⟹ ∃ (SMT DVP 110 kV i) ⟺ (n_DVP 110 kV>0),
i=0 ⟹ ∄ (SMT DVP 110 kV i) ⟺ (n_DVP 110 kV=0),
i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
NMT DVP 110 kV i:
∀i (i≠0) ⟹ ∃ (NMT DVP 110 kV i) ⟺ (n_DVP 110 kV>0),
i=0 ⟹ ∄ (NMT DVP 110 kV i) ⟺ (n_DVP 110 kV=0),
i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
SR DVP x kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR DVP x kV i GSS j) ⟺ (n_DVP x kV>0 ∧ n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR DVP x kV i GSS j) ⟺ (n_DVP x kV=0 ∨ n_GSS x kV=0),
i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_DVP x kV, n_GSS x kV∈N0;
SR DVP x kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR DVP x kV i PSS k) ⟺ (n_DVP x kV>0 ∧ n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR DVP x kV i PSS k) ⟺ (n_DVP x kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_DVP x kV, n_PSS x kV∈N0;
P DVP x kV i:
∀i (i≠0) ⟹ ∃ (P DVP x kV i) ⟺ (n_DVP x kV>0),
i=0 ⟹ ∄ (P DVP x kV i) ⟺ (n_DVP x kV=0),
i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
IRSU DVP x kV i:
∀i (i≠0) ⟹ ∃ (IRSU DVP x kV i) ⟺ (n_DVP x kV>0),
i=0 ⟹ ∄ (IRSU DVP x kV i) ⟺ (n_DVP x kV=0),
i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
SMT DVP x kV i:
∀i (i≠0) ⟹ ∃ (SMT DVP x kV i) ⟺ (n_DVP x kV>0),
i=0 ⟹ ∄ (SMT DVP x kV i) ⟺ (n_DVP x kV=0),
i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
NMT DVP x kV i:
∀i (i≠0) ⟹ ∃ (NMT DVP x kV i) ⟺ (n_DVP x kV>0),
i=0 ⟹ ∄ (NMT DVP x kV i) ⟺ (n_DVP x kV=0),
i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
SR KBP 400 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR KBP 400 kV i GSS j) ⟺ (n_KBP 400 kV>0 ∧ n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR KBP 400 kV i GSS j) ⟺ (n_KBP 400 kV=0 ∨ n_GSS 400 kV=0),
i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_KBP 400 kV, n_GSS 400 kV∈N0;
SR KBP 400 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR KBP 400 kV i PSS k) ⟺ (n_KBP 400 kV>0 ∧ n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR KBP 400 kV i PSS k) ⟺ (n_KBP 400 kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_KBP 400 kV, n_PSS 400 kV∈N0;
P KBP 400 kV i:
∀i (i≠0) ⟹ ∃ (P KBP 400 kV i) ⟺ (n_KBP 400 kV>0),
i=0 ⟹ ∄ (P KBP 400 kV i) ⟺ (n_KBP 400 kV=0),
i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
IRSU KBP 400 kV i:
∀i (i≠0) ⟹ ∃ (IRSU KBP 400 kV i) ⟺ (n_KBP 400 kV>0),
i=0 ⟹ ∄ (IRSU KBP 400 kV i) ⟺ (n_KBP 400 kV=0),
i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
SMT KBP 400 kV i:
∀i (i≠0) ⟹ ∃ (SMT KBP 400 kV i) ⟺ (n_KBP 400 kV>0),
i=0 ⟹ ∄ (SMT KBP 400 kV i) ⟺ (n_KBP 400 kV=0),
i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
NMT KBP 400 kV i:
∀i (i≠0) ⟹ ∃ (NMT KBP 400 kV i) ⟺ (n_KBP 400 kV>0),
i=0 ⟹ ∄ (NMT KBP 400 kV i) ⟺ (n_KBP 400 kV=0),
i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
SR KBP 220 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR KBP 220 kV i GSS j) ⟺ (n_KBP 220 kV>0 ∧ n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR KBP 220 kV i GSS j) ⟺ (n_KBP 220 kV=0 ∨ n_GSS 220 kV=0),
i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_KBP 220 kV, n_GSS 220 kV∈N0;
SR KBP 220 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR KBP 220 kV i PSS k) ⟺ (n_KBP 220 kV>0 ∧ n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR KBP 220 kV i PSS k) ⟺ (n_KBP 220 kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_KBP 220 kV, n_PSS 220 kV∈N0;
P KBP 220 kV i:
∀i (i≠0) ⟹ ∃ (P KBP 220 kV i) ⟺ (n_KBP 220 kV>0),
i=0 ⟹ ∄ (P KBP 220 kV i) ⟺ (n_KBP 220 kV=0),
i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
IRSU KBP 220 kV i:
∀i (i≠0) ⟹ ∃ (IRSU KBP 220 kV i) ⟺ (n_KBP 220 kV>0),
i=0 ⟹ ∄ (IRSU KBP 220 kV i) ⟺ (n_KBP 220 kV=0),
i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
SMT KBP 220 kV i:
∀i (i≠0) ⟹ ∃ (SMT KBP 220 kV i) ⟺ (n_KBP 220 kV>0),
i=0 ⟹ ∄ (SMT KBP 220 kV i) ⟺ (n_KBP 220 kV=0),
i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
NMT KBP 220 kV i:
∀i (i≠0) ⟹ ∃ (NMT KBP 220 kV i) ⟺ (n_KBP 220 kV>0),
i=0 ⟹ ∄ (NMT KBP 220 kV i) ⟺ (n_KBP 220 kV=0),
i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
SR KBP 110 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR KBP 110 kV i GSS j) ⟺ (n_KBP 110 kV>0 ∧ n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR KBP 110 kV i GSS j) ⟺ (n_KBP 110 kV=0 ∨ n_GSS 110 kV=0),
i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_KBP 110 kV, n_GSS 110 kV∈N0;
SR KBP 110 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR KBP 110 kV i PSS k) ⟺ (n_KBP 110 kV>0 ∧ n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR KBP 110 kV i PSS k) ⟺ (n_KBP 110 kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_KBP 110 kV, n_PSS 110 kV∈N0;
P KBP 110 kV i:
∀i (i≠0) ⟹ ∃ (P KBP 110 kV i) ⟺ (n_KBP 110 kV>0),
i=0 ⟹ ∄ (P KBP 110 kV i) ⟺ (n_KBP 110 kV=0),
i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
IRSU KBP 110 kV i:
∀i (i≠0) ⟹ ∃ (IRSU KBP 110 kV i) ⟺ (n_KBP 110 kV>0),
i=0 ⟹ ∄ (IRSU KBP 110 kV i) ⟺ (n_KBP 110 kV=0),
i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
SMT KBP 110 kV i:
∀i (i≠0) ⟹ ∃ (SMT KBP 110 kV i) ⟺ (n_KBP 110 kV>0),
i=0 ⟹ ∄ (SMT KBP 110 kV i) ⟺ (n_KBP 110 kV=0),
i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
NMT KBP 110 kV i:
∀i (i≠0) ⟹ ∃ (NMT KBP 110 kV i) ⟺ (n_KBP 110 kV>0),
i=0 ⟹ ∄ (NMT KBP 110 kV i) ⟺ (n_KBP 110 kV=0),
i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
SR KBP x kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR KBP x kV i GSS j) ⟺ (n_KBP x kV>0 ∧ n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR KBP x kV i GSS j) ⟺ (n_KBP x kV=0 ∨ n_GSS x kV=0),
i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_KBP x kV, n_GSS x kV∈N0;
SR KBP x kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR KBP x kV i PSS k) ⟺ (n_KBP x kV>0 ∧ n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR KBP x kV i PSS k) ⟺ (n_KBP x kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_KBP x kV, n_PSS x kV∈N0;
P KBP x kV i:
∀i (i≠0) ⟹ ∃ (P KBP x kV i) ⟺ (n_KBP x kV>0),
i=0 ⟹ ∄ (P KBP x kV i) ⟺ (n_KBP x kV=0),
i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
IRSU KBP x kV i:
∀i (i≠0) ⟹ ∃ (IRSU KBP x kV i) ⟺ (n_KBP x kV>0),
i=0 ⟹ ∄ (IRSU KBP x kV i) ⟺ (n_KBP x kV=0),
i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
SMT KBP x kV i:
∀i (i≠0) ⟹ ∃ (SMT KBP x kV i) ⟺ (n_KBP x kV>0),
i=0 ⟹ ∄ (SMT KBP x kV i) ⟺ (n_KBP x kV=0),
i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
NMT KBP x kV i:
∀i (i≠0) ⟹ ∃ (NMT KBP x kV i) ⟺ (n_KBP x kV>0),
i=0 ⟹ ∄ (NMT KBP x kV i) ⟺ (n_KBP x kV=0),
i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
SR TRPVN TR 400/220 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPVN TR 400/220 kV/kV i GSS j) ⟺ (n_TRPVN TR 400/220 kV/kV>0 ∧ n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPVN TR 400/220 kV/kV i GSS j) ⟺ (n_TRPVN TR 400/220 kV/kV=0 ∨ n_GSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/220 kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/220 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPVN TR 400/220 kV/kV i PSS k) ⟺ (n_TRPVN TR 400/220 kV/kV>0 ∧ n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPVN TR 400/220 kV/kV i PSS k) ⟺ (n_TRPVN TR 400/220 kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/220 kV/kV, n_PSS 400 kV∈N0;
IR TRPVN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPVN TR 400/220 kV/kV i) ⟺ (n_TRPVN TR 400/220 kV/kV>0 ∧ n_PSS 400 kV>0),
i=0 ⟹ ∄ (IR TRPVN TR 400/220 kV/kV i) ⟺ (n_TRPVN TR 400/220 kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
P TRPVN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPVN TR 400/220 kV/kV i) ⟺ (n_TRPVN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (P TRPVN TR 400/220 kV/kV i) ⟺ (n_TRPVN TR 400/220 kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
SMT TRPVN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPVN TR 400/220 kV/kV i) ⟺ (n_TRPVN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (SMT TRPVN TR 400/220 kV/kV i) ⟺ (n_TRPVN TR 400/220 kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
OP TRPVN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPVN TR 400/220 kV/kV i) ⟺ (n_TRPVN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (OP TRPVN TR 400/220 kV/kV i) ⟺ (n_TRPVN TR 400/220 kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
SR TRPVN TR 400/110 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPVN TR 400/110 kV/kV i GSS j) ⟺ (n_TRPVN TR 400/110 kV/kV>0 ∧ n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPVN TR 400/110 kV/kV i GSS j) ⟺ (n_TRPVN TR 400/110 kV/kV=0 ∨ n_GSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/110 kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/110 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPVN TR 400/110 kV/kV i PSS k) ⟺ (n_TRPVN TR 400/110 kV/kV>0 ∧ n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPVN TR 400/110 kV/kV i PSS k) ⟺ (n_TRPVN TR 400/110 kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/110 kV/kV, n_PSS 400 kV∈N0;
IR TRPVN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPVN TR 400/110 kV/kV i) ⟺ (n_TRPVN TR 400/110 kV/kV>0 ∧ n_PSS 400 kV>0),
i=0 ⟹ ∄ (IR TRPVN TR 400/110 kV/kV i) ⟺ (n_TRPVN TR 400/110 kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
P TRPVN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPVN TR 400/110 kV/kV i) ⟺ (n_TRPVN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (P TRPVN TR 400/110 kV/kV i) ⟺ (n_TRPVN TR 400/110 kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
SMT TRPVN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPVN TR 400/110 kV/kV i) ⟺ (n_TRPVN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (SMT TRPVN TR 400/110 kV/kV i) ⟺ (n_TRPVN TR 400/110 kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
OP TRPVN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPVN TR 400/110 kV/kV i) ⟺ (n_TRPVN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (OP TRPVN TR 400/110 kV/kV i) ⟺ (n_TRPVN TR 400/110 kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
SR TRPVN TR 220/110 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPVN TR 220/110 kV/kV i GSS j) ⟺ (n_TRPVN TR 220/110 kV/kV>0 ∧ n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPVN TR 220/110 kV/kV i GSS j) ⟺ (n_TRPVN TR 220/110 kV/kV=0 ∨ n_GSS 220 kV=0),
i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/110 kV/kV, n_GSS 220 kV∈N0;
SR TRPVN TR 220/110 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPVN TR 220/110 kV/kV i PSS k) ⟺ (n_TRPVN TR 220/110 kV/kV>0 ∧ n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPVN TR 220/110 kV/kV i PSS k) ⟺ (n_TRPVN TR 220/110 kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPVN TR 220/110 kV/kV, n_PSS 220 kV∈N0;
IR TRPVN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPVN TR 220/110 kV/kV i) ⟺ (n_TRPVN TR 220/110 kV/kV>0 ∧ n_PSS 220 kV>0),
i=0 ⟹ ∄ (IR TRPVN TR 220/110 kV/kV i) ⟺ (n_TRPVN TR 220/110 kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
P TRPVN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPVN TR 220/110 kV/kV i) ⟺ (n_TRPVN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (P TRPVN TR 220/110 kV/kV i) ⟺ (n_TRPVN TR 220/110 kV/kV=0),
i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
SMT TRPVN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPVN TR 220/110 kV/kV i) ⟺ (n_TRPVN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (SMT TRPVN TR 220/110 kV/kV i) ⟺ (n_TRPVN TR 220/110 kV/kV=0),
i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
OP TRPVN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPVN TR 220/110 kV/kV i) ⟺ (n_TRPVN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (OP TRPVN TR 220/110 kV/kV i) ⟺ (n_TRPVN TR 220/110 kV/kV=0),
i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
SR TRPVN TR 400/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPVN TR 400/x kV/kV i GSS j) ⟺ (n_TRPVN TR 400/x kV/kV>0 ∧ n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPVN TR 400/x kV/kV i GSS j) ⟺ (n_TRPVN TR 400/x kV/kV=0 ∨ n_GSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/x kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPVN TR 400/x kV/kV i PSS k) ⟺ (n_TRPVN TR 400/x kV/kV>0 ∧ n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPVN TR 400/x kV/kV i PSS k) ⟺ (n_TRPVN TR 400/x kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/x kV/kV, n_PSS 400 kV∈N0;
IR TRPVN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPVN TR 400/x kV/kV i) ⟺ (n_TRPVN TR 400/x kV/kV>0 ∧ n_PSS 400 kV>0),
i=0 ⟹ ∄ (IR TRPVN TR 400/x kV/kV i) ⟺ (n_TRPVN TR 400/x kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
P TRPVN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPVN TR 400/x kV/kV i) ⟺ (n_TRPVN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (P TRPVN TR 400/x kV/kV i) ⟺ (n_TRPVN TR 400/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
SMT TRPVN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPVN TR 400/x kV/kV i) ⟺ (n_TRPVN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (SMT TRPVN TR 400/x kV/kV i) ⟺ (n_TRPVN TR 400/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
OP TRPVN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPVN TR 400/x kV/kV i) ⟺ (n_TRPVN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (OP TRPVN TR 400/x kV/kV i) ⟺ (n_TRPVN TR 400/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
SR TRPVN TR 220/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPVN TR 220/x kV/kV i GSS j) ⟺ (n_TRPVN TR 220/x kV/kV>0 ∧ n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPVN TR 220/x kV/kV i GSS j) ⟺ (n_TRPVN TR 220/x kV/kV=0 ∨ n_GSS 220 kV=0),
i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/x kV/kV, n_GSS 220 kV∈N0;
SR TRPVN TR 220/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPVN TR 220/x kV/kV i PSS k) ⟺ (n_TRPVN TR 220/x kV/kV>0 ∧ n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPVN TR 220/x kV/kV i PSS k) ⟺ (n_TRPVN TR 220/x kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPVN TR 220/x kV/kV, n_PSS 220 kV∈N0;
IR TRPVN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPVN TR 220/x kV/kV i) ⟺ (n_TRPVN TR 220/x kV/kV>0 ∧ n_PSS 220 kV>0),
i=0 ⟹ ∄ (IR TRPVN TR 220/x kV/kV i) ⟺ (n_TRPVN TR 220/x kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
P TRPVN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPVN TR 220/x kV/kV i) ⟺ (n_TRPVN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (P TRPVN TR 220/x kV/kV i) ⟺ (n_TRPVN TR 220/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
SMT TRPVN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPVN TR 220/x kV/kV i) ⟺ (n_TRPVN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (SMT TRPVN TR 220/x kV/kV i) ⟺ (n_TRPVN TR 220/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
OP TRPVN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPVN TR 220/x kV/kV i) ⟺ (n_TRPVN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (OP TRPVN TR 220/x kV/kV i) ⟺ (n_TRPVN TR 220/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
SR TRPVN TR 110/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPVN TR 110/x kV/kV i GSS j) ⟺ (n_TRPVN TR 110/x kV/kV>0 ∧ n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPVN TR 110/x kV/kV i GSS j) ⟺ (n_TRPVN TR 110/x kV/kV=0 ∨ n_GSS 110 kV=0),
i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPVN TR 110/x kV/kV, n_GSS 110 kV∈N0;
SR TRPVN TR 110/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPVN TR 110/x kV/kV i PSS k) ⟺ (n_TRPVN TR 110/x kV/kV>0 ∧ n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPVN TR 110/x kV/kV i PSS k) ⟺ (n_TRPVN TR 110/x kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPVN TR 110/x kV/kV, n_PSS 110 kV∈N0;
IR TRPVN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPVN TR 110/x kV/kV i) ⟺ (n_TRPVN TR 110/x kV/kV>0 ∧ n_PSS 110 kV>0),
i=0 ⟹ ∄ (IR TRPVN TR 110/x kV/kV i) ⟺ (n_TRPVN TR 110/x kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
P TRPVN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPVN TR 110/x kV/kV i) ⟺ (n_TRPVN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (P TRPVN TR 110/x kV/kV i) ⟺ (n_TRPVN TR 110/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
SMT TRPVN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPVN TR 110/x kV/kV i) ⟺ (n_TRPVN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (SMT TRPVN TR 110/x kV/kV i) ⟺ (n_TRPVN TR 110/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
OP TRPVN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPVN TR 110/x kV/kV i) ⟺ (n_TRPVN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (OP TRPVN TR 110/x kV/kV i) ⟺ (n_TRPVN TR 110/x kV/kV=0),
i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
SR TRPNN TR 400/220 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPNN TR 400/220 kV/kV i GSS j) ⟺ (n_TRPNN TR 400/220 kV/kV>0 ∧ n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPNN TR 400/220 kV/kV i GSS j) ⟺ (n_TRPNN TR 400/220 kV/kV=0 ∨ n_GSS 220 kV=0),
i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_GSS 220 kV∈N0;
SR TRPNN TR 400/220 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPNN TR 400/220 kV/kV i PSS k) ⟺ (n_TRPNN TR 400/220 kV/kV>0 ∧ n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPNN TR 400/220 kV/kV i PSS k) ⟺ (n_TRPNN TR 400/220 kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_PSS 220 kV∈N0;
IR TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV>0 ∧ n_PSS 220 kV>0),
i=0 ⟹ ∄ (IR TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
P TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (P TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
SMT TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (SMT TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
NMT TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (NMT TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (NMT TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
OP TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (OP TRPNN TR 400/220 kV/kV i) ⟺ (n_TRPNN TR 400/220 kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
SR TRPNN TR 400/110 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPNN TR 400/110 kV/kV i GSS j) ⟺ (n_TRPNN TR 400/110 kV/kV>0 ∧ n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPNN TR 400/110 kV/kV i GSS j) ⟺ (n_TRPNN TR 400/110 kV/kV=0 ∨ n_GSS 110 kV=0),
i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_GSS 110 kV∈N0;
SR TRPNN TR 400/110 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPNN TR 400/110 kV/kV i PSS k) ⟺ (n_TRPNN TR 400/110 kV/kV>0 ∧ n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPNN TR 400/110 kV/kV i PSS k) ⟺ (n_TRPNN TR 400/110 kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_PSS 110 kV∈N0;
IR TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV>0 ∧ n_PSS 110 kV>0),
i=0 ⟹ ∄ (IR TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
P TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (P TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
SMT TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (SMT TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
NMT TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (NMT TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (NMT TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
OP TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (OP TRPNN TR 400/110 kV/kV i) ⟺ (n_TRPNN TR 400/110 kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
SR TRPNN TR 220/110 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPNN TR 220/110 kV/kV i GSS j) ⟺ (n_TRPNN TR 220/110 kV/kV>0 ∧ n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPNN TR 220/110 kV/kV i GSS j) ⟺ (n_TRPNN TR 220/110 kV/kV=0 ∨ n_GSS 110 kV=0),
i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_GSS 110 kV∈N0;
SR TRPNN TR 220/110 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPNN TR 220/110 kV/kV i PSS k) ⟺ (n_TRPNN TR 220/110 kV/kV>0 ∧ n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPNN TR 220/110 kV/kV i PSS k) ⟺ (n_TRPNN TR 220/110 kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_PSS 110 kV∈N0;
IR TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV>0 ∧ n_PSS 110 kV>0),
i=0 ⟹ ∄ (IR TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
P TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (P TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV=0),
i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
SMT TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (SMT TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV=0),
i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
NMT TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (NMT TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (NMT TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV=0),
i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
OP TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (OP TRPNN TR 220/110 kV/kV i) ⟺ (n_TRPNN TR 220/110 kV/kV=0),
i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
SR TRPNN TR 400/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPNN TR 400/x kV/kV i GSS j) ⟺ (n_TRPNN TR 400/x kV/kV>0 ∧ n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPNN TR 400/x kV/kV i GSS j) ⟺ (n_TRPNN TR 400/x kV/kV=0 ∨ n_GSS x kV=0),
i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 400/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPNN TR 400/x kV/kV i PSS k) ⟺ (n_TRPNN TR 400/x kV/kV>0 ∧ n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPNN TR 400/x kV/kV i PSS k) ⟺ (n_TRPNN TR 400/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV>0 ∧ n_PSS x kV>0),
i=0 ⟹ ∄ (IR TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
P TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (P TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
SMT TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (SMT TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
NMT TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (NMT TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (NMT TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
OP TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (OP TRPNN TR 400/x kV/kV i) ⟺ (n_TRPNN TR 400/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
SR TRPNN TR 220/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPNN TR 220/x kV/kV i GSS j) ⟺ (n_TRPNN TR 220/x kV/kV>0 ∧ n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPNN TR 220/x kV/kV i GSS j) ⟺ (n_TRPNN TR 220/x kV/kV=0 ∨ n_GSS x kV=0),
i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 220/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPNN TR 220/x kV/kV i PSS k) ⟺ (n_TRPNN TR 220/x kV/kV>0 ∧ n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPNN TR 220/x kV/kV i PSS k) ⟺ (n_TRPNN TR 220/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (IR TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
P TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV>0 ∧ n_PSS x kV>0),
i=0 ⟹ ∄ (P TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
SMT TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (SMT TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
NMT TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (NMT TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (NMT TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
OP TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (OP TRPNN TR 220/x kV/kV i) ⟺ (n_TRPNN TR 220/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
SR TRPNN TR 110/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR TRPNN TR 110/x kV/kV i GSS j) ⟺ (n_TRPNN TR 110/x kV/kV>0 ∧ n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR TRPNN TR 110/x kV/kV i GSS j) ⟺ (n_TRPNN TR 110/x kV/kV=0 ∨ n_GSS x kV=0),
i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 110/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (SR TRPNN TR 110/x kV/kV i PSS k) ⟺ (n_TRPNN TR 110/x kV/kV>0 ∧ n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (SR TRPNN TR 110/x kV/kV i PSS k) ⟺ (n_TRPNN TR 110/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (IR TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV>0 ∧ n_PSS x kV>0),
i=0 ⟹ ∄ (IR TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
P TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (P TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (P TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
SMT TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (SMT TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (SMT TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
NMT TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (NMT TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (NMT TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
OP TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (OP TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (OP TRPNN TR 110/x kV/kV i) ⟺ (n_TRPNN TR 110/x kV/kV=0),
i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
SR GSP 400 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR GSP 400 kV i GSS j) ⟺ (n_GSP 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR GSP 400 kV i GSS j) ⟺ (n_GSP 400 kV=0),
i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, i∈{0} ⟺ n_GSP 400 kV=0, j∈{i,i+1} ⟺ n_GSP 400 kV>0, j∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
P GSP 400 kV i:
∀i (i≠0) ⟹ ∃ (P GSP 400 kV i) ⟺ (n_GSP 400 kV>0),
i=0 ⟹ ∄ (P GSP 400 kV i) ⟺ (n_GSP 400 kV=0),
i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, i∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
SMT GSP 400 kV i:
∀i (i≠0) ⟹ ∃ (SMT GSP 400 kV i) ⟺ (n_GSP 400 kV>0),
i=0 ⟹ ∄ (SMT GSP 400 kV i) ⟺ (n_GSP 400 kV=0),
i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, i∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
SR GSP 220 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR GSP 220 kV i GSS j) ⟺ (n_GSP 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR GSP 220 kV i GSS j) ⟺ (n_GSP 220 kV=0),
i∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, i∈{0} ⟺ n_GSP 220 kV=0, j∈{i,i+1} ⟺ n_GSP 220 kV>0, j∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
P GSP 220 kV i:
∀i (i≠0) ⟹ ∃ (P GSP 220 kV i) ⟺ (n_GSP 220 kV>0),
i=0 ⟹ ∄ (P GSP 220 kV i) ⟺ (n_GSP 220 kV=0),
i∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, i∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
SMT GSP 220 kV i:
∀i (i≠0) ⟹ ∃ (SMT GSP 220 kV i) ⟺ (n_GSP 220 kV>0),
i=0 ⟹ ∄ (SMT GSP 220 kV i) ⟺ (n_GSP 220 kV=0),
i∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, i∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
SR GSP 110 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR GSP 110 kV i GSS j) ⟺ (n_GSP 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR GSP 110 kV i GSS j) ⟺ (n_GSP 110 kV=0),
i∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, i∈{0} ⟺ n_GSP 110 kV=0, j∈{i,i+1} ⟺ n_GSP 110 kV>0, j∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
P GSP 110 kV i:
∀i (i≠0) ⟹ ∃ (P GSP 110 kV i) ⟺ (n_GSP 110 kV>0),
i=0 ⟹ ∄ (P GSP 110 kV i) ⟺ (n_GSP 110 kV=0),
i∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, i∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
SMT GSP 110 kV i:
∀i (i≠0) ⟹ ∃ (SMT GSP 110 kV i) ⟺ (n_GSP 110 kV>0),
i=0 ⟹ ∄ (SMT GSP 110 kV i) ⟺ (n_GSP 110 kV=0),
i∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, i∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
SR GSP x kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR GSP x kV i GSS j) ⟺ (n_GSP x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR GSP x kV i GSS j) ⟺ (n_GSP x kV=0),
i∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, i∈{0} ⟺ n_GSP x kV=0, j∈{i,i+1} ⟺ n_GSP x kV>0, j∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
P GSP x kV i:
∀i (i≠0) ⟹ ∃ (P GSP x kV i) ⟺ (n_GSP x kV>0),
i=0 ⟹ ∄ (P GSP x kV i) ⟺ (n_GSP x kV=0),
i∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, i∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
SMT GSP x kV i:
∀i (i≠0) ⟹ ∃ (SMT GSP x kV i) ⟺ (n_GSP x kV>0),
i=0 ⟹ ∄ (SMT GSP x kV i) ⟺ (n_GSP x kV=0),
i∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, i∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
SR PSP 400 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR PSP 400 kV i GSS j) ⟺ (n_PSP 400 kV>0 ∧ n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR PSP 400 kV i GSS j) ⟺ (n_PSP 400 kV=0 ∨ n_GSS 400 kV=0),
i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, i∈{0} ⟺ n_PSP 400 kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_PSP 400 kV, n_GSS 400 kV∈N0;
SR PSP 400 kV i PSS i:
∀i (i≠0) ⟹ ∃ (SR PSP 400 kV i PSS i) ⟺ (n_PSP 400 kV>0),
i=0 ⟹ ∄ (SR PSP 400 kV i PSS i) ⟺ (n_PSP 400 kV=0),
i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, i∈{0} ⟺ n_PSP 400 kV=0, 
n_PSP 400 kV∈N0;
P PSP 400 kV i:
∀i (i≠0) ⟹ ∃ (P PSP 400 kV i) ⟺ (n_PSP 400 kV>0),
i=0 ⟹ ∄ (P PSP 400 kV i) ⟺ (n_PSP 400 kV=0),
i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, i∈{0} ⟺ n_PSP 400 kV=0, 
n_PSP 400 kV∈N0;
SR PSP 220 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR PSP 220 kV i GSS j) ⟺ (n_PSP 220 kV>0 ∧ n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR PSP 220 kV i GSS j) ⟺ (n_PSP 220 kV=0 ∨ n_GSS 220 kV=0),
i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, i∈{0} ⟺ n_PSP 220 kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_PSP 220 kV, n_GSS 220 kV∈N0;
SR PSP 220 kV i PSS i:
∀i (i≠0) ⟹ ∃ (SR PSP 220 kV i PSS i) ⟺ (n_PSP 220 kV>0),
i=0 ⟹ ∄ (SR PSP 220 kV i PSS i) ⟺ (n_PSP 220 kV=0),
i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, i∈{0} ⟺ n_PSP 220 kV=0, 
n_PSP 220 kV∈N0;
P PSP 220 kV i:
∀i (i≠0) ⟹ ∃ (P PSP 220 kV i) ⟺ (n_PSP 220 kV>0),
i=0 ⟹ ∄ (P PSP 220 kV i) ⟺ (n_PSP 220 kV=0),
i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, i∈{0} ⟺ n_PSP 220 kV=0, 
n_PSP 220 kV∈N0;
SR PSP 110 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR PSP 110 kV i GSS j) ⟺ (n_PSP 110 kV>0 ∧ n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR PSP 110 kV i GSS j) ⟺ (n_PSP 110 kV=0 ∨ n_GSS 110 kV=0),
i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, i∈{0} ⟺ n_PSP 110 kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_PSP 110 kV, n_GSS 110 kV∈N0;
PSP 110 kV i PSS i:
∀i (i≠0) ⟹ ∃ (PSP 110 kV i PSS i) ⟺ (n_PSP 110 kV>0),
i=0 ⟹ ∄ (PSP 110 kV i PSS i) ⟺ (n_PSP 110 kV=0),
i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, i∈{0} ⟺ n_PSP 110 kV=0, 
n_PSP 110 kV∈N0;
P PSP 110 kV i:
∀i (i≠0) ⟹ ∃ (P PSP 110 kV i) ⟺ (n_PSP 110 kV>0),
i=0 ⟹ ∄ (P PSP 110 kV i) ⟺ (n_PSP 110 kV=0),
i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, i∈{0} ⟺ n_PSP 110 kV=0, 
n_PSP 110 kV∈N0;
SR PSP x kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (SR PSP x kV i GSS j) ⟺ (n_PSP x kV>0 ∧ n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (SR PSP x kV i GSS j) ⟺ (n_PSP x kV=0 ∨ n_GSS x kV=0),
i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, i∈{0} ⟺ n_PSP x kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_PSP x kV, n_GSS x kV∈N0;
PSP x kV i PSS i:
∀i (i≠0) ⟹ ∃ (PSP x kV i PSS i) ⟺ (n_PSP x kV>0),
i=0 ⟹ ∄ (PSP x kV i PSS i) ⟺ (n_PSP x kV=0),
i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, i∈{0} ⟺ n_PSP x kV=0, 
n_PSP x kV∈N0;
P PSP x kV i:
∀i (i≠0) ⟹ ∃ (P PSP x kV i) ⟺ (n_PSP x kV>0),
i=0 ⟹ ∄ (P PSP x kV i) ⟺ (n_PSP x kV=0),
i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, i∈{0} ⟺ n_PSP x kV=0, 
n_PSP x kV∈N0;
TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (TR 400/220 kV/kV i) ⟺ (n_TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (TR 400/220 kV/kV i) ⟺ (n_TR 400/220 kV/kV=0),
i∈{1, ..., n_TR 400/220 kV/kV} ⟺ n_TR 400/220 kV/kV>0, i∈{0} ⟺ n_TR 400/220 kV/kV=0, 
n_TR 400/220 kV/kV∈N0;
TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (TR 400/110 kV/kV i) ⟺ (n_TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (TR 400/110 kV/kV i) ⟺ (n_TR 400/110 kV/kV=0),
i∈{1, ..., n_TR 400/110 kV/kV} ⟺ n_TR 400/110 kV/kV>0, i∈{0} ⟺ n_TR 400/110 kV/kV=0, 
n_TR 400/110 kV/kV∈N0;
TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (TR 220/110 kV/kV i) ⟺ (n_TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (TR 220/110 kV/kV i) ⟺ (n_TR 220/110 kV/kV=0),
i∈{1, ..., n_TR 220/110 kV/kV} ⟺ n_TR 220/110 kV/kV>0, i∈{0} ⟺ n_TR 220/110 kV/kV=0, 
n_TR 220/110 kV/kV∈N0;
TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (TR 400/x kV/kV i) ⟺ (n_TR 400/x kV/kV>0),
i=0 ⟹ ∄ (TR 400/x kV/kV i) ⟺ (n_TR 400/x kV/kV=0),
i∈{1, ..., n_TR 400/x kV/kV} ⟺ n_TR 400/x kV/kV>0, i∈{0} ⟺ n_TR 400/x kV/kV=0, 
n_TR 400/x kV/kV∈N0;
TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (TR 220/x kV/kV i) ⟺ (n_TR 220/x kV/kV>0),
i=0 ⟹ ∄ (TR 220/x kV/kV i) ⟺ (n_TR 220/x kV/kV=0),
i∈{1, ..., n_TR 220/x kV/kV} ⟺ n_TR 220/x kV/kV>0, i∈{0} ⟺ n_TR 220/x kV/kV=0, 
n_TR 220/x kV/kV∈N0;
TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (TR 110/x kV/kV i) ⟺ (n_TR 110/x kV/kV>0),
i=0 ⟹ ∄ (TR 110/x kV/kV i) ⟺ (n_TR 110/x kV/kV=0),
i∈{1, ..., n_TR 110/x kV/kV} ⟺ n_TR 110/x kV/kV>0, i∈{0} ⟺ n_TR 110/x kV/kV=0, 
n_TR 110/x kV/kV∈N0;
GSS 400 kV i:
∀i (i≠0) ⟹ ∃ (GSS 400 kV i) ⟺ (n_GSS 400 kV>0),
i=0 ⟹ ∄ (GSS 400 kV i) ⟺ (n_GSS 400 kV=0),
i∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, i∈{0} ⟺ n_GSS 400 kV=0, 
n_GSS 400 kV∈N0;
NMT GSS 400 kV i:
∀i (i≠0) ⟹ ∃ (NMT GSS 400 kV i) ⟺ (n_GSS 400 kV>0),
i=0 ⟹ ∄ (NMT GSS 400 kV i) ⟺ (n_GSS 400 kV=0),
i∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, i∈{0} ⟺ n_GSS 400 kV=0, 
n_GSS 400 kV∈N0;
GSS 220 kV i:
∀i (i≠0) ⟹ ∃ (GSS 220 kV i) ⟺ (n_GSS 220 kV>0),
i=0 ⟹ ∄ (GSS 220 kV i) ⟺ (n_GSS 220 kV=0),
i∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, i∈{0} ⟺ n_GSS 220 kV=0, 
n_GSS 220 kV∈N0;
NMT GSS 220 kV i:
∀i (i≠0) ⟹ ∃ (NMT GSS 220 kV i) ⟺ (n_GSS 220 kV>0),
i=0 ⟹ ∄ (NMT GSS 220 kV i) ⟺ (n_GSS 220 kV=0),
i∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, i∈{0} ⟺ n_GSS 220 kV=0, 
n_GSS 220 kV∈N0;
GSS 110 kV i:
∀i (i≠0) ⟹ ∃ (GSS 110 kV i) ⟺ (n_GSS 110 kV>0),
i=0 ⟹ ∄ (GSS 110 kV i) ⟺ (n_GSS 110 kV=0),
i∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, i∈{0} ⟺ n_GSS 110 kV=0, 
n_GSS 110 kV∈N0;
NMT GSS 110 kV i:
∀i (i≠0) ⟹ ∃ (NMT GSS 110 kV i) ⟺ (n_GSS 110 kV>0),
i=0 ⟹ ∄ (NMT GSS 110 kV i) ⟺ (n_GSS 110 kV=0),
i∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, i∈{0} ⟺ n_GSS 110 kV=0, 
n_GSS 110 kV∈N0;
GSS x kV i:
∀i (i≠0) ⟹ ∃ (GSS x kV i) ⟺ (n_GSS x kV>0),
i=0 ⟹ ∄ (GSS x kV i) ⟺ (n_GSS x kV=0),
i∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, i∈{0} ⟺ n_GSS x kV=0, 
n_GSS x kV∈N0;
NMT GSS x kV i:
∀i (i≠0) ⟹ ∃ (NMT GSS x kV i) ⟺ (n_GSS x kV>0),
i=0 ⟹ ∄ (NMT GSS x kV i) ⟺ (n_GSS x kV=0),
i∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, i∈{0} ⟺ n_GSS x kV=0, 
n_GSS x kV∈N0;
PSS 400 kV i:
∀i (i≠0) ⟹ ∃ (PSS 400 kV i) ⟺ (n_PSS 400 kV>0),
i=0 ⟹ ∄ (PSS 400 kV i) ⟺ (n_PSS 400 kV=0),
i∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, i∈{0} ⟺ n_PSS 400 kV=0, 
n_PSS 400 kV∈N0;
PSS 220 kV i:
∀i (i≠0) ⟹ ∃ (PSS 220 kV i) ⟺ (n_PSS 220 kV>0),
i=0 ⟹ ∄ (PSS 220 kV i) ⟺ (n_PSS 220 kV=0),
i∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, i∈{0} ⟺ n_PSS 220 kV=0, 
n_PSS 220 kV∈N0;
PSS 110 kV i:
∀i (i≠0) ⟹ ∃ (PSS 110 kV i) ⟺ (n_PSS 110 kV>0),
i=0 ⟹ ∄ (PSS 110 kV i) ⟺ (n_PSS 110 kV=0),
i∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, i∈{0} ⟺ n_PSS 110 kV=0, 
n_PSS 110 kV∈N0;
PSS x kV i:
∀i (i≠0) ⟹ ∃ (PSS x kV i) ⟺ (n_PSS x kV>0),
i=0 ⟹ ∄ (PSS x kV i) ⟺ (n_PSS x kV=0),
i∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, i∈{0} ⟺ n_PSS x kV=0, 
n_PSS x kV∈N0;
Definisanje parametara za EEO
Lista parametara:
n_DVP 400 kV je broj DVP 400 kV,
n_DVP 220 kV je broj DVP 220 kV,
n_DVP 110 kV je broj DVP 110 kV,
n_DVP x kV je broj DVP x kV,
n_KBP 400 kV je broj KBP 400 kV,
n_KBP 220 kV je broj KBP 220 kV,
n_KBP 110 kV je broj KBP 110 kV,
n_KBP x kV je broj KBP x kV,
n_TRPVN TR 400/220 kV/kV je broj TRPVN TR 400/220 kV/kV,
n_TRPVN TR 400/110 kV/kV je broj TRPVN TR 400/110 kV/kV,
n_TRPVN TR 220/110 kV/kV je broj TRPVN TR 220/110 kV/kV,
n_TRPVN TR 400/x kV/kV je broj TRPVN TR 400/x kV/kV,
n_TRPVN TR 220/x kV/kV je broj TRPVN TR 220/x kV/kV,
n_TRPVN TR 110/x kV/kV je broj TRPVN TR 110/x kV/kV,
n_TRPNN TR 400/220 kV/kV je broj TRPNN TR 400/220 kV/kV,
n_TRPNN TR 400/110 kV/kV je broj TRPNN TR 400/110 kV/kV,
n_TRPNN TR 220/110 kV/kV je broj TRPNN TR 220/110 kV/kV,
n_TRPNN TR 400/x kV/kV je broj TRPNN TR 400/x kV/kV,
n_TRPNN TR 220/x kV/kV je broj TRPNN TR 220/x kV/kV,
n_TRPNN TR 110/x kV/kV je broj TRPNN TR 110/x kV/kV,
n_GSP 400 kV je broj GSP 400 kV,
n_GSP 220 kV je broj GSP 220 kV,
n_GSP 110 kV je broj GSP 110 kV,
n_GSP x kV je broj GSP x kV,
n_PSP 400 kV je broj PSP 400 kV,
n_PSP 220 kV je broj PSP 220 kV,
n_PSP 110 kV je broj PSP 110 kV,
n_PSP x kV je broj PSP x kV,
n_TR 400/220 kV/kV je broj TR 400/220 kV/kV,
n_TR 400/110 kV/kV je broj TR 400/110 kV/kV,
n_TR 220/110 kV/kV je broj TR 220/110 kV/kV,
n_TR 400/x kV/kV je broj TR 400/x kV/kV,
n_TR 220/x kV/kV je broj TR 220/x kV/kV,
n_TR 110/x kV/kV je broj TR 110/x kV/kV,
n_GSS 400 kV je broj GSS sa pripadajućom opremom 400 kV,
n_GSS 220 kV je broj GSS sa pripadajućom opremom 220 kV,
n_GSS 110 kV je broj GSS sa pripadajućom opremom 110 kV,
n_GSS x kV je broj GSS sa pripadajućom opremom x kV,
n_PSS 400 kV je broj PSS 400 kV,
n_PSS 220 kV je broj PSS 220 kV,
n_PSS 110 kV je broj PSS 110 kV,
n_PSS x kV je broj PSS x kV.
x-ti EEO
PS se sastoji od minimum dva EEO koji su međusobno na određen način povezani vodovima. x-ti EEO definišemo kao element niza:
EEO x, gde x∈{1, ..., n_EEO} za n_EEO>1, n_EEO∈N.
Osnovni elementi za x-ti EEO
Osnovni elementi se definišu za svaki x-ti EEO x, gde x∈{1, ..., n_EEO} za n_EEO>1, n_EEO∈N.
Osnovni elementi za EEO x sa definisanim postojanjem su:
EEO x SR DVP 400 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR DVP 400 kV i GSS j) ⟺ (EEO x n_DVP 400 kV>0 ∧ EEO x n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR DVP 400 kV i GSS j) ⟺ (EEO x n_DVP 400 kV=0 ∨ EEO x n_GSS 400 kV=0),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x SR DVP 400 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR DVP 400 kV i PSS k) ⟺ (EEO x n_DVP 400 kV>0 ∧ EEO x n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR DVP 400 kV i PSS k) ⟺ (EEO x n_DVP 400 kV=0 ∨ EEO x n_PSS 400 kV=0),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x P DVP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P DVP 400 kV i) ⟺ (EEO x n_DVP 400 kV>0),
i=0 ⟹ ∄ (EEO x P DVP 400 kV i) ⟺ (EEO x n_DVP 400 kV=0),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x IRSU DVP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x IRSU DVP 400 kV i) ⟺ (EEO x n_DVP 400 kV>0),
i=0 ⟹ ∄ (EEO x IRSU DVP 400 kV i) ⟺ (EEO x n_DVP 400 kV=0),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x SMT DVP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT DVP 400 kV i) ⟺ (EEO x n_DVP 400 kV>0),
i=0 ⟹ ∄ (EEO x SMT DVP 400 kV i) ⟺ (EEO x n_DVP 400 kV=0),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x NMT DVP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT DVP 400 kV i) ⟺ (EEO x n_DVP 400 kV>0),
i=0 ⟹ ∄ (EEO x NMT DVP 400 kV i) ⟺ (EEO x n_DVP 400 kV=0),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x SR DVP 220 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR DVP 220 kV i GSS j) ⟺ (EEO x n_DVP 220 kV>0 ∧ EEO x n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR DVP 220 kV i GSS j) ⟺ (EEO x n_DVP 220 kV=0 ∨ EEO x n_GSS 220 kV=0),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x SR DVP 220 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR DVP 220 kV i PSS k) ⟺ (EEO x n_DVP 220 kV>0 ∧ EEO x n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR DVP 220 kV i PSS k) ⟺ (EEO x n_DVP 220 kV=0 ∨ EEO x n_PSS 220 kV=0),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x P DVP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P DVP 220 kV i) ⟺ (EEO x n_DVP 220 kV>0),
i=0 ⟹ ∄ (EEO x P DVP 220 kV i) ⟺ (EEO x n_DVP 220 kV=0),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x IRSU DVP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x IRSU DVP 220 kV i) ⟺ (EEO x n_DVP 220 kV>0),
i=0 ⟹ ∄ (EEO x IRSU DVP 220 kV i) ⟺ (EEO x n_DVP 220 kV=0),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x SMT DVP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT DVP 220 kV i) ⟺ (EEO x n_DVP 220 kV>0),
i=0 ⟹ ∄ (EEO x SMT DVP 220 kV i) ⟺ (EEO x n_DVP 220 kV=0),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x NMT DVP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT DVP 220 kV i) ⟺ (EEO x n_DVP 220 kV>0),
i=0 ⟹ ∄ (EEO x NMT DVP 220 kV i) ⟺ (EEO x n_DVP 220 kV=0),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x SR DVP 110 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR DVP 110 kV i GSS j) ⟺ (EEO x n_DVP 110 kV>0 ∧ EEO x n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR DVP 110 kV i GSS j) ⟺ (EEO x n_DVP 110 kV=0 ∨ EEO x n_GSS 110 kV=0),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x SR DVP 110 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR DVP 110 kV i PSS k) ⟺ (EEO x n_DVP 110 kV>0 ∧ EEO x n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR DVP 110 kV i PSS k) ⟺ (EEO x n_DVP 110 kV=0 ∨ EEO x n_PSS 110 kV=0),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x P DVP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P DVP 110 kV i) ⟺ (EEO x n_DVP 110 kV>0),
i=0 ⟹ ∄ (EEO x P DVP 110 kV i) ⟺ (EEO x n_DVP 110 kV=0),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x IRSU DVP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x IRSU DVP 110 kV i) ⟺ (EEO x n_DVP 110 kV>0),
i=0 ⟹ ∄ (EEO x IRSU DVP 110 kV i) ⟺ (EEO x n_DVP 110 kV=0),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x SMT DVP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT DVP 110 kV i) ⟺ (EEO x n_DVP 110 kV>0),
i=0 ⟹ ∄ (EEO x SMT DVP 110 kV i) ⟺ (EEO x n_DVP 110 kV=0),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x NMT DVP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT DVP 110 kV i) ⟺ (EEO x n_DVP 110 kV>0),
i=0 ⟹ ∄ (EEO x NMT DVP 110 kV i) ⟺ (EEO x n_DVP 110 kV=0),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x SR DVP x kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR DVP x kV i GSS j) ⟺ (EEO x n_DVP x kV>0 ∧ EEO x n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR DVP x kV i GSS j) ⟺ (EEO x n_DVP x kV=0 ∨ EEO x n_GSS x kV=0),
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_DVP x kV, EEO x n_GSS x kV∈N0;
EEO x SR DVP x kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR DVP x kV i PSS k) ⟺ (EEO x n_DVP x kV>0 ∧ EEO x n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR DVP x kV i PSS k) ⟺ (EEO x n_DVP x kV=0 ∨ EEO x n_PSS x kV=0),
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_DVP x kV, EEO x n_PSS x kV∈N0;
EEO x P DVP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x P DVP x kV i) ⟺ (EEO x n_DVP x kV>0),
i=0 ⟹ ∄ (EEO x P DVP x kV i) ⟺ (EEO x n_DVP x kV=0),
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x IRSU DVP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x IRSU DVP x kV i) ⟺ (EEO x n_DVP x kV>0),
i=0 ⟹ ∄ (EEO x IRSU DVP x kV i) ⟺ (EEO x n_DVP x kV=0),
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x SMT DVP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT DVP x kV i) ⟺ (EEO x n_DVP x kV>0),
i=0 ⟹ ∄ (EEO x SMT DVP x kV i) ⟺ (EEO x n_DVP x kV=0),
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x NMT DVP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT DVP x kV i) ⟺ (EEO x n_DVP x kV>0),
i=0 ⟹ ∄ (EEO x NMT DVP x kV i) ⟺ (EEO x n_DVP x kV=0),
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x SR KBP 400 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR KBP 400 kV i GSS j) ⟺ (EEO x n_KBP 400 kV>0 ∧ EEO x n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR KBP 400 kV i GSS j) ⟺ (EEO x n_KBP 400 kV=0 ∨ EEO x n_GSS 400 kV=0),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x SR KBP 400 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR KBP 400 kV i PSS k) ⟺ (EEO x n_KBP 400 kV>0 ∧ EEO x n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR KBP 400 kV i PSS k) ⟺ (EEO x n_KBP 400 kV=0 ∨ EEO x n_PSS 400 kV=0),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x P KBP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P KBP 400 kV i) ⟺ (EEO x n_KBP 400 kV>0),
i=0 ⟹ ∄ (EEO x P KBP 400 kV i) ⟺ (EEO x n_KBP 400 kV=0),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x IRSU KBP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x IRSU KBP 400 kV i) ⟺ (EEO x n_KBP 400 kV>0),
i=0 ⟹ ∄ (EEO x IRSU KBP 400 kV i) ⟺ (EEO x n_KBP 400 kV=0),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x SMT KBP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT KBP 400 kV i) ⟺ (EEO x n_KBP 400 kV>0),
i=0 ⟹ ∄ (EEO x SMT KBP 400 kV i) ⟺ (EEO x n_KBP 400 kV=0),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x NMT KBP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT KBP 400 kV i) ⟺ (EEO x n_KBP 400 kV>0),
i=0 ⟹ ∄ (EEO x NMT KBP 400 kV i) ⟺ (EEO x n_KBP 400 kV=0),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x SR KBP 220 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR KBP 220 kV i GSS j) ⟺ (EEO x n_KBP 220 kV>0 ∧ EEO x n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR KBP 220 kV i GSS j) ⟺ (EEO x n_KBP 220 kV=0 ∨ EEO x n_GSS 220 kV=0),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x SR KBP 220 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR KBP 220 kV i PSS k) ⟺ (EEO x n_KBP 220 kV>0 ∧ EEO x n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR KBP 220 kV i PSS k) ⟺ (EEO x n_KBP 220 kV=0 ∨ EEO x n_PSS 220 kV=0),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x P KBP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P KBP 220 kV i) ⟺ (EEO x n_KBP 220 kV>0),
i=0 ⟹ ∄ (EEO x P KBP 220 kV i) ⟺ (EEO x n_KBP 220 kV=0),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x IRSU KBP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x IRSU KBP 220 kV i) ⟺ (EEO x n_KBP 220 kV>0),
i=0 ⟹ ∄ (EEO x IRSU KBP 220 kV i) ⟺ (EEO x n_KBP 220 kV=0),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x SMT KBP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT KBP 220 kV i) ⟺ (EEO x n_KBP 220 kV>0),
i=0 ⟹ ∄ (EEO x SMT KBP 220 kV i) ⟺ (EEO x n_KBP 220 kV=0),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x NMT KBP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT KBP 220 kV i) ⟺ (EEO x n_KBP 220 kV>0),
i=0 ⟹ ∄ (EEO x NMT KBP 220 kV i) ⟺ (EEO x n_KBP 220 kV=0),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x SR KBP 110 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR KBP 110 kV i GSS j) ⟺ (EEO x n_KBP 110 kV>0 ∧ EEO x n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR KBP 110 kV i GSS j) ⟺ (EEO x n_KBP 110 kV=0 ∨ EEO x n_GSS 110 kV=0),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x SR KBP 110 kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR KBP 110 kV i PSS k) ⟺ (EEO x n_KBP 110 kV>0 ∧ EEO x n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR KBP 110 kV i PSS k) ⟺ (EEO x n_KBP 110 kV=0 ∨ EEO x n_PSS 110 kV=0),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x P KBP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P KBP 110 kV i) ⟺ (EEO x n_KBP 110 kV>0),
i=0 ⟹ ∄ (EEO x P KBP 110 kV i) ⟺ (EEO x n_KBP 110 kV=0),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x IRSU KBP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x IRSU KBP 110 kV i) ⟺ (EEO x n_KBP 110 kV>0),
i=0 ⟹ ∄ (EEO x IRSU KBP 110 kV i) ⟺ (EEO x n_KBP 110 kV=0),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x SMT KBP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT KBP 110 kV i) ⟺ (EEO x n_KBP 110 kV>0),
i=0 ⟹ ∄ (EEO x SMT KBP 110 kV i) ⟺ (EEO x n_KBP 110 kV=0),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x NMT KBP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT KBP 110 kV i) ⟺ (EEO x n_KBP 110 kV>0),
i=0 ⟹ ∄ (EEO x NMT KBP 110 kV i) ⟺ (EEO x n_KBP 110 kV=0),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x SR KBP x kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR KBP x kV i GSS j) ⟺ (EEO x n_KBP x kV>0 ∧ EEO x n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR KBP x kV i GSS j) ⟺ (EEO x n_KBP x kV=0 ∨ EEO x n_GSS x kV=0),
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_KBP x kV, EEO x n_GSS x kV∈N0;
EEO x SR KBP x kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR KBP x kV i PSS k) ⟺ (EEO x n_KBP x kV>0 ∧ EEO x n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR KBP x kV i PSS k) ⟺ (EEO x n_KBP x kV=0 ∨ EEO x n_PSS x kV=0),
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_KBP x kV, EEO x n_PSS x kV∈N0;
EEO x P KBP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x P KBP x kV i) ⟺ (EEO x n_KBP x kV>0),
i=0 ⟹ ∄ (EEO x P KBP x kV i) ⟺ (EEO x n_KBP x kV=0),
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x IRSU KBP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x IRSU KBP x kV i) ⟺ (EEO x n_KBP x kV>0),
i=0 ⟹ ∄ (EEO x IRSU KBP x kV i) ⟺ (EEO x n_KBP x kV=0),
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x SMT KBP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT KBP x kV i) ⟺ (EEO x n_KBP x kV>0),
i=0 ⟹ ∄ (EEO x SMT KBP x kV i) ⟺ (EEO x n_KBP x kV=0),
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x NMT KBP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT KBP x kV i) ⟺ (EEO x n_KBP x kV>0),
i=0 ⟹ ∄ (EEO x NMT KBP x kV i) ⟺ (EEO x n_KBP x kV=0),
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x SR TRPVN TR 400/220 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPVN TR 400/220 kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV>0 ∧ EEO x n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPVN TR 400/220 kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV=0 ∨ EEO x n_GSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SR TRPVN TR 400/220 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPVN TR 400/220 kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV>0 ∧ EEO x n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPVN TR 400/220 kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV=0 ∨ EEO x n_PSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x IR TRPVN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPVN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV>0 ∧ n_PSS 400 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPVN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x P TRPVN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPVN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPVN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x SMT TRPVN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPVN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPVN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x OP TRPVN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPVN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPVN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/220 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x SR TRPVN TR 400/110 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPVN TR 400/110 kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV>0 ∧ EEO x n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPVN TR 400/110 kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV=0 ∨ EEO x n_GSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SR TRPVN TR 400/110 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPVN TR 400/110 kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV>0 ∧ EEO x n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPVN TR 400/110 kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV=0 ∨ EEO x n_PSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x IR TRPVN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPVN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV>0 ∧ n_PSS 400 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPVN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x P TRPVN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPVN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPVN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x SMT TRPVN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPVN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPVN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x OP TRPVN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPVN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPVN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 400/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x SR TRPVN TR 220/110 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPVN TR 220/110 kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV>0 ∧ EEO x n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPVN TR 220/110 kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV=0 ∨ EEO x n_GSS 220 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SR TRPVN TR 220/110 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPVN TR 220/110 kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV>0 ∧ EEO x n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPVN TR 220/110 kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV=0 ∨ EEO x n_PSS 220 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x IR TRPVN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPVN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV>0 ∧ n_PSS 220 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPVN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x P TRPVN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPVN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPVN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x SMT TRPVN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPVN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPVN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x OP TRPVN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPVN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPVN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPVN TR 220/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x SR TRPVN TR 400/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPVN TR 400/x kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 400/x kV/kV>0 ∧ EEO x n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPVN TR 400/x kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 400/x kV/kV=0 ∨ EEO x n_GSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/x kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SR TRPVN TR 400/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPVN TR 400/x kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 400/x kV/kV>0 ∧ EEO x n_PSS 400 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPVN TR 400/x kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 400/x kV/kV=0 ∨ EEO x n_PSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/x kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x IR TRPVN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPVN TR 400/x kV/kV i) ⟺ (EEO x n_TRPVN TR 400/x kV/kV>0 ∧ n_PSS 400 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPVN TR 400/x kV/kV i) ⟺ (EEO x n_TRPVN TR 400/x kV/kV=0 ∨ n_PSS 400 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x P TRPVN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPVN TR 400/x kV/kV i) ⟺ (EEO x n_TRPVN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPVN TR 400/x kV/kV i) ⟺ (EEO x n_TRPVN TR 400/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x SMT TRPVN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPVN TR 400/x kV/kV i) ⟺ (EEO x n_TRPVN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPVN TR 400/x kV/kV i) ⟺ (EEO x n_TRPVN TR 400/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x OP TRPVN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPVN TR 400/x kV/kV i) ⟺ (EEO x n_TRPVN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPVN TR 400/x kV/kV i) ⟺ (EEO x n_TRPVN TR 400/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x SR TRPVN TR 220/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPVN TR 220/x kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 220/x kV/kV>0 ∧ EEO x n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPVN TR 220/x kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 220/x kV/kV=0 ∨ EEO x n_GSS 220 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/x kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SR TRPVN TR 220/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPVN TR 220/x kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 220/x kV/kV>0 ∧ EEO x n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPVN TR 220/x kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 220/x kV/kV=0 ∨ EEO x n_PSS 220 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPVN TR 220/x kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x IR TRPVN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPVN TR 220/x kV/kV i) ⟺ (EEO x n_TRPVN TR 220/x kV/kV>0 ∧ n_PSS 220 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPVN TR 220/x kV/kV i) ⟺ (EEO x n_TRPVN TR 220/x kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x P TRPVN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPVN TR 220/x kV/kV i) ⟺ (EEO x n_TRPVN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPVN TR 220/x kV/kV i) ⟺ (EEO x n_TRPVN TR 220/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x SMT TRPVN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPVN TR 220/x kV/kV i) ⟺ (EEO x n_TRPVN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPVN TR 220/x kV/kV i) ⟺ (EEO x n_TRPVN TR 220/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x OP TRPVN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPVN TR 220/x kV/kV i) ⟺ (EEO x n_TRPVN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPVN TR 220/x kV/kV i) ⟺ (EEO x n_TRPVN TR 220/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x SR TRPVN TR 110/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPVN TR 110/x kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 110/x kV/kV>0 ∧ EEO x n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPVN TR 110/x kV/kV i GSS j) ⟺ (EEO x n_TRPVN TR 110/x kV/kV=0 ∨ EEO x n_GSS 110 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPVN TR 110/x kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SR TRPVN TR 110/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPVN TR 110/x kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 110/x kV/kV>0 ∧ EEO x n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPVN TR 110/x kV/kV i PSS k) ⟺ (EEO x n_TRPVN TR 110/x kV/kV=0 ∨ EEO x n_PSS 110 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPVN TR 110/x kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x IR TRPVN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPVN TR 110/x kV/kV i) ⟺ (EEO x n_TRPVN TR 110/x kV/kV>0 ∧ n_PSS 110 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPVN TR 110/x kV/kV i) ⟺ (EEO x n_TRPVN TR 110/x kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x P TRPVN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPVN TR 110/x kV/kV i) ⟺ (EEO x n_TRPVN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPVN TR 110/x kV/kV i) ⟺ (EEO x n_TRPVN TR 110/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x SMT TRPVN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPVN TR 110/x kV/kV i) ⟺ (EEO x n_TRPVN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPVN TR 110/x kV/kV i) ⟺ (EEO x n_TRPVN TR 110/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x OP TRPVN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPVN TR 110/x kV/kV i) ⟺ (EEO x n_TRPVN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPVN TR 110/x kV/kV i) ⟺ (EEO x n_TRPVN TR 110/x kV/kV=0),
i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x SR TRPNN TR 400/220 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPNN TR 400/220 kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV>0 ∧ EEO x n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPNN TR 400/220 kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV=0 ∨ EEO x n_GSS 220 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SR TRPNN TR 400/220 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPNN TR 400/220 kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV>0 ∧ EEO x n_PSS 220 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPNN TR 400/220 kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV=0 ∨ EEO x n_PSS 220 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x IR TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV>0 ∧ n_PSS 220 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV=0 ∨ n_PSS 220 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x P TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x SMT TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x NMT TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (EEO x NMT TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x OP TRPNN TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPNN TR 400/220 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/220 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x SR TRPNN TR 400/110 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPNN TR 400/110 kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV>0 ∧ EEO x n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPNN TR 400/110 kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV=0 ∨ EEO x n_GSS 110 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SR TRPNN TR 400/110 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPNN TR 400/110 kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV>0 ∧ EEO x n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPNN TR 400/110 kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV=0 ∨ EEO x n_PSS 110 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x IR TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV>0 ∧ n_PSS 110 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x P TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x SMT TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x NMT TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x NMT TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x OP TRPNN TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPNN TR 400/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 400/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x SR TRPNN TR 220/110 kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPNN TR 220/110 kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV>0 ∧ EEO x n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPNN TR 220/110 kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV=0 ∨ EEO x n_GSS 110 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SR TRPNN TR 220/110 kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPNN TR 220/110 kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV>0 ∧ EEO x n_PSS 110 kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPNN TR 220/110 kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV=0 ∨ EEO x n_PSS 110 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x IR TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV>0 ∧ n_PSS 110 kV>0),
i=0 ⟹ ∄ (EEO x IR TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV=0 ∨ n_PSS 110 kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x P TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x SMT TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x NMT TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x NMT TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x OP TRPNN TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPNN TR 220/110 kV/kV i) ⟺ (EEO x n_TRPNN TR 220/110 kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x SR TRPNN TR 400/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPNN TR 400/x kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 400/x kV/kV>0 ∧ EEO x n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPNN TR 400/x kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 400/x kV/kV=0 ∨ EEO x n_GSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SR TRPNN TR 400/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPNN TR 400/x kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 400/x kV/kV>0 ∧ EEO x n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPNN TR 400/x kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 400/x kV/kV=0 ∨ EEO x n_PSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV>0 ∧ n_PSS x kV>0),
i=0 ⟹ ∄ (EEO x IR TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x P TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x SMT TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x NMT TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (EEO x NMT TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x OP TRPNN TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPNN TR 400/x kV/kV i) ⟺ (EEO x n_TRPNN TR 400/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x SR TRPNN TR 220/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPNN TR 220/x kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 220/x kV/kV>0 ∧ EEO x n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPNN TR 220/x kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 220/x kV/kV=0 ∨ EEO x n_GSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SR TRPNN TR 220/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPNN TR 220/x kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 220/x kV/kV>0 ∧ EEO x n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPNN TR 220/x kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 220/x kV/kV=0 ∨ EEO x n_PSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (EEO x IR TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x P TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV>0 ∧ n_PSS x kV>0),
i=0 ⟹ ∄ (EEO x P TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x SMT TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x NMT TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (EEO x NMT TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x OP TRPNN TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPNN TR 220/x kV/kV i) ⟺ (EEO x n_TRPNN TR 220/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x SR TRPNN TR 110/x kV/kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR TRPNN TR 110/x kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 110/x kV/kV>0 ∧ EEO x n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR TRPNN TR 110/x kV/kV i GSS j) ⟺ (EEO x n_TRPNN TR 110/x kV/kV=0 ∨ EEO x n_GSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SR TRPNN TR 110/x kV/kV i PSS k:
∀i, k (i≠0 ∧ k≠0) ⟹ ∃ (EEO x SR TRPNN TR 110/x kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 110/x kV/kV>0 ∧ EEO x n_PSS x kV>0),
∀i, k (i=0 ∨ k=0) ⟹ ∄ (EEO x SR TRPNN TR 110/x kV/kV i PSS k) ⟺ (EEO x n_TRPNN TR 110/x kV/kV=0 ∨ EEO x n_PSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x IR TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV>0 ∧ n_PSS x kV>0),
i=0 ⟹ ∄ (EEO x IR TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV=0 ∨ n_PSS x kV=0),
i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x P TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x P TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (EEO x P TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x SMT TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (EEO x SMT TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x NMT TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (EEO x NMT TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x OP TRPNN TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x OP TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV>0),
i=0 ⟹ ∄ (EEO x OP TRPNN TR 110/x kV/kV i) ⟺ (EEO x n_TRPNN TR 110/x kV/kV=0),
i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x SR GSP 400 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR GSP 400 kV i GSS j) ⟺ (EEO x n_GSP 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR GSP 400 kV i GSS j) ⟺ (EEO x n_GSP 400 kV=0),
i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, i∈{0} ⟺ EEO x n_GSP 400 kV=0, j∈{i,i+1} ⟺ EEO x n_GSP 400 kV>0, j∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x P GSP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P GSP 400 kV i) ⟺ (EEO x n_GSP 400 kV>0),
i=0 ⟹ ∄ (EEO x P GSP 400 kV i) ⟺ (EEO x n_GSP 400 kV=0),
i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, i∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x SMT GSP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT GSP 400 kV i) ⟺ (EEO x n_GSP 400 kV>0),
i=0 ⟹ ∄ (EEO x SMT GSP 400 kV i) ⟺ (EEO x n_GSP 400 kV=0),
i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, i∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x SR GSP 220 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR GSP 220 kV i GSS j) ⟺ (EEO x n_GSP 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR GSP 220 kV i GSS j) ⟺ (EEO x n_GSP 220 kV=0),
i∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, i∈{0} ⟺ EEO x n_GSP 220 kV=0, j∈{i,i+1} ⟺ EEO x n_GSP 220 kV>0, j∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x P GSP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P GSP 220 kV i) ⟺ (EEO x n_GSP 220 kV>0),
i=0 ⟹ ∄ (EEO x P GSP 220 kV i) ⟺ (EEO x n_GSP 220 kV=0),
i∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, i∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x SMT GSP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT GSP 220 kV i) ⟺ (EEO x n_GSP 220 kV>0),
i=0 ⟹ ∄ (EEO x SMT GSP 220 kV i) ⟺ (EEO x n_GSP 220 kV=0),
i∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, i∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x SR GSP 110 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR GSP 110 kV i GSS j) ⟺ (EEO x n_GSP 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR GSP 110 kV i GSS j) ⟺ (EEO x n_GSP 110 kV=0),
i∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, i∈{0} ⟺ EEO x n_GSP 110 kV=0, j∈{i,i+1} ⟺ EEO x n_GSP 110 kV>0, j∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x P GSP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P GSP 110 kV i) ⟺ (EEO x n_GSP 110 kV>0),
i=0 ⟹ ∄ (EEO x P GSP 110 kV i) ⟺ (EEO x n_GSP 110 kV=0),
i∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, i∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x SMT GSP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT GSP 110 kV i) ⟺ (EEO x n_GSP 110 kV>0),
i=0 ⟹ ∄ (EEO x SMT GSP 110 kV i) ⟺ (EEO x n_GSP 110 kV=0),
i∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, i∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x SR GSP x kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR GSP x kV i GSS j) ⟺ (EEO x n_GSP x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR GSP x kV i GSS j) ⟺ (EEO x n_GSP x kV=0),
i∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, i∈{0} ⟺ EEO x n_GSP x kV=0, j∈{i,i+1} ⟺ EEO x n_GSP x kV>0, j∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x P GSP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x P GSP x kV i) ⟺ (EEO x n_GSP x kV>0),
i=0 ⟹ ∄ (EEO x P GSP x kV i) ⟺ (EEO x n_GSP x kV=0),
i∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, i∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x SMT GSP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x SMT GSP x kV i) ⟺ (EEO x n_GSP x kV>0),
i=0 ⟹ ∄ (EEO x SMT GSP x kV i) ⟺ (EEO x n_GSP x kV=0),
i∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, i∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x SR PSP 400 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR PSP 400 kV i GSS j) ⟺ (EEO x n_PSP 400 kV>0 ∧ EEO x n_GSS 400 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR PSP 400 kV i GSS j) ⟺ (EEO x n_PSP 400 kV=0 ∨ EEO x n_GSS 400 kV=0),
i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, i∈{0} ⟺ EEO x n_PSP 400 kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, EEO x n_PSP 400 kV, 
EEO x n_GSS 400 kV∈N0;
EEO x SR PSP 400 kV i PSS i:
∀i (i≠0) ⟹ ∃ (EEO x SR PSP 400 kV i PSS i) ⟺ (EEO x n_PSP 400 kV>0),
i=0 ⟹ ∄ (EEO x SR PSP 400 kV i PSS i) ⟺ (EEO x n_PSP 400 kV=0),
i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, i∈{0} ⟺ EEO x n_PSP 400 kV=0, 
EEO x n_PSP 400 kV∈N0;
EEO x P PSP 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P PSP 400 kV i) ⟺ (EEO x n_PSP 400 kV>0),
i=0 ⟹ ∄ (EEO x P PSP 400 kV i) ⟺ (EEO x n_PSP 400 kV=0),
i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, i∈{0} ⟺ EEO x n_PSP 400 kV=0, 
EEO x n_PSP 400 kV∈N0;
EEO x SR PSP 220 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR PSP 220 kV i GSS j) ⟺ (EEO x n_PSP 220 kV>0 ∧ EEO x n_GSS 220 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR PSP 220 kV i GSS j) ⟺ (EEO x n_PSP 220 kV=0 ∨ EEO x n_GSS 220 kV=0),
i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, i∈{0} ⟺ EEO x n_PSP 220 kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, EEO x n_PSP 220 kV, 
EEO x n_GSS 220 kV∈N0;
EEO x SR PSP 220 kV i PSS i:
∀i (i≠0) ⟹ ∃ (EEO x SR PSP 220 kV i PSS i) ⟺ (EEO x n_PSP 220 kV>0),
i=0 ⟹ ∄ (EEO x SR PSP 220 kV i PSS i) ⟺ (EEO x n_PSP 220 kV=0),
i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, i∈{0} ⟺ EEO x n_PSP 220 kV=0, 
EEO x n_PSP 220 kV∈N0;
EEO x P PSP 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P PSP 220 kV i) ⟺ (EEO x n_PSP 220 kV>0),
i=0 ⟹ ∄ (EEO x P PSP 220 kV i) ⟺ (EEO x n_PSP 220 kV=0),
i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, i∈{0} ⟺ EEO x n_PSP 220 kV=0, 
EEO x n_PSP 220 kV∈N0;
EEO x SR PSP 110 kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR PSP 110 kV i GSS j) ⟺ (EEO x n_PSP 110 kV>0 ∧ EEO x n_GSS 110 kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR PSP 110 kV i GSS j) ⟺ (EEO x n_PSP 110 kV=0 ∨ EEO x n_GSS 110 kV=0),
i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, i∈{0} ⟺ EEO x n_PSP 110 kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, EEO x n_PSP 110 kV, 
EEO x n_GSS 110 kV∈N0;
EEO x PSP 110 kV i PSS i:
∀i (i≠0) ⟹ ∃ (EEO x PSP 110 kV i PSS i) ⟺ (EEO x n_PSP 110 kV>0),
i=0 ⟹ ∄ (EEO x PSP 110 kV i PSS i) ⟺ (EEO x n_PSP 110 kV=0),
i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, i∈{0} ⟺ EEO x n_PSP 110 kV=0, 
EEO x n_PSP 110 kV∈N0;
EEO x P PSP 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x P PSP 110 kV i) ⟺ (EEO x n_PSP 110 kV>0),
i=0 ⟹ ∄ (EEO x P PSP 110 kV i) ⟺ (EEO x n_PSP 110 kV=0),
i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, i∈{0} ⟺ EEO x n_PSP 110 kV=0, 
EEO x n_PSP 110 kV∈N0;
EEO x SR PSP x kV i GSS j:
∀i, j (i≠0 ∧ j≠0) ⟹ ∃ (EEO x SR PSP x kV i GSS j) ⟺ (EEO x n_PSP x kV>0 ∧ EEO x n_GSS x kV>0),
∀i, j (i=0 ∨ j=0) ⟹ ∄ (EEO x SR PSP x kV i GSS j) ⟺ (EEO x n_PSP x kV=0 ∨ EEO x n_GSS x kV=0),
i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, i∈{0} ⟺ EEO x n_PSP x kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, EEO x n_PSP x kV, 
EEO x n_GSS x kV∈N0;
EEO x PSP x kV i PSS i:
∀i (i≠0) ⟹ ∃ (EEO x PSP x kV i PSS i) ⟺ (EEO x n_PSP x kV>0),
i=0 ⟹ ∄ (EEO x PSP x kV i PSS i) ⟺ (EEO x n_PSP x kV=0),
i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, i∈{0} ⟺ EEO x n_PSP x kV=0, 
EEO x n_PSP x kV∈N0;
EEO x P PSP x kV i:
∀i (i≠0) ⟹ ∃ (EEO x P PSP x kV i) ⟺ (EEO x n_PSP x kV>0),
i=0 ⟹ ∄ (EEO x P PSP x kV i) ⟺ (EEO x n_PSP x kV=0),
i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, i∈{0} ⟺ EEO x n_PSP x kV=0, 
EEO x n_PSP x kV∈N0;
EEO x TR 400/220 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x TR 400/220 kV/kV i) ⟺ (EEO x n_TR 400/220 kV/kV>0),
i=0 ⟹ ∄ (EEO x TR 400/220 kV/kV i) ⟺ (EEO x n_TR 400/220 kV/kV=0),
i∈{1, ..., EEO x n_TR 400/220 kV/kV} ⟺ EEO x n_TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TR 400/220 kV/kV=0, 
EEO x n_TR 400/220 kV/kV∈N0;
EEO x TR 400/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x TR 400/110 kV/kV i) ⟺ (EEO x n_TR 400/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x TR 400/110 kV/kV i) ⟺ (EEO x n_TR 400/110 kV/kV=0),
i∈{1, ..., EEO x n_TR 400/110 kV/kV} ⟺ EEO x n_TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TR 400/110 kV/kV=0, 
EEO x n_TR 400/110 kV/kV∈N0;
EEO x TR 220/110 kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x TR 220/110 kV/kV i) ⟺ (EEO x n_TR 220/110 kV/kV>0),
i=0 ⟹ ∄ (EEO x TR 220/110 kV/kV i) ⟺ (EEO x n_TR 220/110 kV/kV=0),
i∈{1, ..., EEO x n_TR 220/110 kV/kV} ⟺ EEO x n_TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TR 220/110 kV/kV=0, 
EEO x n_TR 220/110 kV/kV∈N0;
EEO x TR 400/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x TR 400/x kV/kV i) ⟺ (EEO x n_TR 400/x kV/kV>0),
i=0 ⟹ ∄ (EEO x TR 400/x kV/kV i) ⟺ (EEO x n_TR 400/x kV/kV=0),
i∈{1, ..., EEO x n_TR 400/x kV/kV} ⟺ EEO x n_TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TR 400/x kV/kV=0, 
EEO x n_TR 400/x kV/kV∈N0;
EEO x TR 220/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x TR 220/x kV/kV i) ⟺ (EEO x n_TR 220/x kV/kV>0),
i=0 ⟹ ∄ (EEO x TR 220/x kV/kV i) ⟺ (EEO x n_TR 220/x kV/kV=0),
i∈{1, ..., EEO x n_TR 220/x kV/kV} ⟺ EEO x n_TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TR 220/x kV/kV=0, 
EEO x n_TR 220/x kV/kV∈N0;
EEO x TR 110/x kV/kV i:
∀i (i≠0) ⟹ ∃ (EEO x TR 110/x kV/kV i) ⟺ (EEO x n_TR 110/x kV/kV>0),
i=0 ⟹ ∄ (EEO x TR 110/x kV/kV i) ⟺ (EEO x n_TR 110/x kV/kV=0),
i∈{1, ..., EEO x n_TR 110/x kV/kV} ⟺ EEO x n_TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TR 110/x kV/kV=0, 
EEO x n_TR 110/x kV/kV∈N0;
EEO x GSS 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x GSS 400 kV i) ⟺ (EEO x n_GSS 400 kV>0),
i=0 ⟹ ∄ (EEO x GSS 400 kV i) ⟺ (EEO x n_GSS 400 kV=0),
i∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, i∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_GSS 400 kV∈N0;
EEO x NMT GSS 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT GSS 400 kV i) ⟺ (EEO x n_GSS 400 kV>0),
i=0 ⟹ ∄ (EEO x NMT GSS 400 kV i) ⟺ (EEO x n_GSS 400 kV=0),
i∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, i∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_GSS 400 kV∈N0;
EEO x GSS 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x GSS 220 kV i) ⟺ (EEO x n_GSS 220 kV>0),
i=0 ⟹ ∄ (EEO x GSS 220 kV i) ⟺ (EEO x n_GSS 220 kV=0),
i∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, i∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_GSS 220 kV∈N0;
EEO x NMT GSS 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT GSS 220 kV i) ⟺ (EEO x n_GSS 220 kV>0),
i=0 ⟹ ∄ (EEO x NMT GSS 220 kV i) ⟺ (EEO x n_GSS 220 kV=0),
i∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, i∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_GSS 220 kV∈N0;
EEO x GSS 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x GSS 110 kV i) ⟺ (EEO x n_GSS 110 kV>0),
i=0 ⟹ ∄ (EEO x GSS 110 kV i) ⟺ (EEO x n_GSS 110 kV=0),
i∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, i∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_GSS 110 kV∈N0;
EEO x NMT GSS 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT GSS 110 kV i) ⟺ (EEO x n_GSS 110 kV>0),
i=0 ⟹ ∄ (EEO x NMT GSS 110 kV i) ⟺ (EEO x n_GSS 110 kV=0),
i∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, i∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_GSS 110 kV∈N0;
EEO x GSS x kV i:
∀i (i≠0) ⟹ ∃ (EEO x GSS x kV i) ⟺ (EEO x n_GSS x kV>0),
i=0 ⟹ ∄ (EEO x GSS x kV i) ⟺ (EEO x n_GSS x kV=0),
i∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, i∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_GSS x kV∈N0;
EEO x NMT GSS x kV i:
∀i (i≠0) ⟹ ∃ (EEO x NMT GSS x kV i) ⟺ (EEO x n_GSS x kV>0),
i=0 ⟹ ∄ (EEO x NMT GSS x kV i) ⟺ (EEO x n_GSS x kV=0),
i∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, i∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_GSS x kV∈N0;
EEO x PSS 400 kV i:
∀i (i≠0) ⟹ ∃ (EEO x PSS 400 kV i) ⟺ (EEO x n_PSS 400 kV>0),
i=0 ⟹ ∄ (EEO x PSS 400 kV i) ⟺ (EEO x n_PSS 400 kV=0),
i∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, i∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_PSS 400 kV∈N0;
EEO x PSS 220 kV i:
∀i (i≠0) ⟹ ∃ (EEO x PSS 220 kV i) ⟺ (EEO x n_PSS 220 kV>0),
i=0 ⟹ ∄ (EEO x PSS 220 kV i) ⟺ (EEO x n_PSS 220 kV=0),
i∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, i∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_PSS 220 kV∈N0;
EEO x PSS 110 kV i:
∀i (i≠0) ⟹ ∃ (EEO x PSS 110 kV i) ⟺ (EEO x n_PSS 110 kV>0),
i=0 ⟹ ∄ (EEO x PSS 110 kV i) ⟺ (EEO x n_PSS 110 kV=0),
i∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, i∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_PSS 110 kV∈N0;
EEO x PSS x kV i:
∀i (i≠0) ⟹ ∃ (EEO x PSS x kV i) ⟺ (EEO x n_PSS x kV>0),
i=0 ⟹ ∄ (EEO x PSS x kV i) ⟺ (EEO x n_PSS x kV=0),
i∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, i∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_PSS x kV∈N0;
EEO x UEEO:
∀x∈{1, ..., n_EEO} gde je n_EEO≥2, ∃! EEO x UEEO, n_EEO∈N0.

Definisanje parametara za x-ti EEO
Lista parametara za x-ti EEO:
EEO x n_DVP 400 kV je broj DVP 400 kV u EEO x,
EEO x n_DVP 220 kV je broj DVP 220 kV u EEO x,
EEO x n_DVP 110 kV je broj DVP 110 kV u EEO x,
EEO x n_DVP x kV je broj DVP x kV u EEO x,
EEO x n_KBP 400 kV je broj KBP 400 kV u EEO x,
EEO x n_KBP 220 kV je broj KBP 220 kV u EEO x,
EEO x n_KBP 110 kV je broj KBP 110 kV u EEO x,
EEO x n_KBP x kV je broj KBP x kV u EEO x,
EEO x n_TRPVN TR 400/220 kV/kV je broj TRPVN TR 400/220 kV/kV u EEO x,
EEO x n_TRPVN TR 400/110 kV/kV je broj TRPVN TR 400/110 kV/kV u EEO x,
EEO x n_TRPVN TR 220/110 kV/kV je broj TRPVN TR 220/110 kV/kV u EEO x,
EEO x n_TRPVN TR 400/x kV/kV je broj TRPVN TR 400/x kV/kV u EEO x,
EEO x n_TRPVN TR 220/x kV/kV je broj TRPVN TR 220/x kV/kV u EEO x,
EEO x n_TRPVN TR 110/x kV/kV je broj TRPVN TR 110/x kV/kV u EEO x,
EEO x n_TRPNN TR 400/220 kV/kV je broj TRPNN TR 400/220 kV/kV u EEO x,
EEO x n_TRPNN TR 400/110 kV/kV je broj TRPNN TR 400/110 kV/kV u EEO x,
EEO x n_TRPNN TR 220/110 kV/kV je broj TRPNN TR 220/110 kV/kV u EEO x,
EEO x n_TRPNN TR 400/x kV/kV je broj TRPNN TR 400/x kV/kV u EEO x,
EEO x n_TRPNN TR 220/x kV/kV je broj TRPNN TR 220/x kV/kV u EEO x,
EEO x n_TRPNN TR 110/x kV/kV je broj TRPNN TR 110/x kV/kV u EEO x,
EEO x n_GSP 400 kV je broj GSP 400 kV u EEO x,
EEO x n_GSP 220 kV je broj GSP 220 kV u EEO x,
EEO x n_GSP 110 kV je broj GSP 110 kV u EEO x,
EEO x n_GSP x kV je broj GSP x kV u EEO x,
EEO x n_PSP 400 kV je broj PSP 400 kV u EEO x,
EEO x n_PSP 220 kV je broj PSP 220 kV u EEO x,
EEO x n_PSP 110 kV je broj PSP 110 kV u EEO x,
EEO x n_PSP x kV je broj PSP x kV u EEO x,
EEO x n_TR 400/220 kV/kV je broj TR 400/220 kV/kV u EEO x,
EEO x n_TR 400/110 kV/kV je broj TR 400/110 kV/kV u EEO x,
EEO x n_TR 220/110 kV/kV je broj TR 220/110 kV/kV u EEO x,
EEO x n_TR 400/x kV/kV je broj TR 400/x kV/kV u EEO x,
EEO x n_TR 220/x kV/kV je broj TR 220/x kV/kV u EEO x,
EEO x n_TR 110/x kV/kV je broj TR 110/x kV/kV u EEO x,
EEO x n_GSS 400 kV je broj GSS sa pripadajućom opremom 400 kV u EEO x,
EEO x n_GSS 220 kV je broj GSS sa pripadajućom opremom 220 kV u EEO x,
EEO x n_GSS 110 kV je broj GSS sa pripadajućom opremom 110 kV u EEO x,
EEO x n_GSS x kV je broj GSS sa pripadajućom opremom x kV u EEO x,
EEO x n_PSS 400 kV je broj PSS 400 kV u EEO x,
EEO x n_PSS 220 kV je broj PSS 220 kV u EEO x,
EEO x n_PSS 110 kV je broj PSS 110 kV u EEO x,
EEO x n_PSS x kV je broj PSS x kV u EEO x.
Sve prethodno navedene parametre za svaki EEO x, gde x ∈{1, ..., n_EEO}, n_EEO>1, n_EEO∈N, definiše korisnik.
Osnovni elementi elektroenergetske opreme PS koja ne pripada EEO
Osnovi elementi podele, odnosno listovi elektroenergetske opreme koja ne pripada EEO sa definisanim postojanjem su:
DV 400 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST DV 400 kV ∨ ∀ (x, i, y, j): (DV 400 kV EEO x (i) EEO y (j)) ∈ LISTA DV 400 kV) ⟹ ∃ (DV 400 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST DV 400 kV ∨ ∀ (x, i, y, j): (DV 400 kV EEO x (i) EEO y (j)) ∉ LISTA DV 400 kV) ⟹ ∄ (DV 400 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO y n_DVP 400 kV} ⟺ EEO y n_DVP 400 kV>0, j∈{0} ⟺ EEO y n_DVP 400 kV=0, 
n_EEO∈N, EEO x n_DVP 400 kV, EEO y n_DVP 400 kV∈N0;
DV 220 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST DV 220 kV ∨ ∀ (x, i, y, j): (DV 220 kV EEO x (i) EEO y (j)) ∈ LISTA DV 220 kV) ⟹ ∃ (DV 220 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST DV 220 kV ∨ ∀ (x, i, y, j): (DV 220 kV EEO x (i) EEO y (j)) ∉ LISTA DV 220 kV) ⟹ ∄ (DV 220 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO y n_DVP 220 kV} ⟺ EEO y n_DVP 220 kV>0, j∈{0} ⟺ EEO y n_DVP 220 kV=0, 
n_EEO∈N, EEO x n_DVP 220 kV, EEO y n_DVP 220 kV∈N0;
DV 110 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST DV 110 kV ∨ ∀ (x, i, y, j): (DV 110 kV EEO x (i) EEO y (j)) ∈ LISTA DV 110 kV) ⟹ ∃ (DV 110 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST DV 110 kV ∨ ∀ (x, i, y, j): (DV 110 kV EEO x (i) EEO y (j)) ∉ LISTA DV 110 kV) ⟹ ∄ (DV 110 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO y n_DVP 110 kV} ⟺ EEO y n_DVP 110 kV>0, j∈{0} ⟺ EEO y n_DVP 110 kV=0, 
n_EEO∈N, EEO x n_DVP 110 kV, EEO y n_DVP 110 kV∈N0;
DV x kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST DV x kV ∨ ∀ (x, i, y, j): (DV x kV EEO x (i) EEO y (j)) ∈ LISTA DV x kV) ⟹ ∃ (DV x kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST DV x kV ∨ ∀ (x, i, y, j): (DV x kV EEO x (i) EEO y (j)) ∉ LISTA DV x kV) ⟹ ∄ (DV x kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO y n_DVP x kV} ⟺ EEO y n_DVP x kV>0, j∈{0} ⟺ EEO y n_DVP x kV=0, 
n_EEO∈N, EEO x n_DVP x kV, EEO y n_DVP x kV∈N0;
KB 400 kVEEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST KB 400 kV ∨ ∀ (x, i, y, j): (KB 400 kVEEO x (i) EEO y (j)) ∈ LISTA KB 400 kV) ⟹ ∃ (KB 400 kVEEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST KB 400 kV ∨ ∀ (x, i, y, j): (KB 400 kVEEO x (i) EEO y (j)) ∉ LISTA KB 400 kV) ⟹ ∄ (KB 400 kVEEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO y n_KBP 400 kV} ⟺ EEO y n_KBP 400 kV>0, j∈{0} ⟺ EEO y n_KBP 400 kV=0, 
n_EEO∈N, EEO x n_KBP 400 kV, EEO y n_KBP 400 kV∈N0;
KB 220 kVEEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST KB 220 kV ∨ ∀ (x, i, y, j): (KB 220 kVEEO x (i) EEO y (j)) ∈ LISTA KB 220 kV) ⟹ ∃ (KB 220 kVEEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST KB 220 kV ∨ ∀ (x, i, y, j): (KB 220 kVEEO x (i) EEO y (j)) ∉ LISTA KB 220 kV) ⟹ ∄ (KB 220 kVEEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO y n_KBP 220 kV} ⟺ EEO y n_KBP 220 kV>0, j∈{0} ⟺ EEO y n_KBP 220 kV=0, 
n_EEO∈N, EEO x n_KBP 220 kV, EEO y n_KBP 220 kV∈N0;
KB 110 kVEEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST KB 110 kV ∨ ∀ (x, i, y, j): (KB 110 kVEEO x (i) EEO y (j)) ∈ LISTA KB 110 kV) ⟹ ∃ (KB 110 kVEEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST KB 110 kV ∨ ∀ (x, i, y, j): (KB 110 kVEEO x (i) EEO y (j)) ∉ LISTA KB 110 kV) ⟹ ∄ (KB 110 kVEEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO y n_KBP 110 kV} ⟺ EEO y n_KBP 110 kV>0, j∈{0} ⟺ EEO y n_KBP 110 kV=0, 
n_EEO∈N, EEO x n_KBP 110 kV, EEO y n_KBP 110 kV∈N0;
KB x kVEEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST KB x kV ∨ ∀ (x, i, y, j): (KB x kVEEO x (i) EEO y (j)) ∈ LISTA KB x kV) ⟹ ∃ (KB x kVEEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST KB x kV ∨ ∀ (x, i, y, j): (KB x kVEEO x (i) EEO y (j)) ∉ LISTA KB x kV) ⟹ ∄ (KB x kVEEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO y n_KBP x kV} ⟺ EEO y n_KBP x kV>0, j∈{0} ⟺ EEO y n_KBP x kV=0, 
n_EEO∈N, EEO x n_KBP x kV, EEO y n_KBP x kV∈N0;
MV (DV+KB) 400 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (DV+KB) 400 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 400 kV EEO x (i) EEO y (j)) ∈ LISTA MV (DV+KB) 400 kV) ⟹ ∃ (MV (DV+KB) 400 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (DV+KB) 400 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 400 kV EEO x (i) EEO y (j)) ∉ LISTA MV (DV+KB) 400 kV) ⟹ ∄ (MV (DV+KB) 400 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO y n_KBP 400 kV} ⟺ EEO y n_KBP 400 kV>0, j∈{0} ⟺ EEO y n_KBP 400 kV=0, 
n_EEO∈N, EEO x n_DVP 400 kV, EEO y n_KBP 400 kV∈N0;
MV (DV+KB) 220 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (DV+KB) 220 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 220 kV EEO x (i) EEO y (j)) ∈ LISTA MV (DV+KB) 220 kV) ⟹ ∃ (MV (DV+KB) 220 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (DV+KB) 220 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 220 kV EEO x (i) EEO y (j)) ∉ LISTA MV (DV+KB) 220 kV) ⟹ ∄ (MV (DV+KB) 220 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO y n_KBP 220 kV} ⟺ EEO y n_KBP 220 kV>0, j∈{0} ⟺ EEO y n_KBP 220 kV=0, 
n_EEO∈N, EEO x n_DVP 220 kV, EEO y n_KBP 220 kV∈N0;
MV (DV+KB) 110 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (DV+KB) 110 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 110 kV EEO x (i) EEO y (j)) ∈ LISTA MV (DV+KB) 110 kV) ⟹ ∃ (MV (DV+KB) 110 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (DV+KB) 110 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 110 kV EEO x (i) EEO y (j)) ∉ LISTA MV (DV+KB) 110 kV) ⟹ ∄ (MV (DV+KB) 110 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO y n_KBP 110 kV} ⟺ EEO y n_KBP 110 kV>0, j∈{0} ⟺ EEO y n_KBP 110 kV=0, 
n_EEO∈N, EEO x n_DVP 110 kV, EEO y n_KBP 110 kV∈N0;
MV (DV+KB) x kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (DV+KB) x kV ∨ ∀ (x, i, y, j): (MV (DV+KB) x kV EEO x (i) EEO y (j)) ∈ LISTA MV (DV+KB) x kV) ⟹ ∃ (MV (DV+KB) x kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (DV+KB) x kV ∨ ∀ (x, i, y, j): (MV (DV+KB) x kV EEO x (i) EEO y (j)) ∉ LISTA MV (DV+KB) x kV) ⟹ ∄ (MV (DV+KB) x kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO y n_KBP x kV} ⟺ EEO y n_KBP x kV>0, j∈{0} ⟺ EEO y n_KBP x kV=0, 
n_EEO∈N, EEO x n_DVP x kV, EEO y n_KBP x kV∈N0;
MV (KB+DV) 400 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (KB+DV) 400 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 400 kV EEO x (i) EEO y (j)) ∈ LISTA MV (KB+DV) 400 kV) ⟹ ∃ (MV (KB+DV) 400 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (KB+DV) 400 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 400 kV EEO x (i) EEO y (j)) ∉ LISTA MV (KB+DV) 400 kV) ⟹ ∄ (MV (KB+DV) 400 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO y n_DVP 400 kV} ⟺ EEO y n_DVP 400 kV>0, j∈{0} ⟺ EEO y n_DVP 400 kV=0, 
n_EEO∈N, EEO x n_KBP 400 kV, EEO y n_DVP 400 kV∈N0;
MV (KB+DV) 220 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (KB+DV) 220 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 220 kV EEO x (i) EEO y (j)) ∈ LISTA MV (KB+DV) 220 kV) ⟹ ∃ (MV (KB+DV) 220 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (KB+DV) 220 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 220 kV EEO x (i) EEO y (j)) ∉ LISTA MV (KB+DV) 220 kV) ⟹ ∄ (MV (KB+DV) 220 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO y n_DVP 220 kV} ⟺ EEO y n_DVP 220 kV>0, j∈{0} ⟺ EEO y n_DVP 220 kV=0, 
n_EEO∈N, EEO x n_KBP 220 kV, EEO y n_DVP 220 kV∈N0;
MV (KB+DV) 110 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (KB+DV) 110 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 110 kV EEO x (i) EEO y (j)) ∈ LISTA MV (KB+DV) 110 kV) ⟹ ∃ (MV (KB+DV) 110 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (KB+DV) 110 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 110 kV EEO x (i) EEO y (j)) ∉ LISTA MV (KB+DV) 110 kV) ⟹ ∄ (MV (KB+DV) 110 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO y n_DVP 110 kV} ⟺ EEO y n_DVP 110 kV>0, j∈{0} ⟺ EEO y n_DVP 110 kV=0, 
n_EEO∈N, EEO x n_KBP 110 kV, EEO y n_DVP 110 kV∈N0;
MV (KB+DV) x kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (KB+DV) x kV ∨ ∀ (x, i, y, j): (MV (KB+DV) x kV EEO x (i) EEO y (j)) ∈ LISTA MV (KB+DV) x kV) ⟹ ∃ (MV (KB+DV) x kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (KB+DV) x kV ∨ ∀ (x, i, y, j): (MV (KB+DV) x kV EEO x (i) EEO y (j)) ∉ LISTA MV (KB+DV) x kV) ⟹ ∄ (MV (KB+DV) x kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO y n_DVP x kV} ⟺ EEO y n_DVP x kV>0, j∈{0} ⟺ EEO y n_DVP x kV=0, 
n_EEO∈N, EEO x n_KBP x kV, EEO y n_DVP x kV∈N0;
Definisanje parametara elemenata elektroenergetske opreme koja ne pripada EEO
DV 400 kV u PS su određeni matricom POVEZANOST DV 400 kV ili listom LISTA DV 400 kV koja sadrži sve DV 400 kV punog naziva (DV 400 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST DV 400 kV) = n_DV 400 kV x 4, gde n_DV 400 kV je broj DV 400 kV u PS;
DV 220 kV u PS su određeni matricom POVEZANOST DV 220 kV ili listom LISTA DV 220 kV koja sadrži sve DV 220 kV punog naziva (DV 220 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST DV 220 kV) = n_DV 220 kV x 4, gde n_DV 220 kV je broj DV 220 kV u PS;
DV 110 kV u PS su određeni matricom POVEZANOST DV 110 kV ili listom LISTA DV 110 kV koja sadrži sve DV 110 kV punog naziva (DV 110 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST DV 110 kV) = n_DV 110 kV x 4, gde n_DV 110 kV je broj DV 110 kV u PS;
DV x kV u PS su određeni matricom POVEZANOST DV x kV ili listom LISTA DV x kV koja sadrži sve DV x kV punog naziva (DV x kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST DV x kV) = n_DV x kV x 4, gde n_DV x kV je broj DV x kV u PS;
KB 400 kV u PS su određeni matricom POVEZANOST KB 400 kV ili listom LISTA KB 400 kV koja sadrži sve KB 400 kV punog naziva (KB 400 kVEEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST KB 400 kV) = n_KB 400 kV x 4, gde n_KB 400 kV je broj KB 400 kV u PS;
KB 220 kV u PS su određeni matricom POVEZANOST KB 220 kV ili listom LISTA KB 220 kV koja sadrži sve KB 220 kV punog naziva (KB 220 kVEEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST KB 220 kV) = n_KB 220 kV x 4, gde n_KB 220 kV je broj KB 220 kV u PS;
KB 110 kV u PS su određeni matricom POVEZANOST KB 110 kV ili listom LISTA KB 110 kV koja sadrži sve KB 110 kV punog naziva (KB 110 kVEEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST KB 110 kV) = n_KB 110 kV x 4, gde n_KB 110 kV je broj KB 110 kV u PS;
KB x kV u PS su određeni matricom POVEZANOST KB x kV ili listom LISTA KB x kV koja sadrži sve KB x kV punog naziva (KB x kVEEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST KB x kV) = n_KB x kV x 4, gde n_KB x kV je broj KB x kV u PS;
MV (DV+KB) 400 kV u PS su određeni matricom POVEZANOST MV (DV+KB) 400 kV ili listom LISTA MV (DV+KB) 400 kV koja sadrži sve MV (DV+KB) 400 kV punog naziva (MV (DV+KB) 400 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST MV (DV+KB) 400 kV) = n_MV (DV+KB) 400 kV x 4, gde n_MV (DV+KB) 400 kV je broj MV (DV+KB) 400 kV u PS;
MV (DV+KB) 220 kV u PS su određeni matricom POVEZANOST MV (DV+KB) 220 kV ili listom LISTA MV (DV+KB) 220 kV koja sadrži sve MV (DV+KB) 220 kV punog naziva (MV (DV+KB) 220 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST MV (DV+KB) 220 kV) = n_MV (DV+KB) 220 kV x 4, gde n_MV (DV+KB) 220 kV je broj MV (DV+KB) 220 kV u PS;
MV (DV+KB) 110 kV u PS su određeni matricom POVEZANOST MV (DV+KB) 110 kV ili listom LISTA MV (DV+KB) 110 kV koja sadrži sve MV (DV+KB) 110 kV punog naziva (MV (DV+KB) 110 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST MV (DV+KB) 110 kV) = n_MV (DV+KB) 110 kV x 4, gde n_MV (DV+KB) 110 kV je broj MV (DV+KB) 110 kV u PS;
MV (DV+KB) x kV u PS su određeni matricom POVEZANOST MV (DV+KB) x kV ili listom LISTA MV (DV+KB) x kV koja sadrži sve MV (DV+KB) x kV punog naziva (MV (DV+KB) x kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST MV (DV+KB) x kV) = n_MV (DV+KB) x kV x 4, gde n_MV (DV+KB) x kV je broj MV (DV+KB) x kV u PS;
MV (KB+DV) 400 kV u PS su određeni matricom POVEZANOST MV (KB+DV) 400 kV ili listom LISTA MV (KB+DV) 400 kV koja sadrži sve MV (KB+DV) 400 kV punog naziva (MV (KB+DV) 400 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST MV (KB+DV) 400 kV) = n_MV (KB+DV) 400 kV x 4, gde n_MV (KB+DV) 400 kV je broj MV (KB+DV) 400 kV u PS;
MV (KB+DV) 220 kV u PS su određeni matricom POVEZANOST MV (KB+DV) 220 kV ili listom LISTA MV (KB+DV) 220 kV koja sadrži sve MV (KB+DV) 220 kV punog naziva (MV (KB+DV) 220 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST MV (KB+DV) 220 kV) = n_MV (KB+DV) 220 kV x 4, gde n_MV (KB+DV) 220 kV je broj MV (KB+DV) 220 kV u PS;
MV (KB+DV) 110 kV u PS su određeni matricom POVEZANOST MV (KB+DV) 110 kV ili listom LISTA MV (KB+DV) 110 kV koja sadrži sve MV (KB+DV) 110 kV punog naziva (MV (KB+DV) 110 kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST MV (KB+DV) 110 kV) = n_MV (KB+DV) 110 kV x 4, gde n_MV (KB+DV) 110 kV je broj MV (KB+DV) 110 kV u PS;
MV (KB+DV) x kV u PS su određeni matricom POVEZANOST MV (KB+DV) x kV ili listom LISTA MV (KB+DV) x kV koja sadrži sve MV (KB+DV) x kV punog naziva (MV (KB+DV) x kV EEO x (i) EEO y (j)) sa određenom četvorokom (x,i,y,j).
dim(POVEZANOST MV (KB+DV) x kV) = n_MV (KB+DV) x kV x 4, gde n_MV (KB+DV) x kV je broj MV (KB+DV) x kV u PS.
Sve prethodno pomenute matrice ili liste definiše korisnik.
## Veza elemenata elektroenergetske opreme PS
Svaki osnovni element povezan je sa jednim ili više osnovnih elemenata koji se naziva prethodnik ukoliko je jedan, odnosno koji se nazivaju prethodnici, ukoliko ih je više, i sa jednim ili više osnovnih elemenata koji se naziva sledbenik ukoliko je jedan, odnosno koji se nazivaju sledbenici, ukoliko ih je više.
### Veza osnovnog elementa sa prethodnik i sledbenikom
Struktura povezanosti osnovnog elementa, kada je osnovni element povezan sa jednim prethodnikom i jednim sledbenikom:
prethodnik <-> galvanska veza <-> osnovni element <-> galvanska veza <-> sledbenik.
“galvanska veza <->” je “provodnik <->” određenog poprečnog preseka, dužine i materijala. U cilju jednostvanosti, usvajamo pojednostavljenu strukturu gde “provodnik <->” ne pisemo ali znamo da postoji:
prethodnik <-> osnovni element <-> sledbenik.
### Veza osnovnog elementa sa prethodnicima i sledbenikom
Struktura povezanosti osnovnog elementa, kada je osnovni element povezan sa više prethodnika i jednim sledbenikom:
prethodnik 1 <-> galvanska veza <-> osnovni element
prethodnik i <-> galvanska veza <-> osnovni element
prethodnik n_prethodnika <-> galvanska veza <-> osnovni element
osnovni element <-> galvanska veza <-> sledbenik
gde i označava i-ti element niza definisan sa i∈{2, ..., n_prethodnika}; n_prethodnika≥2, n_prethodnika ∈N.
“galvanska veza <->” je “provodnik <->” određenog poprečnog preseka, dužine i materijala. U cilju jednostvanosti, usvajamo pojednostavljenu strukturu gde “provodnik <->” ne pisemo ali znamo da postoji:
prethodnik 1 <-> osnovni element;
prethodnik i <-> osnovni element;
prethodnik n_prethodnika <-> osnovni element;
osnovni element <-> galvanska veza <-> sledbenik,
gde i označava i-ti element niza definisan sa i∈{2, ..., n_prethodnika}; n_prethodnika≥2, n_prethodnika ∈N.
### Veza osnovnog elementa sa prethodnikom i sledbenicima
Struktura povezanosti osnovnog elementa, kada je osnovni element povezan sa jednim prethodnikom i više sledbenika:
prethodnik <-> galvanska veza <-> osnovni element
osnovni element <-> galvanska veza <-> sledbenik 1
osnovni element <-> galvanska veza <-> sledbenik i
osnovni element <-> galvanska veza <-> sledbenik n_sledbenika
gde i označava i-ti element niza definisan sa i∈{2, ..., n_sledbenika}; n_ sledbenika ≥2, n_ sledbenika ∈N.
“galvanska veza <->” je “provodnik <->” određenog poprečnog preseka, dužine i materijala. U cilju jednostvanosti, usvajamo pojednostavljenu strukturu gde “provodnik <->” ne pisemo ali znamo da postoji:
prethodnik <-> osnovni element;
osnovni element <-> sledbenik 1;
osnovni element <-> sledbenik i;
osnovni element <-> sledbenik n_sledbenika,
gde i označava i-ti element niza definisan sa i∈{2, ..., n_sledbenika}; n_ sledbenika ≥2, n_ sledbenika ∈N.
### Veza osnovnog elementa sa prethodnicima i sledbenicima
Struktura povezanosti osnovnog elementa, kada je osnovni element povezan sa više prethodnika i više sledbenika:
prethodnik 1 <-> galvanska veza <-> osnovni element
prethodnik i <-> galvanska veza <-> osnovni element
prethodnik n_prethodnika <-> galvanska veza <-> osnovni element
osnovni element <-> galvanska veza <-> sledbenik 1
osnovni element <-> galvanska veza <-> sledbenik j
osnovni element <-> galvanska veza <-> sledbenik n_sledbenika
gde i i j označavaju i-ti i j-ti element niza definisanih sa i∈{2, ..., n_prethodnika}, n_ prethodnika≥2; j∈{2, ..., n_sledbenika}, n_ sledbenika ≥2; n_ prethodnika, n_ sledbenika ∈N.
“galvanska veza <->” je “provodnik <->” određenog poprečnog preseka, dužine i materijala. U cilju jednostvanosti, usvajamo pojednostavljenu strukturu gde “provodnik <->” ne pisemo ali znamo da postoji:
prethodnik 1 <-> osnovni element;
prethodnik i <-> osnovni element;
prethodnik n_prethodnika <-> osnovni element;
osnovni element <-> sledbenik 1;
osnovni element <-> sledbenik j;
osnovni element <-> sledbenik n_sledbenika,
gde i i j označavaju i-ti i j-ti element niza definisanih sa i∈{2, ..., n_prethodnika}, n_ prethodnika≥2; j∈{2, ..., n_sledbenika}, n_ sledbenika ≥2; n_ prethodnika, n_ sledbenika ∈N.
### Prethodnici i sledbenici osnovnih elemenata koji pripadaju EEO
Prethodnici i sledbenici osnovih elemenata koji pripadaju EEO su:
SR DVP 400 kV i GSS j:
GSS 400 kV j <-> SR DVP 400 kV i GSS j <-> P DVP 400 kV i,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_DVP 400 kV, n_GSS 400 kV∈N0;
P DVP 400 kV i:
SR DVP 400 kV i GSS j <-> P DVP 400 kV i <-> SMT DVP 400 kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_DVP 400 kV, n_GSS 400 kV∈N0;
IRSU DVP 400 kV i:
SMT DVP 400 kV i <-> IRSU DVP 400 kV i,
IRSU DVP 400 kV i <-> NMT DVP 400 kV i,
IRSU DVP 400 kV i <-> kraj,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
SMT DVP 400 kV i:
P DVP 400 kV i <-> SMT DVP 400 kV i <-> IRSU DVP 400 kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
NMT DVP 400 kV i:
UEEO <-> NMT DVP 400 kV i,
NMT DVP 400 kV i <-> IRSU DVP 400 kV i,
NMT DVP 400 kV i <-> kraj,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
SR DVP 400 kV i PSS k:
PSS 400 kV k <-> SR DVP 400 kV i PSS k,
SR DVP 400 kV i PSS k <-> IRSU DVP 400 kV i,
SR DVP 400 kV i PSS k <-> SMT DVP 400 kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, 
k∈{0} ⟺ n_PSS 400 kV=0, 
n_DVP 400 kV, n_PSS 400 kV∈N0;
P DVP 400 kV i:
SR DVP 400 kV i GSS j <-> P DVP 400 kV i <-> IRSU DVP 400 kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_DVP 400 kV, n_GSS 400 kV∈N0;
IRSU DVP 400 kV i:
P DVP 400 kV i <-> IRSU DVP 400 kV i,
IRSU DVP 400 kV i <-> SR DVP 400 kV i PSS k,
IRSU DVP 400 kV i <-> SMT DVP 400 kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, 
k∈{0} ⟺ n_PSS 400 kV=0, 
n_DVP 400 kV, n_PSS 400 kV∈N0;
SMT DVP 400 kV i:
IRSU DVP 400 kV i <-> SMT DVP 400 kV i,
SR DVP 400 kV i PSS k <-> SMT DVP 400 kV i,
SMT DVP 400 kV i <-> NMT DVP 400 kV i
SMT DVP 400 kV i <-> kraj,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
NMT DVP 400 kV i:
UEEO <-> NMT DVP 400 kV i,
NMT DVP 400 kV i <-> SMT DVP 400 kV i,
NMT DVP 400 kV i <-> kraj,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, 
i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
SR DVP 220 kV i GSS j:
GSS 220 kV j <-> SR DVP 220 kV i GSS j <-> P DVP 220 kV i,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_DVP 220 kV, n_GSS 220 kV∈N0;
P DVP 220 kV i:
SR DVP 220 kV i GSS j <-> P DVP 220 kV i <-> SMT DVP 220 kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_DVP 220 kV, n_GSS 220 kV∈N0;
IRSU DVP 220 kV i:
SMT DVP 220 kV i <-> IRSU DVP 220 kV i,
IRSU DVP 220 kV i <-> NMT DVP 220 kV i,
IRSU DVP 220 kV i <-> kraj,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
SMT DVP 220 kV i:
P DVP 220 kV i <-> SMT DVP 220 kV i <-> IRSU DVP 220 kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
NMT DVP 220 kV i:
UEEO <-> NMT DVP 220 kV i,
NMT DVP 220 kV i <-> IRSU DVP 220 kV i,
NMT DVP 220 kV i <-> kraj,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
SR DVP 220 kV i PSS k:
PSS 220 kV k <-> SR DVP 220 kV i PSS k,
SR DVP 220 kV i PSS k <-> IRSU DVP 220 kV i,
SR DVP 220 kV i PSS k <-> SMT DVP 220 kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_DVP 220 kV, n_PSS 220 kV∈N0;
P DVP 220 kV i:
SR DVP 220 kV i GSS j <-> P DVP 220 kV i <-> IRSU DVP 220 kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_DVP 220 kV, n_GSS 220 kV∈N0;
IRSU DVP 220 kV i:
P DVP 220 kV i <-> IRSU DVP 220 kV i,
IRSU DVP 220 kV i <-> SR DVP 220 kV i PSS k,
IRSU DVP 220 kV i <-> SMT DVP 220 kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_DVP 220 kV, n_PSS 220 kV∈N0;
SMT DVP 220 kV i:
IRSU DVP 220 kV i <-> SMT DVP 220 kV i,
SR DVP 220 kV i PSS k <-> SMT DVP 220 kV i,
SMT DVP 220 kV i <-> NMT DVP 220 kV i
SMT DVP 220 kV i <-> kraj,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
NMT DVP 220 kV i:
UEEO <-> NMT DVP 220 kV i,
NMT DVP 220 kV i <-> SMT DVP 220 kV i,
NMT DVP 220 kV i <-> kraj,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, 
i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
SR DVP 110 kV i GSS j:
GSS 110 kV j <-> SR DVP 110 kV i GSS j <-> P DVP 110 kV i,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_DVP 110 kV, n_GSS 110 kV∈N0;
P DVP 110 kV i:
SR DVP 110 kV i GSS j <-> P DVP 110 kV i <-> SMT DVP 110 kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_DVP 110 kV, n_GSS 110 kV∈N0;
IRSU DVP 110 kV i:
SMT DVP 110 kV i <-> IRSU DVP 110 kV i,
IRSU DVP 110 kV i <-> NMT DVP 110 kV i,
IRSU DVP 110 kV i <-> kraj,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
SMT DVP 110 kV i:
P DVP 110 kV i <-> SMT DVP 110 kV i <-> IRSU DVP 110 kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
NMT DVP 110 kV i:
UEEO <-> NMT DVP 110 kV i,
NMT DVP 110 kV i <-> IRSU DVP 110 kV i,
NMT DVP 110 kV i <-> kraj,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
SR DVP 110 kV i PSS k:
PSS 110 kV k <-> SR DVP 110 kV i PSS k,
SR DVP 110 kV i PSS k <-> IRSU DVP 110 kV i,
SR DVP 110 kV i PSS k <-> SMT DVP 110 kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_DVP 110 kV, n_PSS 110 kV∈N0;
P DVP 110 kV i:
SR DVP 110 kV i GSS j <-> P DVP 110 kV i <-> IRSU DVP 110 kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_DVP 110 kV, n_GSS 110 kV∈N0;
IRSU DVP 110 kV i:
P DVP 110 kV i <-> IRSU DVP 110 kV i,
IRSU DVP 110 kV i <-> SR DVP 110 kV i PSS k,
IRSU DVP 110 kV i <-> SMT DVP 110 kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_DVP 110 kV, n_PSS 110 kV∈N0;
SMT DVP 110 kV i:
IRSU DVP 110 kV i <-> SMT DVP 110 kV i,
SR DVP 110 kV i PSS k <-> SMT DVP 110 kV i,
SMT DVP 110 kV i <-> NMT DVP 110 kV i
SMT DVP 110 kV i <-> kraj,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
NMT DVP 110 kV i:
UEEO <-> NMT DVP 110 kV i,
NMT DVP 110 kV i <-> SMT DVP 110 kV i,
NMT DVP 110 kV i <-> kraj,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, 
i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
SR DVP x kV i GSS j:
GSS x kV j <-> SR DVP x kV i GSS j <-> P DVP x kV i,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_DVP x kV, n_GSS x kV∈N0;
P DVP x kV i:
SR DVP x kV i GSS j <-> P DVP x kV i <-> SMT DVP x kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_DVP x kV, n_GSS x kV∈N0;
IRSU DVP x kV i:
SMT DVP x kV i <-> IRSU DVP x kV i,
IRSU DVP x kV i <-> NMT DVP x kV i,
IRSU DVP x kV i <-> kraj,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
SMT DVP x kV i:
P DVP x kV i <-> SMT DVP x kV i <-> IRSU DVP x kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
NMT DVP x kV i:
UEEO <-> NMT DVP x kV i,
NMT DVP x kV i <-> IRSU DVP x kV i,
NMT DVP x kV i <-> kraj,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
SR DVP x kV i PSS k:
PSS x kV k <-> SR DVP x kV i PSS k,
SR DVP x kV i PSS k <-> IRSU DVP x kV i,
SR DVP x kV i PSS k <-> SMT DVP x kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_DVP x kV, n_PSS x kV∈N0;
P DVP x kV i:
SR DVP x kV i GSS j <-> P DVP x kV i <-> IRSU DVP x kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_DVP x kV, n_GSS x kV∈N0;
IRSU DVP x kV i:
P DVP x kV i <-> IRSU DVP x kV i,
IRSU DVP x kV i <-> SR DVP x kV i PSS k,
IRSU DVP x kV i <-> SMT DVP x kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_DVP x kV, n_PSS x kV∈N0;
SMT DVP x kV i:
IRSU DVP x kV i <-> SMT DVP x kV i,
SR DVP x kV i PSS k <-> SMT DVP x kV i,
SMT DVP x kV i <-> NMT DVP x kV i
SMT DVP x kV i <-> kraj,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
NMT DVP x kV i:
UEEO <-> NMT DVP x kV i,
NMT DVP x kV i <-> SMT DVP x kV i,
NMT DVP x kV i <-> kraj,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, 
i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
SR KBP 400 kV i GSS j:
GSS 400 kV j <-> SR KBP 400 kV i GSS j <-> P KBP 400 kV i,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_KBP 400 kV, n_GSS 400 kV∈N0;
P KBP 400 kV i:
SR KBP 400 kV i GSS j <-> P KBP 400 kV i <-> SMT KBP 400 kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_KBP 400 kV, n_GSS 400 kV∈N0;
IRSU KBP 400 kV i:
SMT KBP 400 kV i <-> IRSU KBP 400 kV i,
IRSU KBP 400 kV i <-> NMT KBP 400 kV i,
IRSU KBP 400 kV i <-> kraj,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
SMT KBP 400 kV i:
P KBP 400 kV i <-> SMT KBP 400 kV i <-> IRSU KBP 400 kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
NMT KBP 400 kV i:
UEEO <-> NMT KBP 400 kV i,
NMT KBP 400 kV i <-> IRSU KBP 400 kV i,
NMT KBP 400 kV i <-> kraj,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
SR KBP 400 kV i PSS k:
PSS 400 kV k <-> SR KBP 400 kV i PSS k,
SR KBP 400 kV i PSS k <-> IRSU KBP 400 kV i,
SR KBP 400 kV i PSS k <-> SMT KBP 400 kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, 
k∈{0} ⟺ n_PSS 400 kV=0, 
n_KBP 400 kV, n_PSS 400 kV∈N0;
P KBP 400 kV i:
SR KBP 400 kV i GSS j <-> P KBP 400 kV i <-> IRSU KBP 400 kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_KBP 400 kV, n_GSS 400 kV∈N0;
IRSU KBP 400 kV i:
P KBP 400 kV i <-> IRSU KBP 400 kV i,
IRSU KBP 400 kV i <-> SR KBP 400 kV i PSS k,
IRSU KBP 400 kV i <-> SMT KBP 400 kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, 
k∈{0} ⟺ n_PSS 400 kV=0, 
n_KBP 400 kV, n_PSS 400 kV∈N0;
SMT KBP 400 kV i:
IRSU KBP 400 kV i <-> SMT KBP 400 kV i,
SR KBP 400 kV i PSS k <-> SMT KBP 400 kV i,
SMT KBP 400 kV i <-> NMT KBP 400 kV i
SMT KBP 400 kV i <-> kraj,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
NMT KBP 400 kV i:
UEEO <-> NMT KBP 400 kV i,
NMT KBP 400 kV i <-> SMT KBP 400 kV i,
NMT KBP 400 kV i <-> kraj,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, 
i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
SR KBP 220 kV i GSS j:
GSS 220 kV j <-> SR KBP 220 kV i GSS j <-> P KBP 220 kV i,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_KBP 220 kV, n_GSS 220 kV∈N0;
P KBP 220 kV i:
SR KBP 220 kV i GSS j <-> P KBP 220 kV i <-> SMT KBP 220 kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_KBP 220 kV, n_GSS 220 kV∈N0;
IRSU KBP 220 kV i:
SMT KBP 220 kV i <-> IRSU KBP 220 kV i,
IRSU KBP 220 kV i <-> NMT KBP 220 kV i,
IRSU KBP 220 kV i <-> kraj,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
SMT KBP 220 kV i:
P KBP 220 kV i <-> SMT KBP 220 kV i <-> IRSU KBP 220 kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
NMT KBP 220 kV i:
UEEO <-> NMT KBP 220 kV i,
NMT KBP 220 kV i <-> IRSU KBP 220 kV i,
NMT KBP 220 kV i <-> kraj,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
SR KBP 220 kV i PSS k:
PSS 220 kV k <-> SR KBP 220 kV i PSS k,
SR KBP 220 kV i PSS k <-> IRSU KBP 220 kV i,
SR KBP 220 kV i PSS k <-> SMT KBP 220 kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_KBP 220 kV, n_PSS 220 kV∈N0;
P KBP 220 kV i:
SR KBP 220 kV i GSS j <-> P KBP 220 kV i <-> IRSU KBP 220 kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_KBP 220 kV, n_GSS 220 kV∈N0;
IRSU KBP 220 kV i:
P KBP 220 kV i <-> IRSU KBP 220 kV i,
IRSU KBP 220 kV i <-> SR KBP 220 kV i PSS k,
IRSU KBP 220 kV i <-> SMT KBP 220 kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_KBP 220 kV, n_PSS 220 kV∈N0;
SMT KBP 220 kV i:
IRSU KBP 220 kV i <-> SMT KBP 220 kV i,
SR KBP 220 kV i PSS k <-> SMT KBP 220 kV i,
SMT KBP 220 kV i <-> NMT KBP 220 kV i
SMT KBP 220 kV i <-> kraj,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
NMT KBP 220 kV i:
UEEO <-> NMT KBP 220 kV i,
NMT KBP 220 kV i <-> SMT KBP 220 kV i,
NMT KBP 220 kV i <-> kraj,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, 
i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
SR KBP 110 kV i GSS j:
GSS 110 kV j <-> SR KBP 110 kV i GSS j <-> P KBP 110 kV i,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_KBP 110 kV, n_GSS 110 kV∈N0;
P KBP 110 kV i:
SR KBP 110 kV i GSS j <-> P KBP 110 kV i <-> SMT KBP 110 kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_KBP 110 kV, n_GSS 110 kV∈N0;
IRSU KBP 110 kV i:
SMT KBP 110 kV i <-> IRSU KBP 110 kV i,
IRSU KBP 110 kV i <-> NMT KBP 110 kV i,
IRSU KBP 110 kV i <-> kraj,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
SMT KBP 110 kV i:
P KBP 110 kV i <-> SMT KBP 110 kV i <-> IRSU KBP 110 kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
NMT KBP 110 kV i:
UEEO <-> NMT KBP 110 kV i,
NMT KBP 110 kV i <-> IRSU KBP 110 kV i,
NMT KBP 110 kV i <-> kraj,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
SR KBP 110 kV i PSS k:
PSS 110 kV k <-> SR KBP 110 kV i PSS k,
SR KBP 110 kV i PSS k <-> IRSU KBP 110 kV i,
SR KBP 110 kV i PSS k <-> SMT KBP 110 kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_KBP 110 kV, n_PSS 110 kV∈N0;
P KBP 110 kV i:
SR KBP 110 kV i GSS j <-> P KBP 110 kV i <-> IRSU KBP 110 kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_KBP 110 kV, n_GSS 110 kV∈N0;
IRSU KBP 110 kV i:
P KBP 110 kV i <-> IRSU KBP 110 kV i,
IRSU KBP 110 kV i <-> SR KBP 110 kV i PSS k,
IRSU KBP 110 kV i <-> SMT KBP 110 kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_KBP 110 kV, n_PSS 110 kV∈N0;
SMT KBP 110 kV i:
IRSU KBP 110 kV i <-> SMT KBP 110 kV i,
SR KBP 110 kV i PSS k <-> SMT KBP 110 kV i,
SMT KBP 110 kV i <-> NMT KBP 110 kV i
SMT KBP 110 kV i <-> kraj,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
NMT KBP 110 kV i:
UEEO <-> NMT KBP 110 kV i,
NMT KBP 110 kV i <-> SMT KBP 110 kV i,
NMT KBP 110 kV i <-> kraj,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, 
i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
SR KBP x kV i GSS j:
GSS x kV j <-> SR KBP x kV i GSS j <-> P KBP x kV i,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_KBP x kV, n_GSS x kV∈N0;
P KBP x kV i:
SR KBP x kV i GSS j <-> P KBP x kV i <-> SMT KBP x kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_KBP x kV, n_GSS x kV∈N0;
IRSU KBP x kV i:
SMT KBP x kV i <-> IRSU KBP x kV i,
IRSU KBP x kV i <-> NMT KBP x kV i,
IRSU KBP x kV i <-> kraj,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
SMT KBP x kV i:
P KBP x kV i <-> SMT KBP x kV i <-> IRSU KBP x kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
NMT KBP x kV i:
UEEO <-> NMT KBP x kV i,
NMT KBP x kV i <-> IRSU KBP x kV i,
NMT KBP x kV i <-> kraj,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
SR KBP x kV i PSS k:
PSS x kV k <-> SR KBP x kV i PSS k,
SR KBP x kV i PSS k <-> IRSU KBP x kV i,
SR KBP x kV i PSS k <-> SMT KBP x kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_KBP x kV, n_PSS x kV∈N0;
P KBP x kV i:
SR KBP x kV i GSS j <-> P KBP x kV i <-> IRSU KBP x kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_KBP x kV, n_GSS x kV∈N0;
IRSU KBP x kV i:
P KBP x kV i <-> IRSU KBP x kV i,
IRSU KBP x kV i <-> SR KBP x kV i PSS k,
IRSU KBP x kV i <-> SMT KBP x kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_KBP x kV, n_PSS x kV∈N0;
SMT KBP x kV i:
IRSU KBP x kV i <-> SMT KBP x kV i,
SR KBP x kV i PSS k <-> SMT KBP x kV i,
SMT KBP x kV i <-> NMT KBP x kV i
SMT KBP x kV i <-> kraj,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
NMT KBP x kV i:
UEEO <-> NMT KBP x kV i,
NMT KBP x kV i <-> SMT KBP x kV i,
NMT KBP x kV i <-> kraj,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, 
i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
SR TRPVN TR 400/220 kV/kV i GSS j:
GSS 400 kV j <-> SR TRPVN TR 400/220 kV/kV i GSS j <-> P TRPVN TR 400/220 kV/kV i,
gde i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/220 kV/kV, n_GSS 400 kV∈N0;
P TRPVN TR 400/220 kV/kV i:
SR TRPVN TR 400/220 kV/kV i GSS j <-> P TRPVN TR 400/220 kV/kV i <-> SMT TRPVN TR 400/220 kV/kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/220 kV/kV, n_GSS 400 kV∈N0;
SMT TRPVN TR 400/220 kV/kV i:
P TRPVN TR 400/220 kV/kV i <-> SMT TRPVN TR 400/220 kV/kV i,
SMT TRPVN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i,
SMT TRPVN TR 400/220 kV/kV i <-> OP TRPVN TR 400/220 kV/kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
OP TRPVN TR 400/220 kV/kV i:
UEEO <-> OP TRPVN TR 400/220 kV/kV i,
OP TRPVN TR 400/220 kV/kV i <-> SMT TRPVN TR 400/220 kV/kV i,
OP TRPVN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i,
gde i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
IR TRPVN TR 400/220 kV/kV i:
P TRPVN TR 400/220 kV/kV i <-> IR TRPVN TR 400/220 kV/kV i,
IR TRPVN TR 400/220 kV/kV i <-> SMT TRPVN TR 400/220 kV/kV i,
IR TRPVN TR 400/220 kV/kV i <-> SR TRPVN TR 400/220 kV/kV i PSS k,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
SR TRPVN TR 400/220 kV/kV i PSS k:
PSS 400 kV k <-> SR TRPVN TR 400/220 kV/kV i PSS k,
SR TRPVN TR 400/220 kV/kV i PSS k <-> IR TRPVN TR 400/220 kV/kV i,
SR TRPVN TR 400/220 kV/kV i PSS k <-> SMT TRPVN TR 400/220 kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, 
k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/220 kV/kV, n_PSS 400 kV∈N0;
P TRPVN TR 400/220 kV/kV i:
SR TRPVN TR 400/220 kV/kV i GSS j <-> P TRPVN TR 400/220 kV/kV i <-> IR TRPVN TR 400/220 kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/220 kV/kV, n_GSS 400 kV∈N0;
SMT TRPVN TR 400/220 kV/kV i:
IR TRPVN TR 400/220 kV/kV i <-> SMT TRPVN TR 400/220 kV/kV i,
SR TRPVN TR 400/220 kV/kV i PSS k <-> SMT TRPVN TR 400/220 kV/kV i,
SMT TRPVN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i
SMT TRPVN TR 400/220 kV/kV i <-> OP TRPVN TR 400/220 kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
SR TRPVN TR 400/110 kV/kV i GSS j:
GSS 400 kV j <-> SR TRPVN TR 400/110 kV/kV i GSS j <-> P TRPVN TR 400/110 kV/kV i,
gde i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/110 kV/kV, n_GSS 400 kV∈N0;
P TRPVN TR 400/110 kV/kV i:
SR TRPVN TR 400/110 kV/kV i GSS j <-> P TRPVN TR 400/110 kV/kV i <-> SMT TRPVN TR 400/110 kV/kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/110 kV/kV, n_GSS 400 kV∈N0;
SMT TRPVN TR 400/110 kV/kV i:
P TRPVN TR 400/110 kV/kV i <-> SMT TRPVN TR 400/110 kV/kV i,
SMT TRPVN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i,
SMT TRPVN TR 400/110 kV/kV i <-> OP TRPVN TR 400/110 kV/kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
OP TRPVN TR 400/110 kV/kV i:
UEEO <-> OP TRPVN TR 400/110 kV/kV i,
OP TRPVN TR 400/110 kV/kV i <-> SMT TRPVN TR 400/110 kV/kV i,
OP TRPVN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i,
gde i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
IR TRPVN TR 400/110 kV/kV i:
P TRPVN TR 400/110 kV/kV i <-> IR TRPVN TR 400/110 kV/kV i,
IR TRPVN TR 400/110 kV/kV i <-> SMT TRPVN TR 400/110 kV/kV i,
IR TRPVN TR 400/110 kV/kV i <-> SR TRPVN TR 400/110 kV/kV i PSS k,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
SR TRPVN TR 400/110 kV/kV i PSS k:
PSS 400 kV k <-> SR TRPVN TR 400/110 kV/kV i PSS k,
SR TRPVN TR 400/110 kV/kV i PSS k <-> IR TRPVN TR 400/110 kV/kV i,
SR TRPVN TR 400/110 kV/kV i PSS k <-> SMT TRPVN TR 400/110 kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, 
k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/110 kV/kV, n_PSS 400 kV∈N0;
P TRPVN TR 400/110 kV/kV i:
SR TRPVN TR 400/110 kV/kV i GSS j <-> P TRPVN TR 400/110 kV/kV i <-> IR TRPVN TR 400/110 kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/110 kV/kV, n_GSS 400 kV∈N0;
SMT TRPVN TR 400/110 kV/kV i:
IR TRPVN TR 400/110 kV/kV i <-> SMT TRPVN TR 400/110 kV/kV i,
SR TRPVN TR 400/110 kV/kV i PSS k <-> SMT TRPVN TR 400/110 kV/kV i,
SMT TRPVN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i
SMT TRPVN TR 400/110 kV/kV i <-> OP TRPVN TR 400/110 kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
SR TRPVN TR 220/110 kV/kV i GSS j:
GSS 220 kV j <-> SR TRPVN TR 220/110 kV/kV i GSS j <-> P TRPVN TR 220/110 kV/kV i,
gde i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/110 kV/kV, n_GSS 220 kV∈N0;
P TRPVN TR 220/110 kV/kV i:
SR TRPVN TR 220/110 kV/kV i GSS j <-> P TRPVN TR 220/110 kV/kV i <-> SMT TRPVN TR 220/110 kV/kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/110 kV/kV, n_GSS 220 kV∈N0;
SMT TRPVN TR 220/110 kV/kV i:
P TRPVN TR 220/110 kV/kV i <-> SMT TRPVN TR 220/110 kV/kV i,
SMT TRPVN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i,
SMT TRPVN TR 220/110 kV/kV i <-> OP TRPVN TR 220/110 kV/kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0
OP TRPVN TR 220/110 kV/kV i:
UEEO <-> OP TRPVN TR 220/110 kV/kV i,
OP TRPVN TR 220/110 kV/kV i <-> SMT TRPVN TR 220/110 kV/kV i,
OP TRPVN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i,
gde i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
IR TRPVN TR 220/110 kV/kV i:
P TRPVN TR 220/110 kV/kV i <-> IR TRPVN TR 220/110 kV/kV i,
IR TRPVN TR 220/110 kV/kV i <-> SMT TRPVN TR 220/110 kV/kV i,
IR TRPVN TR 220/110 kV/kV i <-> SR TRPVN TR 220/110 kV/kV i PSS k,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
SR TRPVN TR 220/110 kV/kV i PSS k:
PSS 220 kV k <-> SR TRPVN TR 220/110 kV/kV i PSS k,
SR TRPVN TR 220/110 kV/kV i PSS k <-> IR TRPVN TR 220/110 kV/kV i,
SR TRPVN TR 220/110 kV/kV i PSS k <-> SMT TRPVN TR 220/110 kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPVN TR 220/110 kV/kV, n_PSS 220 kV∈N0;
P TRPVN TR 220/110 kV/kV i:
SR TRPVN TR 220/110 kV/kV i GSS j <-> P TRPVN TR 220/110 kV/kV i <-> IR TRPVN TR 220/110 kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/110 kV/kV, n_GSS 220 kV∈N0;
SMT TRPVN TR 220/110 kV/kV i:
IR TRPVN TR 220/110 kV/kV i <-> SMT TRPVN TR 220/110 kV/kV i,
SR TRPVN TR 220/110 kV/kV i PSS k <-> SMT TRPVN TR 220/110 kV/kV i,
SMT TRPVN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i
SMT TRPVN TR 220/110 kV/kV i <-> OP TRPVN TR 220/110 kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
SR TRPVN TR 400/x kV/kV i GSS j:
GSS 400 kV j <-> SR TRPVN TR 400/x kV/kV i GSS j <-> P TRPVN TR 400/x kV/kV i,
gde i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/x kV/kV, n_GSS 400 kV∈N0;
P TRPVN TR 400/x kV/kV i:
SR TRPVN TR 400/x kV/kV i GSS j <-> P TRPVN TR 400/x kV/kV i <-> SMT TRPVN TR 400/x kV/kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/x kV/kV, n_GSS 400 kV∈N0;
SMT TRPVN TR 400/x kV/kV i:
P TRPVN TR 400/x kV/kV i <-> SMT TRPVN TR 400/x kV/kV i,
SMT TRPVN TR 400/x kV/kV i <-> TR 400/x kV/kV i,
SMT TRPVN TR 400/x kV/kV i <-> OP TRPVN TR 400/x kV/kV i,
uz uslov da je n_PSS 400 kV = 0,
gde i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
OP TRPVN TR 400/x kV/kV i:
UEEO <-> OP TRPVN TR 400/x kV/kV i,
OP TRPVN TR 400/x kV/kV i <-> SMT TRPVN TR 400/x kV/kV i,
OP TRPVN TR 400/x kV/kV i <-> TR 400/x kV/kV i,
gde i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
IR TRPVN TR 400/x kV/kV i:
P TRPVN TR 400/x kV/kV i <-> IR TRPVN TR 400/x kV/kV i,
IR TRPVN TR 400/x kV/kV i <-> SMT TRPVN TR 400/x kV/kV i,
IR TRPVN TR 400/x kV/kV i <-> SR TRPVN TR 400/x kV/kV i PSS k,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
SR TRPVN TR 400/x kV/kV i PSS k:
PSS 400 kV k <-> SR TRPVN TR 400/x kV/kV i PSS k,
SR TRPVN TR 400/x kV/kV i PSS k <-> IR TRPVN TR 400/x kV/kV i,
SR TRPVN TR 400/x kV/kV i PSS k <-> SMT TRPVN TR 400/x kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, 
k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/x kV/kV, n_PSS 400 kV∈N0;
P TRPVN TR 400/x kV/kV i:
SR TRPVN TR 400/x kV/kV i GSS j <-> P TRPVN TR 400/x kV/kV i <-> IR TRPVN TR 400/x kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/x kV/kV, n_GSS 400 kV∈N0;
SMT TRPVN TR 400/x kV/kV i:
IR TRPVN TR 400/x kV/kV i <-> SMT TRPVN TR 400/x kV/kV i,
SR TRPVN TR 400/x kV/kV i PSS k <-> SMT TRPVN TR 400/x kV/kV i,
SMT TRPVN TR 400/x kV/kV i <-> TR 400/x kV/kV i
SMT TRPVN TR 400/x kV/kV i <-> OP TRPVN TR 400/x kV/kV i,
uz uslov da je n_PSS 400 kV > 0,
gde i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
SR TRPVN TR 220/x kV/kV i GSS j:
GSS 220 kV j <-> SR TRPVN TR 220/x kV/kV i GSS j <-> P TRPVN TR 220/x kV/kV i,
gde i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/x kV/kV, n_GSS 220 kV∈N0;
P TRPVN TR 220/x kV/kV i:
SR TRPVN TR 220/x kV/kV i GSS j <-> P TRPVN TR 220/x kV/kV i <-> SMT TRPVN TR 220/x kV/kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/x kV/kV, n_GSS 220 kV∈N0;
SMT TRPVN TR 220/x kV/kV i:
P TRPVN TR 220/x kV/kV i <-> SMT TRPVN TR 220/x kV/kV i,
SMT TRPVN TR 220/x kV/kV i <-> TR 220/x kV/kV i,
SMT TRPVN TR 220/x kV/kV i <-> OP TRPVN TR 220/x kV/kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0
OP TRPVN TR 220/x kV/kV i:
UEEO <-> OP TRPVN TR 220/x kV/kV i,
OP TRPVN TR 220/x kV/kV i <-> SMT TRPVN TR 220/x kV/kV i,
OP TRPVN TR 220/x kV/kV i <-> TR 220/x kV/kV i,
gde i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
IR TRPVN TR 220/x kV/kV i:
P TRPVN TR 220/x kV/kV i <-> IR TRPVN TR 220/x kV/kV i,
IR TRPVN TR 220/x kV/kV i <-> SMT TRPVN TR 220/x kV/kV i,
IR TRPVN TR 220/x kV/kV i <-> SR TRPVN TR 220/x kV/kV i PSS k,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
SR TRPVN TR 220/x kV/kV i PSS k:
PSS 220 kV k <-> SR TRPVN TR 220/x kV/kV i PSS k,
SR TRPVN TR 220/x kV/kV i PSS k <-> IR TRPVN TR 220/x kV/kV i,
SR TRPVN TR 220/x kV/kV i PSS k <-> SMT TRPVN TR 220/x kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPVN TR 220/x kV/kV, n_PSS 220 kV∈N0;
P TRPVN TR 220/x kV/kV i:
SR TRPVN TR 220/x kV/kV i GSS j <-> P TRPVN TR 220/x kV/kV i <-> IR TRPVN TR 220/x kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/x kV/kV, n_GSS 220 kV∈N0;
SMT TRPVN TR 220/x kV/kV i:
IR TRPVN TR 220/x kV/kV i <-> SMT TRPVN TR 220/x kV/kV i,
SR TRPVN TR 220/x kV/kV i PSS k <-> SMT TRPVN TR 220/x kV/kV i,
SMT TRPVN TR 220/x kV/kV i <-> TR 220/x kV/kV i
SMT TRPVN TR 220/x kV/kV i <-> OP TRPVN TR 220/x kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
SR TRPVN TR 110/x kV/kV i GSS j:
GSS 110 kV j <-> SR TRPVN TR 110/x kV/kV i GSS j <-> P TRPVN TR 110/x kV/kV i,
gde i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPVN TR 110/x kV/kV, n_GSS 110 kV∈N0;
P TRPVN TR 110/x kV/kV i:
SR TRPVN TR 110/x kV/kV i GSS j <-> P TRPVN TR 110/x kV/kV i <-> SMT TRPVN TR 110/x kV/kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPVN TR 110/x kV/kV, n_GSS 110 kV∈N0;
SMT TRPVN TR 110/x kV/kV i:
P TRPVN TR 110/x kV/kV i <-> SMT TRPVN TR 110/x kV/kV i,
SMT TRPVN TR 110/x kV/kV i <-> TR 110/x kV/kV i,
SMT TRPVN TR 110/x kV/kV i <-> OP TRPVN TR 110/x kV/kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
OP TRPVN TR 110/x kV/kV i:
UEEO <-> OP TRPVN TR 110/x kV/kV i,
OP TRPVN TR 110/x kV/kV i <-> SMT TRPVN TR 110/x kV/kV i,
OP TRPVN TR 110/x kV/kV i <-> TR 110/x kV/kV i,
gde i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
IR TRPVN TR 110/x kV/kV i:
P TRPVN TR 110/x kV/kV i <-> IR TRPVN TR 110/x kV/kV i,
IR TRPVN TR 110/x kV/kV i <-> SMT TRPVN TR 110/x kV/kV i,
IR TRPVN TR 110/x kV/kV i <-> SR TRPVN TR 110/x kV/kV i PSS k,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
SR TRPVN TR 110/x kV/kV i PSS k:
PSS 110 kV k <-> SR TRPVN TR 110/x kV/kV i PSS k,
SR TRPVN TR 110/x kV/kV i PSS k <-> IR TRPVN TR 110/x kV/kV i,
SR TRPVN TR 110/x kV/kV i PSS k <-> SMT TRPVN TR 110/x kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPVN TR 110/x kV/kV, n_PSS 110 kV∈N0;
P TRPVN TR 110/x kV/kV i:
SR TRPVN TR 110/x kV/kV i GSS j <-> P TRPVN TR 110/x kV/kV i <-> IR TRPVN TR 110/x kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPVN TR 110/x kV/kV, n_GSS 110 kV∈N0;
SMT TRPVN TR 110/x kV/kV i:
IR TRPVN TR 110/x kV/kV i <-> SMT TRPVN TR 110/x kV/kV i,
SR TRPVN TR 110/x kV/kV i PSS k <-> SMT TRPVN TR 110/x kV/kV i,
SMT TRPVN TR 110/x kV/kV i <-> TR 110/x kV/kV i
SMT TRPVN TR 110/x kV/kV i <-> OP TRPVN TR 110/x kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
SR TRPNN TR 400/220 kV/kV i GSS j:
GSS 220 kV j <-> SR TRPNN TR 400/220 kV/kV i GSS j <-> P TRPNN TR 400/220 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_GSS 220 kV∈N0;
P TRPNN TR 400/220 kV/kV i:
SR TRPNN TR 400/220 kV/kV i GSS j <-> P TRPNN TR 400/220 kV/kV i <-> SMT TRPNN TR 400/220 kV/kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_GSS 220 kV∈N0;
SMT TRPNN TR 400/220 kV/kV i:
P TRPNN TR 400/220 kV/kV i <-> SMT TRPNN TR 400/220 kV/kV i,
SMT TRPNN TR 400/220 kV/kV i <-> NMT TRPNN TR 400/220 kV/kV i,
SMT TRPNN TR 400/220 kV/kV i <-> OP TRPNN TR 400/220 kV/kV i,
SMT TRPNN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i,
uz uslov da je n_PSS 220 kV = 0,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
NMT TRPNN TR 400/220 kV/kV i:
UEEO <-> NMT TRPNN TR 400/220 kV/kV i,
NMT TRPNN TR 400/220 kV/kV i <-> SMT TRPNN TR 400/220 kV/kV i,
NMT TRPNN TR 400/220 kV/kV i <-> OP TRPNN TR 400/220 kV/kV i,
NMT TRPNN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
OP TRPNN TR 400/220 kV/kV i:
UEEO <-> OP TRPNN TR 400/220 kV/kV i,
OP TRPNN TR 400/220 kV/kV i <-> SMT TRPNN TR 400/220 kV/kV i,
OP TRPNN TR 400/220 kV/kV i <-> NMT TRPNN TR 400/220 kV/kV i,
OP TRPNN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
SR TRPNN TR 400/220 kV/kV i PSS k:
PSS 220 kV k <-> SR TRPNN TR 400/220 kV/kV i PSS k,
SR TRPNN TR 400/220 kV/kV i PSS k <-> IR TRPNN TR 400/220 kV/kV i,
SR TRPNN TR 400/220 kV/kV i PSS k <-> SMT TRPNN TR 400/220 kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_PSS 220 kV∈N0;
IR TRPNN TR 400/220 kV/kV i:
P TRPNN TR 400/220 kV/kV i <-> IR TRPNN TR 400/220 kV/kV i,
IR TRPNN TR 400/220 kV/kV i <-> SMT TRPNN TR 400/220 kV/kV i,
IR TRPNN TR 400/220 kV/kV i <-> SR TRPNN TR 400/220 kV/kV i PSS k,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_PSS 220 kV∈N0;
P TRPNN TR 400/220 kV/kV i:
SR TRPNN TR 400/220 kV/kV i GSS j <-> P TRPNN TR 400/220 kV/kV i <-> IR TRPNN TR 400/220 kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_GSS 220 kV∈N0;
SMT TRPNN TR 400/220 kV/kV i:
IR TRPNN TR 400/220 kV/kV i <-> SMT TRPNN TR 400/220 kV/kV i,
SR TRPNN TR 400/220 kV/kV i PSS k <-> SMT TRPNN TR 400/220 kV/kV i,
SMT TRPNN TR 400/220 kV/kV i <-> NMT TRPNN TR 400/220 kV/kV i,
SMT TRPNN TR 400/220 kV/kV i <-> OP TRPNN TR 400/220 kV/kV i,
SMT TRPNN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i,
uz uslov da je n_PSS 220 kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
SR TRPNN TR 400/110 kV/kV i GSS j:
GSS 110 kV j <-> SR TRPNN TR 400/110 kV/kV i GSS j <-> P TRPNN TR 400/110 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_GSS 110 kV∈N0;
P TRPNN TR 400/110 kV/kV i:
SR TRPNN TR 400/110 kV/kV i GSS j <-> P TRPNN TR 400/110 kV/kV i <-> SMT TRPNN TR 400/110 kV/kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_GSS 110 kV∈N0;
SMT TRPNN TR 400/110 kV/kV i:
P TRPNN TR 400/110 kV/kV i <-> SMT TRPNN TR 400/110 kV/kV i,
SMT TRPNN TR 400/110 kV/kV i <-> NMT TRPNN TR 400/110 kV/kV i,
SMT TRPNN TR 400/110 kV/kV i <-> OP TRPNN TR 400/110 kV/kV i,
SMT TRPNN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
NMT TRPNN TR 400/110 kV/kV i:
UEEO <-> NMT TRPNN TR 400/110 kV/kV i,
NMT TRPNN TR 400/110 kV/kV i <-> SMT TRPNN TR 400/110 kV/kV i,
NMT TRPNN TR 400/110 kV/kV i <-> OP TRPNN TR 400/110 kV/kV i,
NMT TRPNN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
OP TRPNN TR 400/110 kV/kV i:
UEEO <-> OP TRPNN TR 400/110 kV/kV i,
OP TRPNN TR 400/110 kV/kV i <-> SMT TRPNN TR 400/110 kV/kV i,
OP TRPNN TR 400/110 kV/kV i <-> NMT TRPNN TR 400/110 kV/kV i,
OP TRPNN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
SR TRPNN TR 400/110 kV/kV i PSS k:
PSS 110 kV k <-> SR TRPNN TR 400/110 kV/kV i PSS k,
SR TRPNN TR 400/110 kV/kV i PSS k <-> IR TRPNN TR 400/110 kV/kV i,
SR TRPNN TR 400/110 kV/kV i PSS k <-> SMT TRPNN TR 400/110 kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_PSS 110 kV∈N0;
IR TRPNN TR 400/110 kV/kV i:
P TRPNN TR 400/110 kV/kV i <-> IR TRPNN TR 400/110 kV/kV i,
IR TRPNN TR 400/110 kV/kV i <-> SMT TRPNN TR 400/110 kV/kV i,
IR TRPNN TR 400/110 kV/kV i <-> SR TRPNN TR 400/110 kV/kV i PSS k,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_PSS 110 kV∈N0;
P TRPNN TR 400/110 kV/kV i:
SR TRPNN TR 400/110 kV/kV i GSS j <-> P TRPNN TR 400/110 kV/kV i <-> IR TRPNN TR 400/110 kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_GSS 110 kV∈N0;
SMT TRPNN TR 400/110 kV/kV i:
IR TRPNN TR 400/110 kV/kV i <-> SMT TRPNN TR 400/110 kV/kV i,
SR TRPNN TR 400/110 kV/kV i PSS k <-> SMT TRPNN TR 400/110 kV/kV i,
SMT TRPNN TR 400/110 kV/kV i <-> NMT TRPNN TR 400/110 kV/kV i,
SMT TRPNN TR 400/110 kV/kV i <-> OP TRPNN TR 400/110 kV/kV i,
SMT TRPNN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
SR TRPNN TR 220/110 kV/kV i GSS j:
GSS 110 kV j <-> SR TRPNN TR 220/110 kV/kV i GSS j <-> P TRPNN TR 220/110 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_GSS 110 kV∈N0;
P TRPNN TR 220/110 kV/kV i:
SR TRPNN TR 220/110 kV/kV i GSS j <-> P TRPNN TR 220/110 kV/kV i <-> SMT TRPNN TR 220/110 kV/kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_GSS 110 kV∈N0;
SMT TRPNN TR 220/110 kV/kV i:
P TRPNN TR 220/110 kV/kV i <-> SMT TRPNN TR 220/110 kV/kV i,
SMT TRPNN TR 220/110 kV/kV i <-> NMT TRPNN TR 220/110 kV/kV i,
SMT TRPNN TR 220/110 kV/kV i <-> OP TRPNN TR 220/110 kV/kV i,
SMT TRPNN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i,
uz uslov da je n_PSS 110 kV = 0,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
NMT TRPNN TR 220/110 kV/kV i:
UEEO <-> NMT TRPNN TR 220/110 kV/kV i,
NMT TRPNN TR 220/110 kV/kV i <-> SMT TRPNN TR 220/110 kV/kV i,
NMT TRPNN TR 220/110 kV/kV i <-> OP TRPNN TR 220/110 kV/kV i,
NMT TRPNN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
OP TRPNN TR 220/110 kV/kV i:
UEEO <-> OP TRPNN TR 220/110 kV/kV i,
OP TRPNN TR 220/110 kV/kV i <-> SMT TRPNN TR 220/110 kV/kV i,
OP TRPNN TR 220/110 kV/kV i <-> NMT TRPNN TR 220/110 kV/kV i,
OP TRPNN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
SR TRPNN TR 220/110 kV/kV i PSS k:
PSS 110 kV k <-> SR TRPNN TR 220/110 kV/kV i PSS k,
SR TRPNN TR 220/110 kV/kV i PSS k <-> IR TRPNN TR 220/110 kV/kV i,
SR TRPNN TR 220/110 kV/kV i PSS k <-> SMT TRPNN TR 220/110 kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_PSS 110 kV∈N0;
IR TRPNN TR 220/110 kV/kV i:
P TRPNN TR 220/110 kV/kV i <-> IR TRPNN TR 220/110 kV/kV i,
IR TRPNN TR 220/110 kV/kV i <-> SMT TRPNN TR 220/110 kV/kV i,
IR TRPNN TR 220/110 kV/kV i <-> SR TRPNN TR 220/110 kV/kV i PSS k,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_PSS 110 kV∈N0;
P TRPNN TR 220/110 kV/kV i:
SR TRPNN TR 220/110 kV/kV i GSS j <-> P TRPNN TR 220/110 kV/kV i <-> IR TRPNN TR 220/110 kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_GSS 110 kV∈N0;
SMT TRPNN TR 220/110 kV/kV i:
IR TRPNN TR 220/110 kV/kV i <-> SMT TRPNN TR 220/110 kV/kV i,
SR TRPNN TR 220/110 kV/kV i PSS k <-> SMT TRPNN TR 220/110 kV/kV i,
SMT TRPNN TR 220/110 kV/kV i <-> NMT TRPNN TR 220/110 kV/kV i,
SMT TRPNN TR 220/110 kV/kV i <-> OP TRPNN TR 220/110 kV/kV i,
SMT TRPNN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i,
uz uslov da je n_PSS 110 kV > 0,
gde i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
SR TRPNN TR 400/x kV/kV i GSS j:
GSS x kV j <-> SR TRPNN TR 400/x kV/kV i GSS j <-> P TRPNN TR 400/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_GSS x kV∈N0;
P TRPNN TR 400/x kV/kV i:
SR TRPNN TR 400/x kV/kV i GSS j <-> P TRPNN TR 400/x kV/kV i <-> SMT TRPNN TR 400/x kV/kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_GSS x kV∈N0;
SMT TRPNN TR 400/x kV/kV i:
P TRPNN TR 400/x kV/kV i <-> SMT TRPNN TR 400/x kV/kV i,
SMT TRPNN TR 400/x kV/kV i <-> NMT TRPNN TR 400/x kV/kV i,
SMT TRPNN TR 400/x kV/kV i <-> OP TRPNN TR 400/x kV/kV i,
SMT TRPNN TR 400/x kV/kV i <-> TR 400/x kV/kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
NMT TRPNN TR 400/x kV/kV i:
UEEO <-> NMT TRPNN TR 400/x kV/kV i,
NMT TRPNN TR 400/x kV/kV i <-> SMT TRPNN TR 400/x kV/kV i,
NMT TRPNN TR 400/x kV/kV i <-> OP TRPNN TR 400/x kV/kV i,
NMT TRPNN TR 400/x kV/kV i <-> TR 400/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
OP TRPNN TR 400/x kV/kV i:
UEEO <-> OP TRPNN TR 400/x kV/kV i,
OP TRPNN TR 400/x kV/kV i <-> SMT TRPNN TR 400/x kV/kV i,
OP TRPNN TR 400/x kV/kV i <-> NMT TRPNN TR 400/x kV/kV i,
OP TRPNN TR 400/x kV/kV i <-> TR 400/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
SR TRPNN TR 400/x kV/kV i PSS k:
PSS x kV k <-> SR TRPNN TR 400/x kV/kV i PSS k,
SR TRPNN TR 400/x kV/kV i PSS k <-> IR TRPNN TR 400/x kV/kV i,
SR TRPNN TR 400/x kV/kV i PSS k <-> SMT TRPNN TR 400/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 400/x kV/kV i:
P TRPNN TR 400/x kV/kV i <-> IR TRPNN TR 400/x kV/kV i,
IR TRPNN TR 400/x kV/kV i <-> SMT TRPNN TR 400/x kV/kV i,
IR TRPNN TR 400/x kV/kV i <-> SR TRPNN TR 400/x kV/kV i PSS k,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_PSS x kV∈N0;
P TRPNN TR 400/x kV/kV i:
SR TRPNN TR 400/x kV/kV i GSS j <-> P TRPNN TR 400/x kV/kV i <-> IR TRPNN TR 400/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_GSS x kV∈N0;
SMT TRPNN TR 400/x kV/kV i:
IR TRPNN TR 400/x kV/kV i <-> SMT TRPNN TR 400/x kV/kV i,
SR TRPNN TR 400/x kV/kV i PSS k <-> SMT TRPNN TR 400/x kV/kV i,
SMT TRPNN TR 400/x kV/kV i <-> NMT TRPNN TR 400/x kV/kV i,
SMT TRPNN TR 400/x kV/kV i <-> OP TRPNN TR 400/x kV/kV i,
SMT TRPNN TR 400/x kV/kV i <-> TR 400/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;

SR TRPNN TR 220/x kV/kV i GSS j:
GSS x kV j <-> SR TRPNN TR 220/x kV/kV i GSS j <-> P TRPNN TR 220/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_GSS x kV∈N0;
P TRPNN TR 220/x kV/kV i:
SR TRPNN TR 220/x kV/kV i GSS j <-> P TRPNN TR 220/x kV/kV i <-> SMT TRPNN TR 220/x kV/kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_GSS x kV∈N0;
SMT TRPNN TR 220/x kV/kV i:
P TRPNN TR 220/x kV/kV i <-> SMT TRPNN TR 220/x kV/kV i,
SMT TRPNN TR 220/x kV/kV i <-> NMT TRPNN TR 220/x kV/kV i,
SMT TRPNN TR 220/x kV/kV i <-> OP TRPNN TR 220/x kV/kV i,
SMT TRPNN TR 220/x kV/kV i <-> TR 220/x kV/kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
NMT TRPNN TR 220/x kV/kV i:
UEEO <-> NMT TRPNN TR 220/x kV/kV i,
NMT TRPNN TR 220/x kV/kV i <-> SMT TRPNN TR 220/x kV/kV i,
NMT TRPNN TR 220/x kV/kV i <-> OP TRPNN TR 220/x kV/kV i,
NMT TRPNN TR 220/x kV/kV i <-> TR 220/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
OP TRPNN TR 220/x kV/kV i:
UEEO <-> OP TRPNN TR 220/x kV/kV i,
OP TRPNN TR 220/x kV/kV i <-> SMT TRPNN TR 220/x kV/kV i,
OP TRPNN TR 220/x kV/kV i <-> NMT TRPNN TR 220/x kV/kV i,
OP TRPNN TR 220/x kV/kV i <-> TR 220/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
SR TRPNN TR 220/x kV/kV i PSS k:
PSS x kV k <-> SR TRPNN TR 220/x kV/kV i PSS k,
SR TRPNN TR 220/x kV/kV i PSS k <-> IR TRPNN TR 220/x kV/kV i,
SR TRPNN TR 220/x kV/kV i PSS k <-> SMT TRPNN TR 220/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 220/x kV/kV i:
P TRPNN TR 220/x kV/kV i <-> IR TRPNN TR 220/x kV/kV i,
IR TRPNN TR 220/x kV/kV i <-> SMT TRPNN TR 220/x kV/kV i,
IR TRPNN TR 220/x kV/kV i <-> SR TRPNN TR 220/x kV/kV i PSS k,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_PSS x kV∈N0;
P TRPNN TR 220/x kV/kV i:
SR TRPNN TR 220/x kV/kV i GSS j <-> P TRPNN TR 220/x kV/kV i <-> IR TRPNN TR 220/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_GSS x kV∈N0;
SMT TRPNN TR 220/x kV/kV i:
IR TRPNN TR 220/x kV/kV i <-> SMT TRPNN TR 220/x kV/kV i,
SR TRPNN TR 220/x kV/kV i PSS k <-> SMT TRPNN TR 220/x kV/kV i,
SMT TRPNN TR 220/x kV/kV i <-> NMT TRPNN TR 220/x kV/kV i,
SMT TRPNN TR 220/x kV/kV i <-> OP TRPNN TR 220/x kV/kV i,
SMT TRPNN TR 220/x kV/kV i <-> TR 220/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
SR TRPNN TR 110/x kV/kV i GSS j:
GSS x kV j <-> SR TRPNN TR 110/x kV/kV i GSS j <-> P TRPNN TR 110/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_GSS x kV∈N0;
P TRPNN TR 110/x kV/kV i:
SR TRPNN TR 110/x kV/kV i GSS j <-> P TRPNN TR 110/x kV/kV i <-> SMT TRPNN TR 110/x kV/kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_GSS x kV∈N0;
SMT TRPNN TR 110/x kV/kV i:
P TRPNN TR 110/x kV/kV i <-> SMT TRPNN TR 110/x kV/kV i,
SMT TRPNN TR 110/x kV/kV i <-> NMT TRPNN TR 110/x kV/kV i,
SMT TRPNN TR 110/x kV/kV i <-> OP TRPNN TR 110/x kV/kV i,
SMT TRPNN TR 110/x kV/kV i <-> TR 110/x kV/kV i,
uz uslov da je n_PSS x kV = 0,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
NMT TRPNN TR 110/x kV/kV i:
UEEO <-> NMT TRPNN TR 110/x kV/kV i,
NMT TRPNN TR 110/x kV/kV i <-> SMT TRPNN TR 110/x kV/kV i,
NMT TRPNN TR 110/x kV/kV i <-> OP TRPNN TR 110/x kV/kV i,
NMT TRPNN TR 110/x kV/kV i <-> TR 110/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
OP TRPNN TR 110/x kV/kV i:
UEEO <-> OP TRPNN TR 110/x kV/kV i,
OP TRPNN TR 110/x kV/kV i <-> SMT TRPNN TR 110/x kV/kV i,
OP TRPNN TR 110/x kV/kV i <-> NMT TRPNN TR 110/x kV/kV i,
OP TRPNN TR 110/x kV/kV i <-> TR 110/x kV/kV i,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
SR TRPNN TR 110/x kV/kV i PSS k:
PSS x kV k <-> SR TRPNN TR 110/x kV/kV i PSS k,
SR TRPNN TR 110/x kV/kV i PSS k <-> IR TRPNN TR 110/x kV/kV i,
SR TRPNN TR 110/x kV/kV i PSS k <-> SMT TRPNN TR 110/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 110/x kV/kV i:
P TRPNN TR 110/x kV/kV i <-> IR TRPNN TR 110/x kV/kV i,
IR TRPNN TR 110/x kV/kV i <-> SMT TRPNN TR 110/x kV/kV i,
IR TRPNN TR 110/x kV/kV i <-> SR TRPNN TR 110/x kV/kV i PSS k,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_PSS x kV∈N0;
P TRPNN TR 110/x kV/kV i:
SR TRPNN TR 110/x kV/kV i GSS j <-> P TRPNN TR 110/x kV/kV i <-> IR TRPNN TR 110/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_GSS x kV∈N0;
SMT TRPNN TR 110/x kV/kV i:
IR TRPNN TR 110/x kV/kV i <-> SMT TRPNN TR 110/x kV/kV i,
SR TRPNN TR 110/x kV/kV i PSS k <-> SMT TRPNN TR 110/x kV/kV i,
SMT TRPNN TR 110/x kV/kV i <-> NMT TRPNN TR 110/x kV/kV i,
SMT TRPNN TR 110/x kV/kV i <-> OP TRPNN TR 110/x kV/kV i,
SMT TRPNN TR 110/x kV/kV i <-> TR 110/x kV/kV i,
uz uslov da je n_PSS x kV > 0,
gde i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
SR GSP 400 kV i GSS i:
GSS 400 kV i <-> SR GSP 400 kV i GSS i <-> P GSP 400 kV i,
gde i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, 
i∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
P GSP 400 kV i:
SR GSP 400 kV i GSS i <-> P GSP 400 kV i <-> SMT GSP 400 kV i,
gde i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, 
i∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
SMT GSP 400 kV i:
P GSP 400 kV i <-> SMT GSP 400 kV i <-> SR GSP 400 kV i GSS i+1,
gde i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, 
i∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
SR GSP 400 kV i GSS i+1:
SMT GSP 400 kV i <-> SR GSP 400 kV i GSS i+1 <-> GSS 400 kV i+1,
gde i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, 
i∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
SR GSP 220 kV i GSS i:
GSS 220 kV i <-> SR GSP 220 kV i GSS i <-> P GSP 220 kV i,
gde i∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, 
i∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
P GSP 220 kV i:
SR GSP 220 kV i GSS i <-> P GSP 220 kV i <-> SMT GSP 220 kV i,
gde i∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, 
i∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
SMT GSP 220 kV i:
P GSP 220 kV i <-> SMT GSP 220 kV i <-> GSS 220 kV i+1,
gde i∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, 
i∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
SR GSP 220 kV i GSS i+1:
SMT GSP 220 kV i <-> SR GSP 220 kV i GSS i+1 <-> GSS 220 kV i+1,
gde ∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, 
∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
SR GSP 110 kV i GSS i:
GSS 110 kV i <-> SR GSP 110 kV i GSS i <-> P GSP 110 kV i,
gde i∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, 
i∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
P GSP 110 kV i:
SR GSP 110 kV i GSS i <-> P GSP 110 kV i <-> SMT GSP 110 kV i,
gde i∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, 
i∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
SMT GSP 110 kV i:
P GSP 110 kV i <-> SMT GSP 110 kV i <-> GSS 110 kV i+1,
gde i∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, 
i∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
SR GSP 110 kV i GSS i+1:
SMT GSP 110 kV i <-> SR GSP 110 kV i GSS i+1 <-> GSS 110 kV i+1,
gde ∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, 
∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
SR GSP x kV i GSS i:
GSS x kV i <-> SR GSP x kV i GSS i <-> P GSP x kV i,
gde i∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, 
i∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
P GSP x kV i:
SR GSP x kV i GSS i <-> P GSP x kV i <-> SMT GSP x kV i,
gde i∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, 
i∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
SMT GSP x kV i:
P GSP x kV i <-> SMT GSP x kV i <-> GSS x kV i+1,
gde i∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, 
i∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
SR GSP x kV i GSS i+1:
SMT GSP x kV i <-> SR GSP x kV i GSS i+1 <-> GSS x kV i+1,
gde ∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, 
∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
SR PSP 400 kV i GSS j:
GSS 400 kV j <-> SR PSP 400 kV i GSS j <-> P PSP 400 kV i,
gde i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, 
i∈{0} ⟺ n_PSP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_PSP 400 kV, n_GSS 400 kV∈N0;
P PSP 400 kV i:
SR PSP 400 kV i GSS j <-> P PSP 400 kV i <-> SR PSP 400 kV i PSS i,
gde i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, 
i∈{0} ⟺ n_PSP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_PSP 400 kV, n_GSS 400 kV∈N0;
SR PSP 400 kV i PSS i:
P PSP 400 kV i <-> SR PSP 400 kV i PSS i <-> PSS 400 kV i,
gde i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, 
i∈{0} ⟺ n_PSP 400 kV=0, 
n_PSP 400 kV∈N0;
SR PSP 220 kV i GSS j:
GSS 220 kV j <-> SR PSP 220 kV i GSS j <-> P PSP 220 kV i,
gde i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, 
i∈{0} ⟺ n_PSP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_PSP 220 kV, n_GSS 220 kV∈N0;
P PSP 220 kV i:
SR PSP 220 kV i GSS j <-> P PSP 220 kV i <-> SR PSP 220 kV i PSS i,
gde i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, 
i∈{0} ⟺ n_PSP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_PSP 220 kV, n_GSS 220 kV∈N0;
SR PSP 220 kV i PSS i:
P PSP 220 kV i <-> SR PSP 220 kV i PSS i <-> PSS 220 kV i,
gde i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, 
i∈{0} ⟺ n_PSP 220 kV=0, 
n_PSP 220 kV∈N0;
SR PSP 110 kV i GSS j:
GSS 110 kV j <-> SR PSP 110 kV i GSS j <-> P PSP 110 kV i,
gde i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, 
i∈{0} ⟺ n_PSP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_PSP 110 kV, n_GSS 110 kV∈N0;
P PSP 110 kV i:
SR PSP 110 kV i GSS j <-> P PSP 110 kV i <-> SR PSP 110 kV i PSS i,
gde i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, 
i∈{0} ⟺ n_PSP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_PSP 110 kV, n_GSS 110 kV∈N0;
SR PSP 110 kV i PSS i:
P PSP 110 kV i <-> SR PSP 110 kV i PSS i <-> PSS 110 kV i,
gde i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, 
i∈{0} ⟺ n_PSP 110 kV=0, 
n_PSP 110 kV∈N0;
SR PSP x kV i GSS j:
GSS x kV j <-> SR PSP x kV i GSS j <-> P PSP x kV i,
gde i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, 
i∈{0} ⟺ n_PSP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_PSP x kV, n_GSS x kV∈N0;
P PSP x kV i:
SR PSP x kV i GSS j <-> P PSP x kV i <-> SR PSP x kV i PSS i,
gde i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, 
i∈{0} ⟺ n_PSP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_PSP x kV, n_GSS x kV∈N0;
SR PSP x kV i PSS i:
P PSP x kV i <-> SR PSP x kV i PSS i <-> PSS x kV i,
gde i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, 
i∈{0} ⟺ n_PSP x kV=0, 
n_PSP x kV∈N0;
TR 400/220 kV/kV i:
SMT TRPVN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i,
OP TRPVN TR 400/220 kV/kV i <-> TR 400/220 kV/kV i,
TR 400/220 kV/kV i <-> NMT TRPNN TR 400/220 kV/kV i,
TR 400/220 kV/kV i <-> SMT TRPNN TR 400/220 kV/kV i,
TR 400/220 kV/kV i <-> OP TRPNN TR 400/220 kV/kV i,
gde i∈{1, ..., n_TR 400/220 kV/kV} ⟺ n_TR 400/220 kV/kV>0, 
i∈{0} ⟺ n_TR 400/220 kV/kV=0, 
n_TR 400/220 kV/kV∈N0;
TR 400/110 kV/kV i:
SMT TRPVN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i,
OP TRPVN TR 400/110 kV/kV i <-> TR 400/110 kV/kV i,
TR 400/110 kV/kV i <-> SMT TRPNN TR 400/110 kV/kV i,
TR 400/110 kV/kV i <-> NMT TRPNN TR 400/110 kV/kV i,
TR 400/110 kV/kV i <-> OP TRPNN TR 400/110 kV/kV i,
gde i∈{1, ..., n_TR 400/110 kV/kV} ⟺ n_TR 400/110 kV/kV>0, 
i∈{0} ⟺ n_TR 400/110 kV/kV=0, 
n_TR 400/110 kV/kV∈N0;
TR 220/110 kV/kV i:
SMT TRPVN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i,
OP TRPVN TR 220/110 kV/kV i <-> TR 220/110 kV/kV i,
TR 220/110 kV/kV i <-> SMT TRPNN TR 220/110 kV/kV i,
TR 220/110 kV/kV i <-> NMT TRPNN TR 220/110 kV/kV i,
TR 220/110 kV/kV i <-> OP TRPNN TR 220/110 kV/kV i,
gde i∈{1, ..., n_TR 220/110 kV/kV} ⟺ n_TR 220/110 kV/kV>0, 
i∈{0} ⟺ n_TR 220/110 kV/kV=0, 
n_TR 220/110 kV/kV∈N0;
TR 400/x kV/kV i:
SMT TRPVN TR 400/x kV/kV i <-> TR 400/x kV/kV i,
OP TRPVN TR 400/x kV/kV i <-> TR 400/x kV/kV i,
TR 400/x kV/kV i <-> NMT TRPNN TR 400/x kV/kV i,
TR 400/x kV/kV i <-> SMT TRPNN TR 400/x kV/kV i,
TR 400/x kV/kV i <-> OP TRPNN TR 400/x kV/kV i,
gde i∈{1, ..., n_TR 400/x kV/kV} ⟺ n_TR 400/x kV/kV>0, 
i∈{0} ⟺ n_TR 400/x kV/kV=0, 
n_TR 400/x kV/kV∈N0;
TR 220/x kV/kV i:
SMT TRPVN TR 220/x kV/kV i <-> TR 220/x kV/kV i,
OP TRPVN TR 220/x kV/kV i <-> TR 220/x kV/kV i,
TR 220/x kV/kV i <-> NMT TRPNN TR 220/x kV/kV i,
TR 220/x kV/kV i <-> SMT TRPNN TR 220/x kV/kV i,
TR 220/x kV/kV i <-> OP TRPNN TR 220/x kV/kV i,
gde i∈{1, ..., n_TR 220/x kV/kV} ⟺ n_TR 220/x kV/kV>0, 
i∈{0} ⟺ n_TR 220/x kV/kV=0, 
n_TR 220/x kV/kV∈N0;
TR 110/x kV/kV i:
SMT TRPVN TR 110/x kV/kV i <-> TR 110/x kV/kV i,
OP TRPVN TR 110/x kV/kV i <-> TR 110/x kV/kV i,
TR 110/x kV/kV i <-> NMT TRPNN TR 110/x kV/kV i,
TR 110/x kV/kV i <-> SMT TRPNN TR 110/x kV/kV i,
TR 110/x kV/kV i <-> OP TRPNN TR 110/x kV/kV i,
gde i∈{1, ..., n_TR 110/x kV/kV} ⟺ n_TR 110/x kV/kV>0, 
i∈{0} ⟺ n_TR 110/x kV/kV=0, 
n_TR 110/x kV/kV∈N0;
GSS 400 kV j:
NMT GSS 400 kV j <-> GSS 400 kV j,
GSS 400 kV j <-> SR DVP 400 kV a1 GSS j,
GSS 400 kV j <-> SR KBP 400 kV a2 GSS j,
GSS 400 kV j <-> SR TRPVN TR 400/220 kV/kV a3 GSS j,
GSS 400 kV j <-> SR TRPVN TR 400/110 kV/kV a4 GSS j,
GSS 400 kV j <-> SR TRPVN TR 400/x kV/kV a5 GSS j,
GSS 400 kV j <-> SR GSP 400 kV a7 GSS j,
GSS 400 kV j <-> SR PSP 400 kV a6 GSS j,
gde a1∈{1, ..., n_DVP 400 KV} ⟺ n_DVP 400 KV>0, 
a1∈{0} ⟺ n_DVP 400 KV=0, 
a2∈{1, ..., n_KBP 400 KV} ⟺ n_KBP 400 KV>0, 
a2∈{0} ⟺ n_KBP 400 KV=0, 
a3∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
a3∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
a4∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
a4∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
a5∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
a5∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
a6∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, 
a6∈{0} ⟺ n_PSP 400 kV=0, 
a7∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, 
a7∈{0} ⟺ n_GSP 400 kV=0, 
j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_DVP 400 KV, n_KBP 400 KV, n_TRPVN TR 400/220 kV/kV, n_TRPVN TR 400/110 kV/kV, n_TRPVN TR 400/x kV/kV, n_PSP 400 kV, n_GSP 400 kV, n_GSS 400 kV∈N0;
NMT GSS 400 kV j:
UEEO <-> NMT GSS 400 kV j,
NMT GSS 400 kV j <-> GSS 400 kV j,
NMT GSS 400 kV j <-> SR DVP 220 kV a1 GSS j,
NMT GSS 400 kV j <-> SR KBP 220 kV a2 GSS j,
NMT GSS 400 kV j <-> SR TRPVN TR 220/110 kV/kV a3 GSS j,
NMT GSS 400 kV j <-> SR TRPVN TR 220/x kV/kV a4 GSS j,
NMT GSS 400 kV j <-> SR TRPNN TR 400/220 kV/kV a5 GSS j,
NMT GSS 400 kV j <-> SR PSP 220 kV a6 GSS j,
gde j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
j∈{0} ⟺ n_GSS 400 kV=0, 
n_GSS 400 kV∈N0;
GSS 220 kV j:
NMT GSS 220 kV j <-> GSS 220 kV j,
GSS 220 kV j <-> SR DVP 220 kV a1 GSS j,
GSS 220 kV j <-> SR KBP 220 kV a2 GSS j,
GSS 220 kV j <-> SR TRPVN TR 220/110 kV/kV a3 GSS j,
GSS 220 kV j <-> SR TRPVN TR 220/x kV/kV a4 GSS j,
GSS 220 kV j <-> SR TRPNN TR 400/220 kV/kV a5 GSS j,
GSS 220 kV j <-> SR PSP 220 kV a6 GSS j,
GSS 220 kV j <-> SR GSP 220 kV a7 GSS j,
gde a1∈{1, ..., n_DVP 220 KV} ⟺ n_DVP 220 KV>0, 
a1∈{0} ⟺ n_DVP 220 KV=0, 
a2∈{1, ..., n_KBP 220 KV} ⟺ n_KBP 220 KV>0, 
a2∈{0} ⟺ n_KBP 220 KV=0, 
a3∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
a3∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
a4∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
a4∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
a5∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
a5∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
a6∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, 
a6∈{0} ⟺ n_PSP 220 kV=0, 
a7∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, 
a7∈{0} ⟺ n_GSP 220 kV=0, 
j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_DVP 220 KV, n_KBP 220 KV, n_TRPVN TR 220/110 kV/kV, n_TRPVN TR 220/x kV/kV, n_TRPNN TR 400/220 kV/kV, n_PSP 220 kV, n_GSP 220 kV, n_GSS 220 kV∈N0;
NMT GSS 220 kV j:
UEEO <-> NMT GSS 220 kV j,
NMT GSS 220 kV j <-> GSS 220 kV j,
NMT GSS 220 kV j <-> SR DVP 110 kV a1 GSS j,
NMT GSS 220 kV j <-> SR KBP 110 kV a2 GSS j,
NMT GSS 220 kV j <-> SR TRPVN TR 110/x kV/kV a3 GSS j,
NMT GSS 220 kV j <-> SR TRPNN TR 400/110 kV/kV a4 GSS j,
NMT GSS 220 kV j <-> SR TRPNN TR 220/110 kV/kV a5 GSS j,
NMT GSS 220 kV j <-> SR PSP 110 kV a6 GSS j,
gde j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
j∈{0} ⟺ n_GSS 220 kV=0, 
n_GSS 220 kV∈N0;
GSS 110 kV j:
NMT GSS 110 kV j <-> GSS 110 kV j,
GSS 110 kV j <-> SR DVP 110 kV a1 GSS j,
GSS 110 kV j <-> SR KBP 110 kV a2 GSS j,
GSS 110 kV j <-> SR TRPVN TR 110/x kV/kV a3 GSS j,
GSS 110 kV j <-> SR TRPNN TR 400/110 kV/kV a4 GSS j,
GSS 110 kV j <-> SR TRPNN TR 220/110 kV/kV a5 GSS j,
GSS 110 kV j <-> SR PSP 110 kV a6 GSS j,
GSS 110 kV j <-> SR GSP 110 kV a7 GSS j,
gde a1∈{1, ..., n_DVP 110 KV} ⟺ n_DVP 110 KV>0, 
a1∈{0} ⟺ n_DVP 110 KV=0, 
a2∈{1, ..., n_KBP 110 KV} ⟺ n_KBP 110 KV>0, 
a2∈{0} ⟺ n_KBP 110 KV=0, 
a3∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
a3∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
a4∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
a4∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
a5∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
a5∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
a6∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, 
a6∈{0} ⟺ n_PSP 110 kV=0, 
a7∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, 
a7∈{0} ⟺ n_GSP 110 kV=0, 
j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_DVP 110 KV, n_KBP 110 KV, n_TRPVN TR 110/x kV/kV, n_TRPNN TR 400/110 kV/kV, n_TRPNN TR 220/110 kV/kV, n_PSP 110 kV, n_GSP 110 kV, n_GSS 110 kV∈N0;
NMT GSS 110 kV j:
UEEO <-> NMT GSS 110 kV j,
NMT GSS 110 kV j <-> GSS 110 kV j,
NMT GSS 110 kV j <-> SR DVP x kV a1 GSS j,
NMT GSS 110 kV j <-> SR KBP x kV a2 GSS j,
NMT GSS 110 kV j <-> SR TRPNN TR 400/x kV/kV a3 GSS j,
NMT GSS 110 kV j <-> SR TRPNN TR 220/x kV/kV a4 GSS j,
NMT GSS 110 kV j <-> SR TRPNN TR 110/x kV/kV a5 GSS j,
NMT GSS 110 kV j <-> SR PSP x kV a6 GSS j,
gde j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
j∈{0} ⟺ n_GSS 110 kV=0, 
n_GSS 110 kV∈N0;
GSS x kV j:
NMT GSS x kV j <-> GSS x kV j,
GSS x kV j <-> SR DVP x kV a1 GSS j,
GSS x kV j <-> SR KBP x kV a2 GSS j,
GSS x kV j <-> SR TRPNN TR 400/x kV/kV a3 GSS j,
GSS x kV j <-> SR TRPNN TR 220/x kV/kV a4 GSS j,
GSS x kV j <-> SR TRPNN TR 110/x kV/kV a5 GSS j,
GSS x kV j <-> SR PSP x kV a6 GSS j,
GSS x kV j <-> SR GSP x kV a7 GSS j,
gde a1∈{1, ..., n_DVP x KV} ⟺ n_DVP x KV>0, 
a1∈{0} ⟺ n_DVP x KV=0, 
a2∈{1, ..., n_KBP x KV} ⟺ n_KBP x KV>0, 
a2∈{0} ⟺ n_KBP x KV=0, 
a3∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
a3∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
a4∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
a4∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
a5∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
a5∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
a6∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, 
a6∈{0} ⟺ n_PSP x kV=0, 
a7∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, 
a7∈{0} ⟺ n_GSP x kV=0, 
j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_DVP x KV, n_KBP x KV, n_TRPNN TR 400/x kV/kV, n_TRPNN TR 220/x kV/kV, n_TRPNN TR 110/x kV/kV, n_PSP x kV, n_GSP x kV, n_GSS x kV∈N0;
NMT GSS x kV j:
UEEO <-> NMT GSS x kV j,
NMT GSS x kV j <-> GSS x kV j,
NMT GSS x kV j <-> SR DVP 400 kV a1 PSS k,
NMT GSS x kV j <-> SR KBP 400 kV a2 PSS k,
NMT GSS x kV j <-> SR TRPVN TR 400/220 kV/kV a3 PSS k,
NMT GSS x kV j <-> SR TRPVN TR 400/110 kV/kV a4 PSS k,
NMT GSS x kV j <-> SR TRPVN TR 400/x kV/kV a5 PSS k,
NMT GSS x kV j <-> SR PSP 400 kV a6 PSS k,
gde j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
j∈{0} ⟺ n_GSS x kV=0, 
n_GSS x kV∈N0;
PSS 400 kV k:
SR PSP 400 kV a6 PSS k <-> PSS 400 kV k,
PSS 400 kV k <-> SR DVP 400 kV a1 PSS k,
PSS 400 kV k <-> SR KBP 400 kV a2 PSS k,
PSS 400 kV k <-> SR TRPVN TR 400/220 kV/kV a3 PSS k,
PSS 400 kV k <-> SR TRPVN TR 400/110 kV/kV a4 PSS k,
PSS 400 kV k <-> SR TRPVN TR 400/x kV/kV a5 PSS k,
gde a1∈{1, ..., n_DVP 400 KV} ⟺ n_DVP 400 KV>0, 
a1∈{0} ⟺ n_DVP 400 KV=0, 
a2∈{1, ..., n_KBP 400 KV} ⟺ n_KBP 400 KV>0, 
a2∈{0} ⟺ n_KBP 400 KV=0, 
a3∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
a3∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
a4∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
a4∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
a5∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
a5∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
a6∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, 
a6∈{0} ⟺ n_PSP 400 kV=0, 
k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, 
k∈{0} ⟺ n_PSS 400 kV=0, 
n_DVP 400 KV, n_KBP 400 KV, n_TRPVN TR 400/220 kV/kV, n_TRPVN TR 400/110 kV/kV, n_TRPVN TR 400/x kV/kV, n_PSP 400 kV, n_PSS 400 kV∈N0;
PSS 220 kV k:
SR PSP 220 kV a6 PSS k <-> PSS 220 kV k,
PSS 220 kV k <-> SR DVP 220 kV a1 PSS k,
PSS 220 kV k <-> SR KBP 220 kV a2 PSS k,
PSS 220 kV k <-> SR TRPVN TR 220/110 kV/kV a3 PSS k,
PSS 220 kV k <-> SR TRPVN TR 220/x kV/kV a4 PSS k,
PSS 220 kV k <-> SR TRPNN TR 400/220 kV/kV a5 PSS k,
gde a1∈{1, ..., n_DVP 220 KV} ⟺ n_DVP 220 KV>0, 
a1∈{0} ⟺ n_DVP 220 KV=0, 
a2∈{1, ..., n_KBP 220 KV} ⟺ n_KBP 220 KV>0, 
a2∈{0} ⟺ n_KBP 220 KV=0, 
a3∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
a3∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
a4∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
a4∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
a5∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
a5∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
a6∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, 
a6∈{0} ⟺ n_PSP 220 kV=0, 
k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, 
k∈{0} ⟺ n_PSS 220 kV=0, 
n_DVP 220 KV, n_KBP 220 KV, n_TRPVN TR 220/110 kV/kV, n_TRPVN TR 220/x kV/kV, n_TRPNN TR 400/220 kV/kV, n_PSP 220 kV, n_PSS 220 kV∈N0;
PSS 110 kV k:
SR PSP 110 kV a6 PSS k <-> PSS 110 kV k,
PSS 110 kV k <-> SR DVP 110 kV a1 PSS k,
PSS 110 kV k <-> SR KBP 110 kV a2 PSS k,
PSS 110 kV k <-> SR TRPVN TR 110/x kV/kV a3 PSS k,
PSS 110 kV k <-> SR TRPNN TR 400/110 kV/kV a4 PSS k,
PSS 110 kV k <-> SR TRPNN TR 220/110 kV/kV a5 PSS k,
gde a1∈{1, ..., n_DVP 110 KV} ⟺ n_DVP 110 KV>0, 
a1∈{0} ⟺ n_DVP 110 KV=0, 
a2∈{1, ..., n_KBP 110 KV} ⟺ n_KBP 110 KV>0, 
a2∈{0} ⟺ n_KBP 110 KV=0, 
a3∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
a3∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
a4∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
a4∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
a5∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
a5∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
a6∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, 
a6∈{0} ⟺ n_PSP 110 kV=0, 
k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, 
k∈{0} ⟺ n_PSS 110 kV=0, 
n_DVP 110 KV, n_KBP 110 KV, n_TRPVN TR 110/x kV/kV, n_TRPNN TR 400/110 kV/kV, n_TRPNN TR 220/110 kV/kV, n_PSP 110 kV, n_PSS 110 kV∈N0;
PSS x kV k:
SR PSP x kV a6 PSS k <-> PSS x kV k,
PSS x kV k <-> SR DVP x kV a1 PSS k,
PSS x kV k <-> SR KBP x kV a2 PSS k,
PSS x kV k <-> SR TRPNN TR 400/x kV/kV a3 PSS k,
PSS x kV k <-> SR TRPNN TR 220/x kV/kV a4 PSS k,
PSS x kV k <-> SR TRPNN TR 110/x kV/kV a5 PSS k,
gde a1∈{1, ..., n_DVP x KV} ⟺ n_DVP x KV>0, 
a1∈{0} ⟺ n_DVP x KV=0, 
a2∈{1, ..., n_KBP x KV} ⟺ n_KBP x KV>0, 
a2∈{0} ⟺ n_KBP x KV=0, 
a3∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
a3∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
a4∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
a4∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
a5∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
a5∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
a6∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, 
a6∈{0} ⟺ n_PSP x kV=0, 
k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, 
k∈{0} ⟺ n_PSS x kV=0, 
n_DVP x KV, n_KBP x KV, n_TRPNN TR 400/x kV/kV, n_TRPNN TR 220/x kV/kV, n_TRPNN TR 110/x kV/kV, n_PSP x kV, n_PSS x kV∈N0;
UEEO:
Ne postoji <-> UEEO,
UEEO <-> NMT DVP 400 kV a1,
UEEO <-> NMT DVP 220 kV a2,
UEEO <-> NMT DVP 110 kV a3,
UEEO <-> NMT DVP x kV a4,
UEEO <-> NMT KBP 400 kV a5,
UEEO <-> NMT KBP 220 kV a6,
UEEO <-> NMT KBP 110 kV a7,
UEEO <-> NMT KBP x kV a8,
UEEO <-> NMT TRPNN TR 400/220 kV/kV a9,
UEEO <-> NMT TRPNN TR 400/110 kV/kV a10,
UEEO <-> NMT TRPNN TR 220/110 kV/kV a11,
UEEO <-> NMT TRPNN TR 400/x kV/kV a12,
UEEO <-> NMT TRPNN TR 220/x kV/kV a13,
UEEO <-> NMT TRPNN TR 110/x kV/kV a14,
UEEO <-> NMT GSS 400 kV a15,
UEEO <-> NMT GSS 220 kV a16,
UEEO <-> NMT GSS 110 kV a17,
UEEO <-> NMT GSS x kV a18,
UEEO <-> OP TRPVN TR 400/220 kV/kV a19,
UEEO <-> OP TRPVN TR 400/110 kV/kV a20,
UEEO <-> OP TRPVN TR 220/110 kV/kV a21,
UEEO <-> OP TRPVN TR 400/x kV/kV a22,
UEEO <-> OP TRPVN TR 220/x kV/kV a23,
UEEO <-> OP TRPVN TR 110/x kV/kV a24,
UEEO <-> OP TRPNN TR 400/220 kV/kV a9,
UEEO <-> OP TRPNN TR 400/110 kV/kV a10,
UEEO <-> OP TRPNN TR 220/110 kV/kV a11,
UEEO <-> OP TRPNN TR 400/x kV/kV a12,
UEEO <-> OP TRPNN TR 220/x kV/kV a13,
UEEO <-> OP TRPNN TR 110/x kV/kV a14,
gde:
a1∈{1, ..., n_DVP 400 KV} ⟺ n_DVP 400 KV>0, 
a1∈{0} ⟺ n_DVP 400 KV=0,
a2∈{1, ..., n_DVP 220 KV} ⟺ n_DVP 220 KV>0, 
a2∈{0} ⟺ n_DVP 220 KV=0,
a3∈{1, ..., n_DVP 110 KV} ⟺ n_DVP 110 KV>0, 
a3∈{0} ⟺ n_DVP 110 KV=0,
a4∈{1, ..., n_DVP x KV} ⟺ n_DVP x KV>0, 
a4∈{0} ⟺ n_DVP x KV=0,
a5∈{1, ..., n_KBP 400 KV} ⟺ n_KBP 400 KV>0, 
a5∈{0} ⟺ n_KBP 400 KV=0,
a6∈{1, ..., n_KBP 220 KV} ⟺ n_KBP 220 KV>0, 
a6∈{0} ⟺ n_KBP 220 KV=0,
a7∈{1, ..., n_KBP 110 KV} ⟺ n_KBP 110 KV>0, 
a7∈{0} ⟺ n_KBP 110 KV=0,
a8∈{1, ..., n_KBP x KV} ⟺ n_KBP x KV>0, 
a8∈{0} ⟺ n_KBP x KV=0,
a9∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, 
a9∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0,
a10∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, 
a10∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0,
a11∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, 
a11∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0,
a12∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, 
a12∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0,
a13∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, 
a13∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0,
a14∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, 
a14∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0,
a15∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, 
a15∈{0} ⟺ n_GSS 400 kV=0,
a16∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, 
a16∈{0} ⟺ n_GSS 220 kV=0,
a17∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, 
a17∈{0} ⟺ n_GSS 110 kV=0,
a18∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, 
a18∈{0} ⟺ n_GSS x kV=0,
a19∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, 
a19∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0,
a20∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, 
a20∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0,
a21∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, 
a21∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0,
a22∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, 
a22∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0,
a23∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, 
a23∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0,
a24∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, 
a24∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0,
n_DVP 400 KV, n_DVP 220 KV, n_DVP 110 KV, n_DVP x KV, n_KBP 400 KV, n_KBP 220 KV, n_KBP 110 KV, n_KBP x KV, n_TRPNN TR 400/220 kV/kV, n_TRPNN TR 400/110 kV/kV, n_TRPNN TR 220/110 kV/kV, n_TRPNN TR 400/x kV/kV, n_TRPNN TR 220/x kV/kV, n_TRPNN TR 110/x kV/kV, n_GSS 400 kV, n_GSS 400 kV, n_GSS 220 kV, n_GSS 110 kV, n_GSS x kV, n_TRPVN TR 400/220 kV/kV, n_TRPVN TR 400/110 kV/kV, n_TRPVN TR 220/110 kV/kV, n_TRPVN TR 220/110 kV/kV, n_TRPVN TR 400/x kV/kV, n_TRPVN TR 220/x kV/kV, n_TRPVN TR 110/x kV/kV∈N0;
Prethodnici i sledbenici osnovnih elemenata koji pripadaju EEO x
Prethodnici i sledbenici osnovih elemenata EEO x, gde x∈{1, ..., n_EEO} za n_EEO>1, n_EEO∈N:
EEO x SR DVP 400 kV i GSS j:
EEO x GSS 400 kV j <-> EEO x SR DVP 400 kV i GSS j <-> EEO x P DVP 400 kV i,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x P DVP 400 kV i:
EEO x SR DVP 400 kV i GSS j <-> EEO x P DVP 400 kV i <-> EEO x SMT DVP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x IRSU DVP 400 kV i:
EEO x SMT DVP 400 kV i <-> EEO x IRSU DVP 400 kV i,
EEO x IRSU DVP 400 kV i <-> EEO x NMT DVP 400 kV i,
EEO x IRSU DVP 400 kV i <-> kraj,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x SMT DVP 400 kV i:
EEO x P DVP 400 kV i <-> EEO x SMT DVP 400 kV i <-> EEO x IRSU DVP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x NMT DVP 400 kV i:
EEO x UEEO <-> EEO x NMT DVP 400 kV i,
EEO x NMT DVP 400 kV i <-> EEO x IRSU DVP 400 kV i,
EEO x NMT DVP 400 kV i <-> kraj,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x SR DVP 400 kV i PSS k:
EEO x PSS 400 kV k <-> EEO x SR DVP 400 kV i PSS k,
EEO x SR DVP 400 kV i PSS k <-> EEO x IRSU DVP 400 kV i,
EEO x SR DVP 400 kV i PSS k <-> EEO x SMT DVP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, 
k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x P DVP 400 kV i:
EEO x SR DVP 400 kV i GSS j <-> EEO x P DVP 400 kV i <-> EEO x IRSU DVP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x IRSU DVP 400 kV i:
EEO x P DVP 400 kV i <-> EEO x IRSU DVP 400 kV i,
EEO x IRSU DVP 400 kV i <-> EEO x SR DVP 400 kV i PSS k,
EEO x IRSU DVP 400 kV i <-> EEO x SMT DVP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, 
k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x SMT DVP 400 kV i:
EEO x IRSU DVP 400 kV i <-> EEO x SMT DVP 400 kV i,
EEO x SR DVP 400 kV i PSS k <-> EEO x SMT DVP 400 kV i,
EEO x SMT DVP 400 kV i <-> EEO x NMT DVP 400 kV i
EEO x SMT DVP 400 kV i <-> kraj,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x NMT DVP 400 kV i:
EEO x UEEO <-> EEO x NMT DVP 400 kV i,
EEO x NMT DVP 400 kV i <-> EEO x SMT DVP 400 kV i,
EEO x NMT DVP 400 kV i <-> kraj,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, 
i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x SR DVP 220 kV i GSS j:
EEO x GSS 220 kV j <-> EEO x SR DVP 220 kV i GSS j <-> EEO x P DVP 220 kV i,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x P DVP 220 kV i:
EEO x SR DVP 220 kV i GSS j <-> EEO x P DVP 220 kV i <-> EEO x SMT DVP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x IRSU DVP 220 kV i:
EEO x SMT DVP 220 kV i <-> EEO x IRSU DVP 220 kV i,
EEO x IRSU DVP 220 kV i <-> EEO x NMT DVP 220 kV i,
EEO x IRSU DVP 220 kV i <-> kraj,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x SMT DVP 220 kV i:
EEO x P DVP 220 kV i <-> EEO x SMT DVP 220 kV i <-> EEO x IRSU DVP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x NMT DVP 220 kV i:
EEO x UEEO <-> EEO x NMT DVP 220 kV i,
EEO x NMT DVP 220 kV i <-> EEO x IRSU DVP 220 kV i,
EEO x NMT DVP 220 kV i <-> kraj,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x SR DVP 220 kV i PSS k:
EEO x PSS 220 kV k <-> EEO x SR DVP 220 kV i PSS k,
EEO x SR DVP 220 kV i PSS k <-> EEO x IRSU DVP 220 kV i,
EEO x SR DVP 220 kV i PSS k <-> EEO x SMT DVP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x P DVP 220 kV i:
EEO x SR DVP 220 kV i GSS j <-> EEO x P DVP 220 kV i <-> EEO x IRSU DVP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x IRSU DVP 220 kV i:
EEO x P DVP 220 kV i <-> EEO x IRSU DVP 220 kV i,
EEO x IRSU DVP 220 kV i <-> EEO x SR DVP 220 kV i PSS k,
EEO x IRSU DVP 220 kV i <-> EEO x SMT DVP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x SMT DVP 220 kV i:
EEO x IRSU DVP 220 kV i <-> EEO x SMT DVP 220 kV i,
EEO x SR DVP 220 kV i PSS k <-> EEO x SMT DVP 220 kV i,
EEO x SMT DVP 220 kV i <-> EEO x NMT DVP 220 kV i
EEO x SMT DVP 220 kV i <-> kraj,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x NMT DVP 220 kV i:
EEO x UEEO <-> EEO x NMT DVP 220 kV i,
EEO x NMT DVP 220 kV i <-> EEO x SMT DVP 220 kV i,
EEO x NMT DVP 220 kV i <-> kraj,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, 
i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x SR DVP 110 kV i GSS j:
EEO x GSS 110 kV j <-> EEO x SR DVP 110 kV i GSS j <-> EEO x P DVP 110 kV i,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x P DVP 110 kV i:
EEO x SR DVP 110 kV i GSS j <-> EEO x P DVP 110 kV i <-> EEO x SMT DVP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x IRSU DVP 110 kV i:
EEO x SMT DVP 110 kV i <-> EEO x IRSU DVP 110 kV i,
EEO x IRSU DVP 110 kV i <-> EEO x NMT DVP 110 kV i,
EEO x IRSU DVP 110 kV i <-> kraj,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x SMT DVP 110 kV i:
EEO x P DVP 110 kV i <-> EEO x SMT DVP 110 kV i <-> EEO x IRSU DVP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x NMT DVP 110 kV i:
EEO x UEEO <-> EEO x NMT DVP 110 kV i,
EEO x NMT DVP 110 kV i <-> EEO x IRSU DVP 110 kV i,
EEO x NMT DVP 110 kV i <-> kraj,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x SR DVP 110 kV i PSS k:
EEO x PSS 110 kV k <-> EEO x SR DVP 110 kV i PSS k,
EEO x SR DVP 110 kV i PSS k <-> EEO x IRSU DVP 110 kV i,
EEO x SR DVP 110 kV i PSS k <-> EEO x SMT DVP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x P DVP 110 kV i:
EEO x SR DVP 110 kV i GSS j <-> EEO x P DVP 110 kV i <-> EEO x IRSU DVP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x IRSU DVP 110 kV i:
EEO x P DVP 110 kV i <-> EEO x IRSU DVP 110 kV i,
EEO x IRSU DVP 110 kV i <-> EEO x SR DVP 110 kV i PSS k,
EEO x IRSU DVP 110 kV i <-> EEO x SMT DVP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x SMT DVP 110 kV i:
EEO x IRSU DVP 110 kV i <-> EEO x SMT DVP 110 kV i,
EEO x SR DVP 110 kV i PSS k <-> EEO x SMT DVP 110 kV i,
EEO x SMT DVP 110 kV i <-> EEO x NMT DVP 110 kV i
EEO x SMT DVP 110 kV i <-> kraj,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x NMT DVP 110 kV i:
EEO x UEEO <-> EEO x NMT DVP 110 kV i,
EEO x NMT DVP 110 kV i <-> EEO x SMT DVP 110 kV i,
EEO x NMT DVP 110 kV i <-> kraj,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, 
i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x SR DVP x kV i GSS j:
EEO x GSS x kV j <-> EEO x SR DVP x kV i GSS j <-> EEO x P DVP x kV i,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_DVP x kV, EEO x n_GSS x kV∈N0;
EEO x P DVP x kV i:
EEO x SR DVP x kV i GSS j <-> EEO x P DVP x kV i <-> EEO x SMT DVP x kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_DVP x kV, EEO x n_GSS x kV∈N0;
EEO x IRSU DVP x kV i:
EEO x SMT DVP x kV i <-> EEO x IRSU DVP x kV i,
EEO x IRSU DVP x kV i <-> EEO x NMT DVP x kV i,
EEO x IRSU DVP x kV i <-> kraj,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x SMT DVP x kV i:
EEO x P DVP x kV i <-> EEO x SMT DVP x kV i <-> EEO x IRSU DVP x kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x NMT DVP x kV i:
EEO x UEEO <-> EEO x NMT DVP x kV i,
EEO x NMT DVP x kV i <-> EEO x IRSU DVP x kV i,
EEO x NMT DVP x kV i <-> kraj,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x SR DVP x kV i PSS k:
EEO x PSS x kV k <-> EEO x SR DVP x kV i PSS k,
EEO x SR DVP x kV i PSS k <-> EEO x IRSU DVP x kV i,
EEO x SR DVP x kV i PSS k <-> EEO x SMT DVP x kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_DVP x kV, EEO x n_PSS x kV∈N0;
EEO x P DVP x kV i:
EEO x SR DVP x kV i GSS j <-> EEO x P DVP x kV i <-> EEO x IRSU DVP x kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_DVP x kV, EEO x n_GSS x kV∈N0;
EEO x IRSU DVP x kV i:
EEO x P DVP x kV i <-> EEO x IRSU DVP x kV i,
EEO x IRSU DVP x kV i <-> EEO x SR DVP x kV i PSS k,
EEO x IRSU DVP x kV i <-> EEO x SMT DVP x kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_DVP x kV, EEO x n_PSS x kV∈N0;
EEO x SMT DVP x kV i:
EEO x IRSU DVP x kV i <-> EEO x SMT DVP x kV i,
EEO x SR DVP x kV i PSS k <-> EEO x SMT DVP x kV i,
EEO x SMT DVP x kV i <-> EEO x NMT DVP x kV i
EEO x SMT DVP x kV i <-> kraj,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x NMT DVP x kV i:
EEO x UEEO <-> EEO x NMT DVP x kV i,
EEO x NMT DVP x kV i <-> EEO x SMT DVP x kV i,
EEO x NMT DVP x kV i <-> kraj,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, 
i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x SR KBP 400 kV i GSS j:
EEO x GSS 400 kV j <-> EEO x SR KBP 400 kV i GSS j <-> EEO x P KBP 400 kV i,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x P KBP 400 kV i:
EEO x SR KBP 400 kV i GSS j <-> EEO x P KBP 400 kV i <-> EEO x SMT KBP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x IRSU KBP 400 kV i:
EEO x SMT KBP 400 kV i <-> EEO x IRSU KBP 400 kV i,
EEO x IRSU KBP 400 kV i <-> EEO x NMT KBP 400 kV i,
EEO x IRSU KBP 400 kV i <-> kraj,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x SMT KBP 400 kV i:
EEO x P KBP 400 kV i <-> EEO x SMT KBP 400 kV i <-> EEO x IRSU KBP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x NMT KBP 400 kV i:
EEO x UEEO <-> EEO x NMT KBP 400 kV i,
EEO x NMT KBP 400 kV i <-> EEO x IRSU KBP 400 kV i,
EEO x NMT KBP 400 kV i <-> kraj,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x SR KBP 400 kV i PSS k:
EEO x PSS 400 kV k <-> EEO x SR KBP 400 kV i PSS k,
EEO x SR KBP 400 kV i PSS k <-> EEO x IRSU KBP 400 kV i,
EEO x SR KBP 400 kV i PSS k <-> EEO x SMT KBP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, 
k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x P KBP 400 kV i:
EEO x SR KBP 400 kV i GSS j <-> EEO x P KBP 400 kV i <-> EEO x IRSU KBP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x IRSU KBP 400 kV i:
EEO x P KBP 400 kV i <-> EEO x IRSU KBP 400 kV i,
EEO x IRSU KBP 400 kV i <-> EEO x SR KBP 400 kV i PSS k,
EEO x IRSU KBP 400 kV i <-> EEO x SMT KBP 400 kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, 
k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x SMT KBP 400 kV i:
EEO x IRSU KBP 400 kV i <-> EEO x SMT KBP 400 kV i,
EEO x SR KBP 400 kV i PSS k <-> EEO x SMT KBP 400 kV i,
EEO x SMT KBP 400 kV i <-> EEO x NMT KBP 400 kV i
EEO x SMT KBP 400 kV i <-> kraj,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x NMT KBP 400 kV i:
EEO x UEEO <-> EEO x NMT KBP 400 kV i,
EEO x NMT KBP 400 kV i <-> EEO x SMT KBP 400 kV i,
EEO x NMT KBP 400 kV i <-> kraj,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, 
i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x SR KBP 220 kV i GSS j:
EEO x GSS 220 kV j <-> EEO x SR KBP 220 kV i GSS j <-> EEO x P KBP 220 kV i,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x P KBP 220 kV i:
EEO x SR KBP 220 kV i GSS j <-> EEO x P KBP 220 kV i <-> EEO x SMT KBP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x IRSU KBP 220 kV i:
EEO x SMT KBP 220 kV i <-> EEO x IRSU KBP 220 kV i,
EEO x IRSU KBP 220 kV i <-> EEO x NMT KBP 220 kV i,
EEO x IRSU KBP 220 kV i <-> kraj,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x SMT KBP 220 kV i:
EEO x P KBP 220 kV i <-> EEO x SMT KBP 220 kV i <-> EEO x IRSU KBP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x NMT KBP 220 kV i:
EEO x UEEO <-> EEO x NMT KBP 220 kV i,
EEO x NMT KBP 220 kV i <-> EEO x IRSU KBP 220 kV i,
EEO x NMT KBP 220 kV i <-> kraj,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x SR KBP 220 kV i PSS k:
EEO x PSS 220 kV k <-> EEO x SR KBP 220 kV i PSS k,
EEO x SR KBP 220 kV i PSS k <-> EEO x IRSU KBP 220 kV i,
EEO x SR KBP 220 kV i PSS k <-> EEO x SMT KBP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x P KBP 220 kV i:
EEO x SR KBP 220 kV i GSS j <-> EEO x P KBP 220 kV i <-> EEO x IRSU KBP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x IRSU KBP 220 kV i:
EEO x P KBP 220 kV i <-> EEO x IRSU KBP 220 kV i,
EEO x IRSU KBP 220 kV i <-> EEO x SR KBP 220 kV i PSS k,
EEO x IRSU KBP 220 kV i <-> EEO x SMT KBP 220 kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x SMT KBP 220 kV i:
EEO x IRSU KBP 220 kV i <-> EEO x SMT KBP 220 kV i,
EEO x SR KBP 220 kV i PSS k <-> EEO x SMT KBP 220 kV i,
EEO x SMT KBP 220 kV i <-> EEO x NMT KBP 220 kV i
EEO x SMT KBP 220 kV i <-> kraj,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x NMT KBP 220 kV i:
EEO x UEEO <-> EEO x NMT KBP 220 kV i,
EEO x NMT KBP 220 kV i <-> EEO x SMT KBP 220 kV i,
EEO x NMT KBP 220 kV i <-> kraj,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, 
i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x SR KBP 110 kV i GSS j:
EEO x GSS 110 kV j <-> EEO x SR KBP 110 kV i GSS j <-> EEO x P KBP 110 kV i,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x P KBP 110 kV i:
EEO x SR KBP 110 kV i GSS j <-> EEO x P KBP 110 kV i <-> EEO x SMT KBP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x IRSU KBP 110 kV i:
EEO x SMT KBP 110 kV i <-> EEO x IRSU KBP 110 kV i,
EEO x IRSU KBP 110 kV i <-> EEO x NMT KBP 110 kV i,
EEO x IRSU KBP 110 kV i <-> kraj,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x SMT KBP 110 kV i:
EEO x P KBP 110 kV i <-> EEO x SMT KBP 110 kV i <-> EEO x IRSU KBP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x NMT KBP 110 kV i:
EEO x UEEO <-> EEO x NMT KBP 110 kV i,
EEO x NMT KBP 110 kV i <-> EEO x IRSU KBP 110 kV i,
EEO x NMT KBP 110 kV i <-> kraj,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x SR KBP 110 kV i PSS k:
EEO x PSS 110 kV k <-> EEO x SR KBP 110 kV i PSS k,
EEO x SR KBP 110 kV i PSS k <-> EEO x IRSU KBP 110 kV i,
EEO x SR KBP 110 kV i PSS k <-> EEO x SMT KBP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x P KBP 110 kV i:
EEO x SR KBP 110 kV i GSS j <-> EEO x P KBP 110 kV i <-> EEO x IRSU KBP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x IRSU KBP 110 kV i:
EEO x P KBP 110 kV i <-> EEO x IRSU KBP 110 kV i,
EEO x IRSU KBP 110 kV i <-> EEO x SR KBP 110 kV i PSS k,
EEO x IRSU KBP 110 kV i <-> EEO x SMT KBP 110 kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x SMT KBP 110 kV i:
EEO x IRSU KBP 110 kV i <-> EEO x SMT KBP 110 kV i,
EEO x SR KBP 110 kV i PSS k <-> EEO x SMT KBP 110 kV i,
EEO x SMT KBP 110 kV i <-> EEO x NMT KBP 110 kV i
EEO x SMT KBP 110 kV i <-> kraj,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x NMT KBP 110 kV i:
EEO x UEEO <-> EEO x NMT KBP 110 kV i,
EEO x NMT KBP 110 kV i <-> EEO x SMT KBP 110 kV i,
EEO x NMT KBP 110 kV i <-> kraj,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, 
i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x SR KBP x kV i GSS j:
EEO x GSS x kV j <-> EEO x SR KBP x kV i GSS j <-> EEO x P KBP x kV i,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_KBP x kV, EEO x n_GSS x kV∈N0;
EEO x P KBP x kV i:
EEO x SR KBP x kV i GSS j <-> EEO x P KBP x kV i <-> EEO x SMT KBP x kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_KBP x kV, EEO x n_GSS x kV∈N0;
EEO x IRSU KBP x kV i:
EEO x SMT KBP x kV i <-> EEO x IRSU KBP x kV i,
EEO x IRSU KBP x kV i <-> EEO x NMT KBP x kV i,
EEO x IRSU KBP x kV i <-> kraj,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x SMT KBP x kV i:
EEO x P KBP x kV i <-> EEO x SMT KBP x kV i <-> EEO x IRSU KBP x kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x NMT KBP x kV i:
EEO x UEEO <-> EEO x NMT KBP x kV i,
EEO x NMT KBP x kV i <-> EEO x IRSU KBP x kV i,
EEO x NMT KBP x kV i <-> kraj,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x SR KBP x kV i PSS k:
EEO x PSS x kV k <-> EEO x SR KBP x kV i PSS k,
EEO x SR KBP x kV i PSS k <-> EEO x IRSU KBP x kV i,
EEO x SR KBP x kV i PSS k <-> EEO x SMT KBP x kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_KBP x kV, EEO x n_PSS x kV∈N0;
EEO x P KBP x kV i:
EEO x SR KBP x kV i GSS j <-> EEO x P KBP x kV i <-> EEO x IRSU KBP x kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_KBP x kV, EEO x n_GSS x kV∈N0;
EEO x IRSU KBP x kV i:
EEO x P KBP x kV i <-> EEO x IRSU KBP x kV i,
EEO x IRSU KBP x kV i <-> EEO x SR KBP x kV i PSS k,
EEO x IRSU KBP x kV i <-> EEO x SMT KBP x kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_KBP x kV, EEO x n_PSS x kV∈N0;
EEO x SMT KBP x kV i:
EEO x IRSU KBP x kV i <-> EEO x SMT KBP x kV i,
EEO x SR KBP x kV i PSS k <-> EEO x SMT KBP x kV i,
EEO x SMT KBP x kV i <-> EEO x NMT KBP x kV i
EEO x SMT KBP x kV i <-> kraj,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x NMT KBP x kV i:
EEO x UEEO <-> EEO x NMT KBP x kV i,
EEO x NMT KBP x kV i <-> EEO x SMT KBP x kV i,
EEO x NMT KBP x kV i <-> kraj,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, 
i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x SR TRPVN TR 400/220 kV/kV i GSS j:
EEO x GSS 400 kV j <-> EEO x SR TRPVN TR 400/220 kV/kV i GSS j <-> EEO x P TRPVN TR 400/220 kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x P TRPVN TR 400/220 kV/kV i:
EEO x SR TRPVN TR 400/220 kV/kV i GSS j <-> EEO x P TRPVN TR 400/220 kV/kV i <-> EEO x SMT TRPVN TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SMT TRPVN TR 400/220 kV/kV i:
EEO x P TRPVN TR 400/220 kV/kV i <-> EEO x SMT TRPVN TR 400/220 kV/kV i,
EEO x SMT TRPVN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i,
EEO x SMT TRPVN TR 400/220 kV/kV i <-> EEO x OP TRPVN TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x OP TRPVN TR 400/220 kV/kV i:
EEO x UEEO <-> EEO x OP TRPVN TR 400/220 kV/kV i,
EEO x OP TRPVN TR 400/220 kV/kV i <-> EEO x SMT TRPVN TR 400/220 kV/kV i,
EEO x OP TRPVN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x IR TRPVN TR 400/220 kV/kV i:
EEO x P TRPVN TR 400/220 kV/kV i <-> EEO x IR TRPVN TR 400/220 kV/kV i,
EEO x IR TRPVN TR 400/220 kV/kV i <-> EEO x SMT TRPVN TR 400/220 kV/kV i,
EEO x IR TRPVN TR 400/220 kV/kV i <-> EEO x SR TRPVN TR 400/220 kV/kV i PSS k,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x SR TRPVN TR 400/220 kV/kV i PSS k:
EEO x PSS 400 kV k <-> EEO x SR TRPVN TR 400/220 kV/kV i PSS k,
EEO x SR TRPVN TR 400/220 kV/kV i PSS k <-> EEO x IR TRPVN TR 400/220 kV/kV i,
EEO x SR TRPVN TR 400/220 kV/kV i PSS k <-> EEO x SMT TRPVN TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, 
k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x P TRPVN TR 400/220 kV/kV i:
EEO x SR TRPVN TR 400/220 kV/kV i GSS j <-> EEO x P TRPVN TR 400/220 kV/kV i <-> EEO x IR TRPVN TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SMT TRPVN TR 400/220 kV/kV i:
EEO x IR TRPVN TR 400/220 kV/kV i <-> EEO x SMT TRPVN TR 400/220 kV/kV i,
EEO x SR TRPVN TR 400/220 kV/kV i PSS k <-> EEO x SMT TRPVN TR 400/220 kV/kV i,
EEO x SMT TRPVN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i
EEO x SMT TRPVN TR 400/220 kV/kV i <-> EEO x OP TRPVN TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x SR TRPVN TR 400/110 kV/kV i GSS j:
EEO x GSS 400 kV j <-> EEO x SR TRPVN TR 400/110 kV/kV i GSS j <-> EEO x P TRPVN TR 400/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x P TRPVN TR 400/110 kV/kV i:
EEO x SR TRPVN TR 400/110 kV/kV i GSS j <-> EEO x P TRPVN TR 400/110 kV/kV i <-> EEO x SMT TRPVN TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SMT TRPVN TR 400/110 kV/kV i:
EEO x P TRPVN TR 400/110 kV/kV i <-> EEO x SMT TRPVN TR 400/110 kV/kV i,
EEO x SMT TRPVN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i,
EEO x SMT TRPVN TR 400/110 kV/kV i <-> EEO x OP TRPVN TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x OP TRPVN TR 400/110 kV/kV i:
EEO x UEEO <-> EEO x OP TRPVN TR 400/110 kV/kV i,
EEO x OP TRPVN TR 400/110 kV/kV i <-> EEO x SMT TRPVN TR 400/110 kV/kV i,
EEO x OP TRPVN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x IR TRPVN TR 400/110 kV/kV i:
EEO x P TRPVN TR 400/110 kV/kV i <-> EEO x IR TRPVN TR 400/110 kV/kV i,
EEO x IR TRPVN TR 400/110 kV/kV i <-> EEO x SMT TRPVN TR 400/110 kV/kV i,
EEO x IR TRPVN TR 400/110 kV/kV i <-> EEO x SR TRPVN TR 400/110 kV/kV i PSS k,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x SR TRPVN TR 400/110 kV/kV i PSS k:
EEO x PSS 400 kV k <-> EEO x SR TRPVN TR 400/110 kV/kV i PSS k,
EEO x SR TRPVN TR 400/110 kV/kV i PSS k <-> EEO x IR TRPVN TR 400/110 kV/kV i,
EEO x SR TRPVN TR 400/110 kV/kV i PSS k <-> EEO x SMT TRPVN TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, 
k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x P TRPVN TR 400/110 kV/kV i:
EEO x SR TRPVN TR 400/110 kV/kV i GSS j <-> EEO x P TRPVN TR 400/110 kV/kV i <-> EEO x IR TRPVN TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SMT TRPVN TR 400/110 kV/kV i:
EEO x IR TRPVN TR 400/110 kV/kV i <-> EEO x SMT TRPVN TR 400/110 kV/kV i,
EEO x SR TRPVN TR 400/110 kV/kV i PSS k <-> EEO x SMT TRPVN TR 400/110 kV/kV i,
EEO x SMT TRPVN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i
EEO x SMT TRPVN TR 400/110 kV/kV i <-> EEO x OP TRPVN TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x SR TRPVN TR 220/110 kV/kV i GSS j:
EEO x GSS 220 kV j <-> EEO x SR TRPVN TR 220/110 kV/kV i GSS j <-> EEO x P TRPVN TR 220/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x P TRPVN TR 220/110 kV/kV i:
EEO x SR TRPVN TR 220/110 kV/kV i GSS j <-> EEO x P TRPVN TR 220/110 kV/kV i <-> EEO x SMT TRPVN TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SMT TRPVN TR 220/110 kV/kV i:
EEO x P TRPVN TR 220/110 kV/kV i <-> EEO x SMT TRPVN TR 220/110 kV/kV i,
EEO x SMT TRPVN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i,
EEO x SMT TRPVN TR 220/110 kV/kV i <-> EEO x OP TRPVN TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x OP TRPVN TR 220/110 kV/kV i:
EEO x UEEO <-> EEO x OP TRPVN TR 220/110 kV/kV i,
EEO x OP TRPVN TR 220/110 kV/kV i <-> EEO x SMT TRPVN TR 220/110 kV/kV i,
EEO x OP TRPVN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x IR TRPVN TR 220/110 kV/kV i:
EEO x P TRPVN TR 220/110 kV/kV i <-> EEO x IR TRPVN TR 220/110 kV/kV i,
EEO x IR TRPVN TR 220/110 kV/kV i <-> EEO x SMT TRPVN TR 220/110 kV/kV i,
EEO x IR TRPVN TR 220/110 kV/kV i <-> EEO x SR TRPVN TR 220/110 kV/kV i PSS k,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x SR TRPVN TR 220/110 kV/kV i PSS k:
EEO x PSS 220 kV k <-> EEO x SR TRPVN TR 220/110 kV/kV i PSS k,
EEO x SR TRPVN TR 220/110 kV/kV i PSS k <-> EEO x IR TRPVN TR 220/110 kV/kV i,
EEO x SR TRPVN TR 220/110 kV/kV i PSS k <-> EEO x SMT TRPVN TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x P TRPVN TR 220/110 kV/kV i:
EEO x SR TRPVN TR 220/110 kV/kV i GSS j <-> EEO x P TRPVN TR 220/110 kV/kV i <-> EEO x IR TRPVN TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SMT TRPVN TR 220/110 kV/kV i:
EEO x IR TRPVN TR 220/110 kV/kV i <-> EEO x SMT TRPVN TR 220/110 kV/kV i,
EEO x SR TRPVN TR 220/110 kV/kV i PSS k <-> EEO x SMT TRPVN TR 220/110 kV/kV i,
EEO x SMT TRPVN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i
EEO x SMT TRPVN TR 220/110 kV/kV i <-> EEO x OP TRPVN TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x SR TRPVN TR 400/x kV/kV i GSS j:
EEO x GSS 400 kV j <-> EEO x SR TRPVN TR 400/x kV/kV i GSS j <-> EEO x P TRPVN TR 400/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/x kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x P TRPVN TR 400/x kV/kV i:
EEO x SR TRPVN TR 400/x kV/kV i GSS j <-> EEO x P TRPVN TR 400/x kV/kV i <-> EEO x SMT TRPVN TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/x kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SMT TRPVN TR 400/x kV/kV i:
EEO x P TRPVN TR 400/x kV/kV i <-> EEO x SMT TRPVN TR 400/x kV/kV i,
EEO x SMT TRPVN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i,
EEO x SMT TRPVN TR 400/x kV/kV i <-> EEO x OP TRPVN TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS 400 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x OP TRPVN TR 400/x kV/kV i:
EEO x UEEO <-> EEO x OP TRPVN TR 400/x kV/kV i,
EEO x OP TRPVN TR 400/x kV/kV i <-> EEO x SMT TRPVN TR 400/x kV/kV i,
EEO x OP TRPVN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x IR TRPVN TR 400/x kV/kV i:
EEO x P TRPVN TR 400/x kV/kV i <-> EEO x IR TRPVN TR 400/x kV/kV i,
EEO x IR TRPVN TR 400/x kV/kV i <-> EEO x SMT TRPVN TR 400/x kV/kV i,
EEO x IR TRPVN TR 400/x kV/kV i <-> EEO x SR TRPVN TR 400/x kV/kV i PSS k,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x SR TRPVN TR 400/x kV/kV i PSS k:
EEO x PSS 400 kV k <-> EEO x SR TRPVN TR 400/x kV/kV i PSS k,
EEO x SR TRPVN TR 400/x kV/kV i PSS k <-> EEO x IR TRPVN TR 400/x kV/kV i,
EEO x SR TRPVN TR 400/x kV/kV i PSS k <-> EEO x SMT TRPVN TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, 
k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/x kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x P TRPVN TR 400/x kV/kV i:
EEO x SR TRPVN TR 400/x kV/kV i GSS j <-> EEO x P TRPVN TR 400/x kV/kV i <-> EEO x IR TRPVN TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/x kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SMT TRPVN TR 400/x kV/kV i:
EEO x IR TRPVN TR 400/x kV/kV i <-> EEO x SMT TRPVN TR 400/x kV/kV i,
EEO x SR TRPVN TR 400/x kV/kV i PSS k <-> EEO x SMT TRPVN TR 400/x kV/kV i,
EEO x SMT TRPVN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i
EEO x SMT TRPVN TR 400/x kV/kV i <-> EEO x OP TRPVN TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS 400 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x SR TRPVN TR 220/x kV/kV i GSS j:
EEO x GSS 220 kV j <-> EEO x SR TRPVN TR 220/x kV/kV i GSS j <-> EEO x P TRPVN TR 220/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/x kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x P TRPVN TR 220/x kV/kV i:
EEO x SR TRPVN TR 220/x kV/kV i GSS j <-> EEO x P TRPVN TR 220/x kV/kV i <-> EEO x SMT TRPVN TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/x kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SMT TRPVN TR 220/x kV/kV i:
EEO x P TRPVN TR 220/x kV/kV i <-> EEO x SMT TRPVN TR 220/x kV/kV i,
EEO x SMT TRPVN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i,
EEO x SMT TRPVN TR 220/x kV/kV i <-> EEO x OP TRPVN TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x OP TRPVN TR 220/x kV/kV i:
EEO x UEEO <-> EEO x OP TRPVN TR 220/x kV/kV i,
EEO x OP TRPVN TR 220/x kV/kV i <-> EEO x SMT TRPVN TR 220/x kV/kV i,
EEO x OP TRPVN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x IR TRPVN TR 220/x kV/kV i:
EEO x P TRPVN TR 220/x kV/kV i <-> EEO x IR TRPVN TR 220/x kV/kV i,
EEO x IR TRPVN TR 220/x kV/kV i <-> EEO x SMT TRPVN TR 220/x kV/kV i,
EEO x IR TRPVN TR 220/x kV/kV i <-> EEO x SR TRPVN TR 220/x kV/kV i PSS k,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x SR TRPVN TR 220/x kV/kV i PSS k:
EEO x PSS 220 kV k <-> EEO x SR TRPVN TR 220/x kV/kV i PSS k,
EEO x SR TRPVN TR 220/x kV/kV i PSS k <-> EEO x IR TRPVN TR 220/x kV/kV i,
EEO x SR TRPVN TR 220/x kV/kV i PSS k <-> EEO x SMT TRPVN TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPVN TR 220/x kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x P TRPVN TR 220/x kV/kV i:
EEO x SR TRPVN TR 220/x kV/kV i GSS j <-> EEO x P TRPVN TR 220/x kV/kV i <-> EEO x IR TRPVN TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/x kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SMT TRPVN TR 220/x kV/kV i:
EEO x IR TRPVN TR 220/x kV/kV i <-> EEO x SMT TRPVN TR 220/x kV/kV i,
EEO x SR TRPVN TR 220/x kV/kV i PSS k <-> EEO x SMT TRPVN TR 220/x kV/kV i,
EEO x SMT TRPVN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i
EEO x SMT TRPVN TR 220/x kV/kV i <-> EEO x OP TRPVN TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x SR TRPVN TR 110/x kV/kV i GSS j:
EEO x GSS 110 kV j <-> EEO x SR TRPVN TR 110/x kV/kV i GSS j <-> EEO x P TRPVN TR 110/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPVN TR 110/x kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x P TRPVN TR 110/x kV/kV i:
EEO x SR TRPVN TR 110/x kV/kV i GSS j <-> EEO x P TRPVN TR 110/x kV/kV i <-> EEO x SMT TRPVN TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPVN TR 110/x kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SMT TRPVN TR 110/x kV/kV i:
EEO x P TRPVN TR 110/x kV/kV i <-> EEO x SMT TRPVN TR 110/x kV/kV i,
EEO x SMT TRPVN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i,
EEO x SMT TRPVN TR 110/x kV/kV i <-> EEO x OP TRPVN TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x OP TRPVN TR 110/x kV/kV i:
EEO x UEEO <-> EEO x OP TRPVN TR 110/x kV/kV i,
EEO x OP TRPVN TR 110/x kV/kV i <-> EEO x SMT TRPVN TR 110/x kV/kV i,
EEO x OP TRPVN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x IR TRPVN TR 110/x kV/kV i:
EEO x P TRPVN TR 110/x kV/kV i <-> EEO x IR TRPVN TR 110/x kV/kV i,
EEO x IR TRPVN TR 110/x kV/kV i <-> EEO x SMT TRPVN TR 110/x kV/kV i,
EEO x IR TRPVN TR 110/x kV/kV i <-> EEO x SR TRPVN TR 110/x kV/kV i PSS k,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x SR TRPVN TR 110/x kV/kV i PSS k:
EEO x PSS 110 kV k <-> EEO x SR TRPVN TR 110/x kV/kV i PSS k,
EEO x SR TRPVN TR 110/x kV/kV i PSS k <-> EEO x IR TRPVN TR 110/x kV/kV i,
EEO x SR TRPVN TR 110/x kV/kV i PSS k <-> EEO x SMT TRPVN TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPVN TR 110/x kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x P TRPVN TR 110/x kV/kV i:
EEO x SR TRPVN TR 110/x kV/kV i GSS j <-> EEO x P TRPVN TR 110/x kV/kV i <-> EEO x IR TRPVN TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPVN TR 110/x kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SMT TRPVN TR 110/x kV/kV i:
EEO x IR TRPVN TR 110/x kV/kV i <-> EEO x SMT TRPVN TR 110/x kV/kV i,
EEO x SR TRPVN TR 110/x kV/kV i PSS k <-> EEO x SMT TRPVN TR 110/x kV/kV i,
EEO x SMT TRPVN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i
EEO x SMT TRPVN TR 110/x kV/kV i <-> EEO x OP TRPVN TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x SR TRPNN TR 400/220 kV/kV i GSS j:
EEO x GSS 220 kV j <-> EEO x SR TRPNN TR 400/220 kV/kV i GSS j <-> EEO x P TRPNN TR 400/220 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x P TRPNN TR 400/220 kV/kV i:
EEO x SR TRPNN TR 400/220 kV/kV i GSS j <-> EEO x P TRPNN TR 400/220 kV/kV i <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SMT TRPNN TR 400/220 kV/kV i:
EEO x P TRPNN TR 400/220 kV/kV i <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
EEO x SMT TRPNN TR 400/220 kV/kV i <-> EEO x NMT TRPNN TR 400/220 kV/kV i,
EEO x SMT TRPNN TR 400/220 kV/kV i <-> EEO x OP TRPNN TR 400/220 kV/kV i,
EEO x SMT TRPNN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x NMT TRPNN TR 400/220 kV/kV i:
EEO x UEEO <-> EEO x NMT TRPNN TR 400/220 kV/kV i,
EEO x NMT TRPNN TR 400/220 kV/kV i <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
EEO x NMT TRPNN TR 400/220 kV/kV i <-> EEO x OP TRPNN TR 400/220 kV/kV i,
EEO x NMT TRPNN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x OP TRPNN TR 400/220 kV/kV i:
EEO x UEEO <-> EEO x OP TRPNN TR 400/220 kV/kV i,
EEO x OP TRPNN TR 400/220 kV/kV i <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
EEO x OP TRPNN TR 400/220 kV/kV i <-> EEO x NMT TRPNN TR 400/220 kV/kV i,
EEO x OP TRPNN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x SR TRPNN TR 400/220 kV/kV i PSS k:
EEO x PSS 220 kV k <-> EEO x SR TRPNN TR 400/220 kV/kV i PSS k,
EEO x SR TRPNN TR 400/220 kV/kV i PSS k <-> EEO x IR TRPNN TR 400/220 kV/kV i,
EEO x SR TRPNN TR 400/220 kV/kV i PSS k <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x IR TRPNN TR 400/220 kV/kV i:
EEO x P TRPNN TR 400/220 kV/kV i <-> EEO x IR TRPNN TR 400/220 kV/kV i,
EEO x IR TRPNN TR 400/220 kV/kV i <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
EEO x IR TRPNN TR 400/220 kV/kV i <-> EEO x SR TRPNN TR 400/220 kV/kV i PSS k,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x P TRPNN TR 400/220 kV/kV i:
EEO x SR TRPNN TR 400/220 kV/kV i GSS j <-> EEO x P TRPNN TR 400/220 kV/kV i <-> EEO x IR TRPNN TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SMT TRPNN TR 400/220 kV/kV i:
EEO x IR TRPNN TR 400/220 kV/kV i <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
EEO x SR TRPNN TR 400/220 kV/kV i PSS k <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
EEO x SMT TRPNN TR 400/220 kV/kV i <-> EEO x NMT TRPNN TR 400/220 kV/kV i,
EEO x SMT TRPNN TR 400/220 kV/kV i <-> EEO x OP TRPNN TR 400/220 kV/kV i,
EEO x SMT TRPNN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i,
uz uslov da je EEO x n_PSS 220 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x SR TRPNN TR 400/110 kV/kV i GSS j:
EEO x GSS 110 kV j <-> EEO x SR TRPNN TR 400/110 kV/kV i GSS j <-> EEO x P TRPNN TR 400/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x P TRPNN TR 400/110 kV/kV i:
EEO x SR TRPNN TR 400/110 kV/kV i GSS j <-> EEO x P TRPNN TR 400/110 kV/kV i <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SMT TRPNN TR 400/110 kV/kV i:
EEO x P TRPNN TR 400/110 kV/kV i <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
EEO x SMT TRPNN TR 400/110 kV/kV i <-> EEO x NMT TRPNN TR 400/110 kV/kV i,
EEO x SMT TRPNN TR 400/110 kV/kV i <-> EEO x OP TRPNN TR 400/110 kV/kV i,
EEO x SMT TRPNN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x NMT TRPNN TR 400/110 kV/kV i:
EEO x UEEO <-> EEO x NMT TRPNN TR 400/110 kV/kV i,
EEO x NMT TRPNN TR 400/110 kV/kV i <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
EEO x NMT TRPNN TR 400/110 kV/kV i <-> EEO x OP TRPNN TR 400/110 kV/kV i,
EEO x NMT TRPNN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x OP TRPNN TR 400/110 kV/kV i:
EEO x UEEO <-> EEO x OP TRPNN TR 400/110 kV/kV i,
EEO x OP TRPNN TR 400/110 kV/kV i <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
EEO x OP TRPNN TR 400/110 kV/kV i <-> EEO x NMT TRPNN TR 400/110 kV/kV i,
EEO x OP TRPNN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x SR TRPNN TR 400/110 kV/kV i PSS k:
EEO x PSS 110 kV k <-> EEO x SR TRPNN TR 400/110 kV/kV i PSS k,
EEO x SR TRPNN TR 400/110 kV/kV i PSS k <-> EEO x IR TRPNN TR 400/110 kV/kV i,
EEO x SR TRPNN TR 400/110 kV/kV i PSS k <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x IR TRPNN TR 400/110 kV/kV i:
EEO x P TRPNN TR 400/110 kV/kV i <-> EEO x IR TRPNN TR 400/110 kV/kV i,
EEO x IR TRPNN TR 400/110 kV/kV i <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
EEO x IR TRPNN TR 400/110 kV/kV i <-> EEO x SR TRPNN TR 400/110 kV/kV i PSS k,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x P TRPNN TR 400/110 kV/kV i:
EEO x SR TRPNN TR 400/110 kV/kV i GSS j <-> EEO x P TRPNN TR 400/110 kV/kV i <-> EEO x IR TRPNN TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SMT TRPNN TR 400/110 kV/kV i:
EEO x IR TRPNN TR 400/110 kV/kV i <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
EEO x SR TRPNN TR 400/110 kV/kV i PSS k <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
EEO x SMT TRPNN TR 400/110 kV/kV i <-> EEO x NMT TRPNN TR 400/110 kV/kV i,
EEO x SMT TRPNN TR 400/110 kV/kV i <-> EEO x OP TRPNN TR 400/110 kV/kV i,
EEO x SMT TRPNN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x SR TRPNN TR 220/110 kV/kV i GSS j:
EEO x GSS 110 kV j <-> EEO x SR TRPNN TR 220/110 kV/kV i GSS j <-> EEO x P TRPNN TR 220/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x P TRPNN TR 220/110 kV/kV i:
EEO x SR TRPNN TR 220/110 kV/kV i GSS j <-> EEO x P TRPNN TR 220/110 kV/kV i <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SMT TRPNN TR 220/110 kV/kV i:
EEO x P TRPNN TR 220/110 kV/kV i <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
EEO x SMT TRPNN TR 220/110 kV/kV i <-> EEO x NMT TRPNN TR 220/110 kV/kV i,
EEO x SMT TRPNN TR 220/110 kV/kV i <-> EEO x OP TRPNN TR 220/110 kV/kV i,
EEO x SMT TRPNN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x NMT TRPNN TR 220/110 kV/kV i:
EEO x UEEO <-> EEO x NMT TRPNN TR 220/110 kV/kV i,
EEO x NMT TRPNN TR 220/110 kV/kV i <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
EEO x NMT TRPNN TR 220/110 kV/kV i <-> EEO x OP TRPNN TR 220/110 kV/kV i,
EEO x NMT TRPNN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x OP TRPNN TR 220/110 kV/kV i:
EEO x UEEO <-> EEO x OP TRPNN TR 220/110 kV/kV i,
EEO x OP TRPNN TR 220/110 kV/kV i <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
EEO x OP TRPNN TR 220/110 kV/kV i <-> EEO x NMT TRPNN TR 220/110 kV/kV i,
EEO x OP TRPNN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x SR TRPNN TR 220/110 kV/kV i PSS k:
EEO x PSS 110 kV k <-> EEO x SR TRPNN TR 220/110 kV/kV i PSS k,
EEO x SR TRPNN TR 220/110 kV/kV i PSS k <-> EEO x IR TRPNN TR 220/110 kV/kV i,
EEO x SR TRPNN TR 220/110 kV/kV i PSS k <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x IR TRPNN TR 220/110 kV/kV i:
EEO x P TRPNN TR 220/110 kV/kV i <-> EEO x IR TRPNN TR 220/110 kV/kV i,
EEO x IR TRPNN TR 220/110 kV/kV i <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
EEO x IR TRPNN TR 220/110 kV/kV i <-> EEO x SR TRPNN TR 220/110 kV/kV i PSS k,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x P TRPNN TR 220/110 kV/kV i:
EEO x SR TRPNN TR 220/110 kV/kV i GSS j <-> EEO x P TRPNN TR 220/110 kV/kV i <-> EEO x IR TRPNN TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SMT TRPNN TR 220/110 kV/kV i:
EEO x IR TRPNN TR 220/110 kV/kV i <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
EEO x SR TRPNN TR 220/110 kV/kV i PSS k <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
EEO x SMT TRPNN TR 220/110 kV/kV i <-> EEO x NMT TRPNN TR 220/110 kV/kV i,
EEO x SMT TRPNN TR 220/110 kV/kV i <-> EEO x OP TRPNN TR 220/110 kV/kV i,
EEO x SMT TRPNN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i,
uz uslov da je EEO x n_PSS 110 kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x SR TRPNN TR 400/x kV/kV i GSS j:
EEO x GSS x kV j <-> EEO x SR TRPNN TR 400/x kV/kV i GSS j <-> EEO x P TRPNN TR 400/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x P TRPNN TR 400/x kV/kV i:
EEO x SR TRPNN TR 400/x kV/kV i GSS j <-> EEO x P TRPNN TR 400/x kV/kV i <-> EEO x SMT TRPNN TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SMT TRPNN TR 400/x kV/kV i:
EEO x P TRPNN TR 400/x kV/kV i <-> EEO x SMT TRPNN TR 400/x kV/kV i,
EEO x SMT TRPNN TR 400/x kV/kV i <-> EEO x NMT TRPNN TR 400/x kV/kV i,
EEO x SMT TRPNN TR 400/x kV/kV i <-> EEO x OP TRPNN TR 400/x kV/kV i,
EEO x SMT TRPNN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x NMT TRPNN TR 400/x kV/kV i:
EEO x UEEO <-> EEO x NMT TRPNN TR 400/x kV/kV i,
EEO x NMT TRPNN TR 400/x kV/kV i <-> EEO x SMT TRPNN TR 400/x kV/kV i,
EEO x NMT TRPNN TR 400/x kV/kV i <-> EEO x OP TRPNN TR 400/x kV/kV i,
EEO x NMT TRPNN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x OP TRPNN TR 400/x kV/kV i:
EEO x UEEO <-> EEO x OP TRPNN TR 400/x kV/kV i,
EEO x OP TRPNN TR 400/x kV/kV i <-> EEO x SMT TRPNN TR 400/x kV/kV i,
EEO x OP TRPNN TR 400/x kV/kV i <-> EEO x NMT TRPNN TR 400/x kV/kV i,
EEO x OP TRPNN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x SR TRPNN TR 400/x kV/kV i PSS k:
EEO x PSS x kV k <-> EEO x SR TRPNN TR 400/x kV/kV i PSS k,
EEO x SR TRPNN TR 400/x kV/kV i PSS k <-> EEO x IR TRPNN TR 400/x kV/kV i,
EEO x SR TRPNN TR 400/x kV/kV i PSS k <-> EEO x SMT TRPNN TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 400/x kV/kV i:
EEO x P TRPNN TR 400/x kV/kV i <-> EEO x IR TRPNN TR 400/x kV/kV i,
EEO x IR TRPNN TR 400/x kV/kV i <-> EEO x SMT TRPNN TR 400/x kV/kV i,
EEO x IR TRPNN TR 400/x kV/kV i <-> EEO x SR TRPNN TR 400/x kV/kV i PSS k,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x P TRPNN TR 400/x kV/kV i:
EEO x SR TRPNN TR 400/x kV/kV i GSS j <-> EEO x P TRPNN TR 400/x kV/kV i <-> EEO x IR TRPNN TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SMT TRPNN TR 400/x kV/kV i:
EEO x IR TRPNN TR 400/x kV/kV i <-> EEO x SMT TRPNN TR 400/x kV/kV i,
EEO x SR TRPNN TR 400/x kV/kV i PSS k <-> EEO x SMT TRPNN TR 400/x kV/kV i,
EEO x SMT TRPNN TR 400/x kV/kV i <-> EEO x NMT TRPNN TR 400/x kV/kV i,
EEO x SMT TRPNN TR 400/x kV/kV i <-> EEO x OP TRPNN TR 400/x kV/kV i,
EEO x SMT TRPNN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x SR TRPNN TR 220/x kV/kV i GSS j:
EEO x GSS x kV j <-> EEO x SR TRPNN TR 220/x kV/kV i GSS j <-> EEO x P TRPNN TR 220/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x P TRPNN TR 220/x kV/kV i:
EEO x SR TRPNN TR 220/x kV/kV i GSS j <-> EEO x P TRPNN TR 220/x kV/kV i <-> EEO x SMT TRPNN TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SMT TRPNN TR 220/x kV/kV i:
EEO x P TRPNN TR 220/x kV/kV i <-> EEO x SMT TRPNN TR 220/x kV/kV i,
EEO x SMT TRPNN TR 220/x kV/kV i <-> EEO x NMT TRPNN TR 220/x kV/kV i,
EEO x SMT TRPNN TR 220/x kV/kV i <-> EEO x OP TRPNN TR 220/x kV/kV i,
EEO x SMT TRPNN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x NMT TRPNN TR 220/x kV/kV i:
EEO x UEEO <-> EEO x NMT TRPNN TR 220/x kV/kV i,
EEO x NMT TRPNN TR 220/x kV/kV i <-> EEO x SMT TRPNN TR 220/x kV/kV i,
EEO x NMT TRPNN TR 220/x kV/kV i <-> EEO x OP TRPNN TR 220/x kV/kV i,
EEO x NMT TRPNN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x OP TRPNN TR 220/x kV/kV i:
EEO x UEEO <-> EEO x OP TRPNN TR 220/x kV/kV i,
EEO x OP TRPNN TR 220/x kV/kV i <-> EEO x SMT TRPNN TR 220/x kV/kV i,
EEO x OP TRPNN TR 220/x kV/kV i <-> EEO x NMT TRPNN TR 220/x kV/kV i,
EEO x OP TRPNN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x SR TRPNN TR 220/x kV/kV i PSS k:
EEO x PSS x kV k <-> EEO x SR TRPNN TR 220/x kV/kV i PSS k,
EEO x SR TRPNN TR 220/x kV/kV i PSS k <-> EEO x IR TRPNN TR 220/x kV/kV i,
EEO x SR TRPNN TR 220/x kV/kV i PSS k <-> EEO x SMT TRPNN TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 220/x kV/kV i:
EEO x P TRPNN TR 220/x kV/kV i <-> EEO x IR TRPNN TR 220/x kV/kV i,
EEO x IR TRPNN TR 220/x kV/kV i <-> EEO x SMT TRPNN TR 220/x kV/kV i,
EEO x IR TRPNN TR 220/x kV/kV i <-> EEO x SR TRPNN TR 220/x kV/kV i PSS k,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x P TRPNN TR 220/x kV/kV i:
EEO x SR TRPNN TR 220/x kV/kV i GSS j <-> EEO x P TRPNN TR 220/x kV/kV i <-> EEO x IR TRPNN TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SMT TRPNN TR 220/x kV/kV i:
EEO x IR TRPNN TR 220/x kV/kV i <-> EEO x SMT TRPNN TR 220/x kV/kV i,
EEO x SR TRPNN TR 220/x kV/kV i PSS k <-> EEO x SMT TRPNN TR 220/x kV/kV i,
EEO x SMT TRPNN TR 220/x kV/kV i <-> EEO x NMT TRPNN TR 220/x kV/kV i,
EEO x SMT TRPNN TR 220/x kV/kV i <-> EEO x OP TRPNN TR 220/x kV/kV i,
EEO x SMT TRPNN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x SR TRPNN TR 110/x kV/kV i GSS j:
EEO x GSS x kV j <-> EEO x SR TRPNN TR 110/x kV/kV i GSS j <-> EEO x P TRPNN TR 110/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x P TRPNN TR 110/x kV/kV i:
EEO x SR TRPNN TR 110/x kV/kV i GSS j <-> EEO x P TRPNN TR 110/x kV/kV i <-> EEO x SMT TRPNN TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SMT TRPNN TR 110/x kV/kV i:
EEO x P TRPNN TR 110/x kV/kV i <-> EEO x SMT TRPNN TR 110/x kV/kV i,
EEO x SMT TRPNN TR 110/x kV/kV i <-> EEO x NMT TRPNN TR 110/x kV/kV i,
EEO x SMT TRPNN TR 110/x kV/kV i <-> EEO x OP TRPNN TR 110/x kV/kV i,
EEO x SMT TRPNN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS x kV = 0,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x NMT TRPNN TR 110/x kV/kV i:
EEO x UEEO <-> EEO x NMT TRPNN TR 110/x kV/kV i,
EEO x NMT TRPNN TR 110/x kV/kV i <-> EEO x SMT TRPNN TR 110/x kV/kV i,
EEO x NMT TRPNN TR 110/x kV/kV i <-> EEO x OP TRPNN TR 110/x kV/kV i,
EEO x NMT TRPNN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x OP TRPNN TR 110/x kV/kV i:
EEO x UEEO <-> EEO x OP TRPNN TR 110/x kV/kV i,
EEO x OP TRPNN TR 110/x kV/kV i <-> EEO x SMT TRPNN TR 110/x kV/kV i,
EEO x OP TRPNN TR 110/x kV/kV i <-> EEO x NMT TRPNN TR 110/x kV/kV i,
EEO x OP TRPNN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x SR TRPNN TR 110/x kV/kV i PSS k:
EEO x PSS x kV k <-> EEO x SR TRPNN TR 110/x kV/kV i PSS k,
EEO x SR TRPNN TR 110/x kV/kV i PSS k <-> EEO x IR TRPNN TR 110/x kV/kV i,
EEO x SR TRPNN TR 110/x kV/kV i PSS k <-> EEO x SMT TRPNN TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 110/x kV/kV i:
EEO x P TRPNN TR 110/x kV/kV i <-> EEO x IR TRPNN TR 110/x kV/kV i,
EEO x IR TRPNN TR 110/x kV/kV i <-> EEO x SMT TRPNN TR 110/x kV/kV i,
EEO x IR TRPNN TR 110/x kV/kV i <-> EEO x SR TRPNN TR 110/x kV/kV i PSS k,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x P TRPNN TR 110/x kV/kV i:
EEO x SR TRPNN TR 110/x kV/kV i GSS j <-> EEO x P TRPNN TR 110/x kV/kV i <-> EEO x IR TRPNN TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SMT TRPNN TR 110/x kV/kV i:
EEO x IR TRPNN TR 110/x kV/kV i <-> EEO x SMT TRPNN TR 110/x kV/kV i,
EEO x SR TRPNN TR 110/x kV/kV i PSS k <-> EEO x SMT TRPNN TR 110/x kV/kV i,
EEO x SMT TRPNN TR 110/x kV/kV i <-> EEO x NMT TRPNN TR 110/x kV/kV i,
EEO x SMT TRPNN TR 110/x kV/kV i <-> EEO x OP TRPNN TR 110/x kV/kV i,
EEO x SMT TRPNN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i,
uz uslov da je EEO x n_PSS x kV > 0,
gde i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x SR GSP 400 kV i GSS i:
EEO x GSS 400 kV i <-> EEO x SR GSP 400 kV i GSS i <-> EEO x P GSP 400 kV i,
gde i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, 
i∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x P GSP 400 kV i:
EEO x SR GSP 400 kV i GSS i <-> EEO x P GSP 400 kV i <-> EEO x SMT GSP 400 kV i,
gde i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, 
i∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x SMT GSP 400 kV i:
EEO x P GSP 400 kV i <-> EEO x SMT GSP 400 kV i <-> EEO x SR GSP 400 kV i GSS i+1,
gde i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, 
i∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x SR GSP 400 kV i GSS i+1:
EEO x SMT GSP 400 kV i <-> EEO x SR GSP 400 kV i GSS i+1 <-> EEO x GSS 400 kV i+1,
gde i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, 
i∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x SR GSP 220 kV i GSS i:
EEO x GSS 220 kV i <-> EEO x SR GSP 220 kV i GSS i <-> EEO x P GSP 220 kV i,
gde i∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, 
i∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x P GSP 220 kV i:
EEO x SR GSP 220 kV i GSS i <-> EEO x P GSP 220 kV i <-> EEO x SMT GSP 220 kV i,
gde i∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, 
i∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x SMT GSP 220 kV i:
EEO x P GSP 220 kV i <-> EEO x SMT GSP 220 kV i <-> EEO x GSS 220 kV i+1,
gde i∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, 
i∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x SR GSP 220 kV i GSS i+1:
EEO x SMT GSP 220 kV i <-> EEO x SR GSP 220 kV i GSS i+1 <-> EEO x GSS 220 kV i+1,
gde ∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, 
∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x SR GSP 110 kV i GSS i:
EEO x GSS 110 kV i <-> EEO x SR GSP 110 kV i GSS i <-> EEO x P GSP 110 kV i,
gde i∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, 
i∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x P GSP 110 kV i:
EEO x SR GSP 110 kV i GSS i <-> EEO x P GSP 110 kV i <-> EEO x SMT GSP 110 kV i,
gde i∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, 
i∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x SMT GSP 110 kV i:
EEO x P GSP 110 kV i <-> EEO x SMT GSP 110 kV i <-> EEO x GSS 110 kV i+1,
gde i∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, 
i∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x SR GSP 110 kV i GSS i+1:
EEO x SMT GSP 110 kV i <-> EEO x SR GSP 110 kV i GSS i+1 <-> EEO x GSS 110 kV i+1,
gde ∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, 
∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x SR GSP x kV i GSS i:
EEO x GSS x kV i <-> EEO x SR GSP x kV i GSS i <-> EEO x P GSP x kV i,
gde i∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, 
i∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x P GSP x kV i:
EEO x SR GSP x kV i GSS i <-> EEO x P GSP x kV i <-> EEO x SMT GSP x kV i,
gde i∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, 
i∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x SMT GSP x kV i:
EEO x P GSP x kV i <-> EEO x SMT GSP x kV i <-> EEO x GSS x kV i+1,
gde i∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, 
i∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x SR GSP x kV i GSS i+1:
EEO x SMT GSP x kV i <-> EEO x SR GSP x kV i GSS i+1 <-> EEO x GSS x kV i+1,
gde ∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, 
∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x SR PSP 400 kV i GSS j:
EEO x GSS 400 kV j <-> EEO x SR PSP 400 kV i GSS j <-> EEO x P PSP 400 kV i,
gde i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, 
i∈{0} ⟺ EEO x n_PSP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_PSP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x P PSP 400 kV i:
EEO x SR PSP 400 kV i GSS j <-> EEO x P PSP 400 kV i <-> EEO x SR PSP 400 kV i PSS i,
gde i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, 
i∈{0} ⟺ EEO x n_PSP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_PSP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x SR PSP 400 kV i PSS i:
EEO x P PSP 400 kV i <-> EEO x SR PSP 400 kV i PSS i <-> EEO x PSS 400 kV i,
gde i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, 
i∈{0} ⟺ EEO x n_PSP 400 kV=0, 
EEO x n_PSP 400 kV∈N0;
EEO x SR PSP 220 kV i GSS j:
EEO x GSS 220 kV j <-> EEO x SR PSP 220 kV i GSS j <-> EEO x P PSP 220 kV i,
gde i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, 
i∈{0} ⟺ EEO x n_PSP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_PSP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x P PSP 220 kV i:
EEO x SR PSP 220 kV i GSS j <-> EEO x P PSP 220 kV i <-> EEO x SR PSP 220 kV i PSS i,
gde i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, 
i∈{0} ⟺ EEO x n_PSP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_PSP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x SR PSP 220 kV i PSS i:
EEO x P PSP 220 kV i <-> EEO x SR PSP 220 kV i PSS i <-> EEO x PSS 220 kV i,
gde i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, 
i∈{0} ⟺ EEO x n_PSP 220 kV=0, 
EEO x n_PSP 220 kV∈N0;
EEO x SR PSP 110 kV i GSS j:
EEO x GSS 110 kV j <-> EEO x SR PSP 110 kV i GSS j <-> EEO x P PSP 110 kV i,
gde i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, 
i∈{0} ⟺ EEO x n_PSP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_PSP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x P PSP 110 kV i:
EEO x SR PSP 110 kV i GSS j <-> EEO x P PSP 110 kV i <-> EEO x SR PSP 110 kV i PSS i,
gde i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, 
i∈{0} ⟺ EEO x n_PSP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_PSP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x SR PSP 110 kV i PSS i:
EEO x P PSP 110 kV i <-> EEO x SR PSP 110 kV i PSS i <-> EEO x PSS 110 kV i,
gde i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, 
i∈{0} ⟺ EEO x n_PSP 110 kV=0, 
EEO x n_PSP 110 kV∈N0;
EEO x SR PSP x kV i GSS j:
EEO x GSS x kV j <-> EEO x SR PSP x kV i GSS j <-> EEO x P PSP x kV i,
gde i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, 
i∈{0} ⟺ EEO x n_PSP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_PSP x kV, EEO x n_GSS x kV∈N0;
EEO x P PSP x kV i:
EEO x SR PSP x kV i GSS j <-> EEO x P PSP x kV i <-> EEO x SR PSP x kV i PSS i,
gde i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, 
i∈{0} ⟺ EEO x n_PSP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_PSP x kV, EEO x n_GSS x kV∈N0;
EEO x SR PSP x kV i PSS i:
EEO x P PSP x kV i <-> EEO x SR PSP x kV i PSS i <-> EEO x PSS x kV i,
gde i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, 
i∈{0} ⟺ EEO x n_PSP x kV=0, 
EEO x n_PSP x kV∈N0;
EEO x TR 400/220 kV/kV i:
EEO x SMT TRPVN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i,
EEO x OP TRPVN TR 400/220 kV/kV i <-> EEO x TR 400/220 kV/kV i,
EEO x TR 400/220 kV/kV i <-> EEO x NMT TRPNN TR 400/220 kV/kV i,
EEO x TR 400/220 kV/kV i <-> EEO x SMT TRPNN TR 400/220 kV/kV i,
EEO x TR 400/220 kV/kV i <-> EEO x OP TRPNN TR 400/220 kV/kV i,
gde i∈{1, ..., EEO x n_TR 400/220 kV/kV} ⟺ EEO x n_TR 400/220 kV/kV>0, 
i∈{0} ⟺ EEO x n_TR 400/220 kV/kV=0, 
EEO x n_TR 400/220 kV/kV∈N0;
EEO x TR 400/110 kV/kV i:
EEO x SMT TRPVN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i,
EEO x OP TRPVN TR 400/110 kV/kV i <-> EEO x TR 400/110 kV/kV i,
EEO x TR 400/110 kV/kV i <-> EEO x SMT TRPNN TR 400/110 kV/kV i,
EEO x TR 400/110 kV/kV i <-> EEO x NMT TRPNN TR 400/110 kV/kV i,
EEO x TR 400/110 kV/kV i <-> EEO x OP TRPNN TR 400/110 kV/kV i,
gde i∈{1, ..., EEO x n_TR 400/110 kV/kV} ⟺ EEO x n_TR 400/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TR 400/110 kV/kV=0, 
EEO x n_TR 400/110 kV/kV∈N0;
EEO x TR 220/110 kV/kV i:
EEO x SMT TRPVN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i,
EEO x OP TRPVN TR 220/110 kV/kV i <-> EEO x TR 220/110 kV/kV i,
EEO x TR 220/110 kV/kV i <-> EEO x SMT TRPNN TR 220/110 kV/kV i,
EEO x TR 220/110 kV/kV i <-> EEO x NMT TRPNN TR 220/110 kV/kV i,
EEO x TR 220/110 kV/kV i <-> EEO x OP TRPNN TR 220/110 kV/kV i,
gde i∈{1, ..., EEO x n_TR 220/110 kV/kV} ⟺ EEO x n_TR 220/110 kV/kV>0, 
i∈{0} ⟺ EEO x n_TR 220/110 kV/kV=0, 
EEO x n_TR 220/110 kV/kV∈N0;
EEO x TR 400/x kV/kV i:
EEO x SMT TRPVN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i,
EEO x OP TRPVN TR 400/x kV/kV i <-> EEO x TR 400/x kV/kV i,
EEO x TR 400/x kV/kV i <-> EEO x NMT TRPNN TR 400/x kV/kV i,
EEO x TR 400/x kV/kV i <-> EEO x SMT TRPNN TR 400/x kV/kV i,
EEO x TR 400/x kV/kV i <-> EEO x OP TRPNN TR 400/x kV/kV i,
gde i∈{1, ..., EEO x n_TR 400/x kV/kV} ⟺ EEO x n_TR 400/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TR 400/x kV/kV=0, 
EEO x n_TR 400/x kV/kV∈N0;
EEO x TR 220/x kV/kV i:
EEO x SMT TRPVN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i,
EEO x OP TRPVN TR 220/x kV/kV i <-> EEO x TR 220/x kV/kV i,
EEO x TR 220/x kV/kV i <-> EEO x NMT TRPNN TR 220/x kV/kV i,
EEO x TR 220/x kV/kV i <-> EEO x SMT TRPNN TR 220/x kV/kV i,
EEO x TR 220/x kV/kV i <-> EEO x OP TRPNN TR 220/x kV/kV i,
gde i∈{1, ..., EEO x n_TR 220/x kV/kV} ⟺ EEO x n_TR 220/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TR 220/x kV/kV=0, 
EEO x n_TR 220/x kV/kV∈N0;
EEO x TR 110/x kV/kV i:
EEO x SMT TRPVN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i,
EEO x OP TRPVN TR 110/x kV/kV i <-> EEO x TR 110/x kV/kV i,
EEO x TR 110/x kV/kV i <-> EEO x NMT TRPNN TR 110/x kV/kV i,
EEO x TR 110/x kV/kV i <-> EEO x SMT TRPNN TR 110/x kV/kV i,
EEO x TR 110/x kV/kV i <-> EEO x OP TRPNN TR 110/x kV/kV i,
gde i∈{1, ..., EEO x n_TR 110/x kV/kV} ⟺ EEO x n_TR 110/x kV/kV>0, 
i∈{0} ⟺ EEO x n_TR 110/x kV/kV=0, 
EEO x n_TR 110/x kV/kV∈N0;
EEO x GSS 400 kV j:
EEO x NMT GSS 400 kV j <-> EEO x GSS 400 kV j,
EEO x GSS 400 kV j <-> EEO x SR DVP 400 kV a1 GSS j,
EEO x GSS 400 kV j <-> EEO x SR KBP 400 kV a2 GSS j,
EEO x GSS 400 kV j <-> EEO x SR TRPVN TR 400/220 kV/kV a3 GSS j,
EEO x GSS 400 kV j <-> EEO x SR TRPVN TR 400/110 kV/kV a4 GSS j,
EEO x GSS 400 kV j <-> EEO x SR TRPVN TR 400/x kV/kV a5 GSS j,
EEO x GSS 400 kV j <-> EEO x SR GSP 400 kV a7 GSS j,
EEO x GSS 400 kV j <-> EEO x SR PSP 400 kV a6 GSS j,
gde a1∈{1, ..., EEO x n_DVP 400 KV} ⟺ EEO x n_DVP 400 KV>0, 
a1∈{0} ⟺ EEO x n_DVP 400 KV=0, 
a2∈{1, ..., EEO x n_KBP 400 KV} ⟺ EEO x n_KBP 400 KV>0, 
a2∈{0} ⟺ EEO x n_KBP 400 KV=0, 
a3∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
a3∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
a4∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
a4∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
a5∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
a5∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
a6∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, 
a6∈{0} ⟺ EEO x n_PSP 400 kV=0, 
a7∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, 
a7∈{0} ⟺ EEO x n_GSP 400 kV=0, 
j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_DVP 400 KV, EEO x n_KBP 400 KV, EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_TRPVN TR 400/x kV/kV, EEO x n_PSP 400 kV, EEO x n_GSP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x NMT GSS 400 kV j:
EEO x UEEO <-> EEO x NMT GSS 400 kV j,
EEO x NMT GSS 400 kV j <-> EEO x GSS 400 kV j,
EEO x NMT GSS 400 kV j <-> EEO x SR DVP 220 kV a1 GSS j,
EEO x NMT GSS 400 kV j <-> EEO x SR KBP 220 kV a2 GSS j,
EEO x NMT GSS 400 kV j <-> EEO x SR TRPVN TR 220/110 kV/kV a3 GSS j,
EEO x NMT GSS 400 kV j <-> EEO x SR TRPVN TR 220/x kV/kV a4 GSS j,
EEO x NMT GSS 400 kV j <-> EEO x SR TRPNN TR 400/220 kV/kV a5 GSS j,
EEO x NMT GSS 400 kV j <-> EEO x SR PSP 220 kV a6 GSS j,
gde j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_GSS 400 kV∈N0;
EEO x GSS 220 kV j:
EEO x NMT GSS 220 kV j <-> EEO x GSS 220 kV j,
EEO x GSS 220 kV j <-> EEO x SR DVP 220 kV a1 GSS j,
EEO x GSS 220 kV j <-> EEO x SR KBP 220 kV a2 GSS j,
EEO x GSS 220 kV j <-> EEO x SR TRPVN TR 220/110 kV/kV a3 GSS j,
EEO x GSS 220 kV j <-> EEO x SR TRPVN TR 220/x kV/kV a4 GSS j,
EEO x GSS 220 kV j <-> EEO x SR TRPNN TR 400/220 kV/kV a5 GSS j,
EEO x GSS 220 kV j <-> EEO x SR PSP 220 kV a6 GSS j,
EEO x GSS 220 kV j <-> EEO x SR GSP 220 kV a7 GSS j,
gde a1∈{1, ..., EEO x n_DVP 220 KV} ⟺ EEO x n_DVP 220 KV>0, 
a1∈{0} ⟺ EEO x n_DVP 220 KV=0, 
a2∈{1, ..., EEO x n_KBP 220 KV} ⟺ EEO x n_KBP 220 KV>0, 
a2∈{0} ⟺ EEO x n_KBP 220 KV=0, 
a3∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
a3∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
a4∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
a4∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
a5∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
a5∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
a6∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, 
a6∈{0} ⟺ EEO x n_PSP 220 kV=0, 
a7∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, 
a7∈{0} ⟺ EEO x n_GSP 220 kV=0, 
j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_DVP 220 KV, EEO x n_KBP 220 KV, EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_TRPVN TR 220/x kV/kV, EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_PSP 220 kV, EEO x n_GSP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x NMT GSS 220 kV j:
EEO x UEEO <-> EEO x NMT GSS 220 kV j,
EEO x NMT GSS 220 kV j <-> EEO x GSS 220 kV j,
EEO x NMT GSS 220 kV j <-> EEO x SR DVP 110 kV a1 GSS j,
EEO x NMT GSS 220 kV j <-> EEO x SR KBP 110 kV a2 GSS j,
EEO x NMT GSS 220 kV j <-> EEO x SR TRPVN TR 110/x kV/kV a3 GSS j,
EEO x NMT GSS 220 kV j <-> EEO x SR TRPNN TR 400/110 kV/kV a4 GSS j,
EEO x NMT GSS 220 kV j <-> EEO x SR TRPNN TR 220/110 kV/kV a5 GSS j,
EEO x NMT GSS 220 kV j <-> EEO x SR PSP 110 kV a6 GSS j,
gde j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_GSS 220 kV∈N0;
EEO x GSS 110 kV j:
EEO x NMT GSS 110 kV j <-> EEO x GSS 110 kV j,
EEO x GSS 110 kV j <-> EEO x SR DVP 110 kV a1 GSS j,
EEO x GSS 110 kV j <-> EEO x SR KBP 110 kV a2 GSS j,
EEO x GSS 110 kV j <-> EEO x SR TRPVN TR 110/x kV/kV a3 GSS j,
EEO x GSS 110 kV j <-> EEO x SR TRPNN TR 400/110 kV/kV a4 GSS j,
EEO x GSS 110 kV j <-> EEO x SR TRPNN TR 220/110 kV/kV a5 GSS j,
EEO x GSS 110 kV j <-> EEO x SR PSP 110 kV a6 GSS j,
EEO x GSS 110 kV j <-> EEO x SR GSP 110 kV a7 GSS j,
gde a1∈{1, ..., EEO x n_DVP 110 KV} ⟺ EEO x n_DVP 110 KV>0, 
a1∈{0} ⟺ EEO x n_DVP 110 KV=0, 
a2∈{1, ..., EEO x n_KBP 110 KV} ⟺ EEO x n_KBP 110 KV>0, 
a2∈{0} ⟺ EEO x n_KBP 110 KV=0, 
a3∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
a3∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
a4∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
a4∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
a5∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
a5∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
a6∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, 
a6∈{0} ⟺ EEO x n_PSP 110 kV=0, 
a7∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, 
a7∈{0} ⟺ EEO x n_GSP 110 kV=0, 
j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_DVP 110 KV, EEO x n_KBP 110 KV, EEO x n_TRPVN TR 110/x kV/kV, EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_PSP 110 kV, EEO x n_GSP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x NMT GSS 110 kV j:
EEO x UEEO <-> EEO x NMT GSS 110 kV j,
EEO x NMT GSS 110 kV j <-> EEO x GSS 110 kV j,
EEO x NMT GSS 110 kV j <-> EEO x SR DVP x kV a1 GSS j,
EEO x NMT GSS 110 kV j <-> EEO x SR KBP x kV a2 GSS j,
EEO x NMT GSS 110 kV j <-> EEO x SR TRPNN TR 400/x kV/kV a3 GSS j,
EEO x NMT GSS 110 kV j <-> EEO x SR TRPNN TR 220/x kV/kV a4 GSS j,
EEO x NMT GSS 110 kV j <-> EEO x SR TRPNN TR 110/x kV/kV a5 GSS j,
EEO x NMT GSS 110 kV j <-> EEO x SR PSP x kV a6 GSS j,
gde j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_GSS 110 kV∈N0;
EEO x GSS x kV j:
EEO x NMT GSS x kV j <-> EEO x GSS x kV j,
EEO x GSS x kV j <-> EEO x SR DVP x kV a1 GSS j,
EEO x GSS x kV j <-> EEO x SR KBP x kV a2 GSS j,
EEO x GSS x kV j <-> EEO x SR TRPNN TR 400/x kV/kV a3 GSS j,
EEO x GSS x kV j <-> EEO x SR TRPNN TR 220/x kV/kV a4 GSS j,
EEO x GSS x kV j <-> EEO x SR TRPNN TR 110/x kV/kV a5 GSS j,
EEO x GSS x kV j <-> EEO x SR PSP x kV a6 GSS j,
EEO x GSS x kV j <-> EEO x SR GSP x kV a7 GSS j,
gde a1∈{1, ..., EEO x n_DVP x KV} ⟺ EEO x n_DVP x KV>0, 
a1∈{0} ⟺ EEO x n_DVP x KV=0, 
a2∈{1, ..., EEO x n_KBP x KV} ⟺ EEO x n_KBP x KV>0, 
a2∈{0} ⟺ EEO x n_KBP x KV=0, 
a3∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
a3∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
a4∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
a4∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
a5∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
a5∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
a6∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, 
a6∈{0} ⟺ EEO x n_PSP x kV=0, 
a7∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, 
a7∈{0} ⟺ EEO x n_GSP x kV=0, 
j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_DVP x KV, EEO x n_KBP x KV, EEO x n_TRPNN TR 400/x kV/kV, EEO x n_TRPNN TR 220/x kV/kV, EEO x n_TRPNN TR 110/x kV/kV, EEO x n_PSP x kV, EEO x n_GSP x kV, EEO x n_GSS x kV∈N0;
EEO x NMT GSS x kV j:
EEO x UEEO <-> EEO x NMT GSS x kV j,
EEO x NMT GSS x kV j <-> EEO x GSS x kV j,
EEO x NMT GSS x kV j <-> EEO x SR DVP 400 kV a1 PSS k,
EEO x NMT GSS x kV j <-> EEO x SR KBP 400 kV a2 PSS k,
EEO x NMT GSS x kV j <-> EEO x SR TRPVN TR 400/220 kV/kV a3 PSS k,
EEO x NMT GSS x kV j <-> EEO x SR TRPVN TR 400/110 kV/kV a4 PSS k,
EEO x NMT GSS x kV j <-> EEO x SR TRPVN TR 400/x kV/kV a5 PSS k,
EEO x NMT GSS x kV j <-> EEO x SR PSP 400 kV a6 PSS k,
gde j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_GSS x kV∈N0;
EEO x PSS 400 kV k:
EEO x SR PSP 400 kV a6 PSS k <-> EEO x PSS 400 kV k,
EEO x PSS 400 kV k <-> EEO x SR DVP 400 kV a1 PSS k,
EEO x PSS 400 kV k <-> EEO x SR KBP 400 kV a2 PSS k,
EEO x PSS 400 kV k <-> EEO x SR TRPVN TR 400/220 kV/kV a3 PSS k,
EEO x PSS 400 kV k <-> EEO x SR TRPVN TR 400/110 kV/kV a4 PSS k,
EEO x PSS 400 kV k <-> EEO x SR TRPVN TR 400/x kV/kV a5 PSS k,
gde a1∈{1, ..., EEO x n_DVP 400 KV} ⟺ EEO x n_DVP 400 KV>0, 
a1∈{0} ⟺ EEO x n_DVP 400 KV=0, 
a2∈{1, ..., EEO x n_KBP 400 KV} ⟺ EEO x n_KBP 400 KV>0, 
a2∈{0} ⟺ EEO x n_KBP 400 KV=0, 
a3∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
a3∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
a4∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
a4∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
a5∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
a5∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
a6∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, 
a6∈{0} ⟺ EEO x n_PSP 400 kV=0, 
k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, 
k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_DVP 400 KV, EEO x n_KBP 400 KV, EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_TRPVN TR 400/x kV/kV, EEO x n_PSP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x PSS 220 kV k:
EEO x SR PSP 220 kV a6 PSS k <-> EEO x PSS 220 kV k,
EEO x PSS 220 kV k <-> EEO x SR DVP 220 kV a1 PSS k,
EEO x PSS 220 kV k <-> EEO x SR KBP 220 kV a2 PSS k,
EEO x PSS 220 kV k <-> EEO x SR TRPVN TR 220/110 kV/kV a3 PSS k,
EEO x PSS 220 kV k <-> EEO x SR TRPVN TR 220/x kV/kV a4 PSS k,
EEO x PSS 220 kV k <-> EEO x SR TRPNN TR 400/220 kV/kV a5 PSS k,
gde a1∈{1, ..., EEO x n_DVP 220 KV} ⟺ EEO x n_DVP 220 KV>0, 
a1∈{0} ⟺ EEO x n_DVP 220 KV=0, 
a2∈{1, ..., EEO x n_KBP 220 KV} ⟺ EEO x n_KBP 220 KV>0, 
a2∈{0} ⟺ EEO x n_KBP 220 KV=0, 
a3∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
a3∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
a4∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
a4∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
a5∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
a5∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
a6∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, 
a6∈{0} ⟺ EEO x n_PSP 220 kV=0, 
k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, 
k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_DVP 220 KV, EEO x n_KBP 220 KV, EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_TRPVN TR 220/x kV/kV, EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_PSP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x PSS 110 kV k:
EEO x SR PSP 110 kV a6 PSS k <-> EEO x PSS 110 kV k,
EEO x PSS 110 kV k <-> EEO x SR DVP 110 kV a1 PSS k,
EEO x PSS 110 kV k <-> EEO x SR KBP 110 kV a2 PSS k,
EEO x PSS 110 kV k <-> EEO x SR TRPVN TR 110/x kV/kV a3 PSS k,
EEO x PSS 110 kV k <-> EEO x SR TRPNN TR 400/110 kV/kV a4 PSS k,
EEO x PSS 110 kV k <-> EEO x SR TRPNN TR 220/110 kV/kV a5 PSS k,
gde a1∈{1, ..., EEO x n_DVP 110 KV} ⟺ EEO x n_DVP 110 KV>0, 
a1∈{0} ⟺ EEO x n_DVP 110 KV=0, 
a2∈{1, ..., EEO x n_KBP 110 KV} ⟺ EEO x n_KBP 110 KV>0, 
a2∈{0} ⟺ EEO x n_KBP 110 KV=0, 
a3∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
a3∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
a4∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
a4∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
a5∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
a5∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
a6∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, 
a6∈{0} ⟺ EEO x n_PSP 110 kV=0, 
k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, 
k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_DVP 110 KV, EEO x n_KBP 110 KV, EEO x n_TRPVN TR 110/x kV/kV, EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_PSP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x PSS x kV k:
EEO x SR PSP x kV a6 PSS k <-> EEO x PSS x kV k,
EEO x PSS x kV k <-> EEO x SR DVP x kV a1 PSS k,
EEO x PSS x kV k <-> EEO x SR KBP x kV a2 PSS k,
EEO x PSS x kV k <-> EEO x SR TRPNN TR 400/x kV/kV a3 PSS k,
EEO x PSS x kV k <-> EEO x SR TRPNN TR 220/x kV/kV a4 PSS k,
EEO x PSS x kV k <-> EEO x SR TRPNN TR 110/x kV/kV a5 PSS k,
gde a1∈{1, ..., EEO x n_DVP x KV} ⟺ EEO x n_DVP x KV>0, 
a1∈{0} ⟺ EEO x n_DVP x KV=0, 
a2∈{1, ..., EEO x n_KBP x KV} ⟺ EEO x n_KBP x KV>0, 
a2∈{0} ⟺ EEO x n_KBP x KV=0, 
a3∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
a3∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
a4∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
a4∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
a5∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
a5∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
a6∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, 
a6∈{0} ⟺ EEO x n_PSP x kV=0, 
k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, 
k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_DVP x KV, EEO x n_KBP x KV, EEO x n_TRPNN TR 400/x kV/kV, EEO x n_TRPNN TR 220/x kV/kV, EEO x n_TRPNN TR 110/x kV/kV, EEO x n_PSP x kV, EEO x n_PSS x kV∈N0;
EEO x UEEO:
Ne postoji <-> EEO x UEEO,
EEO x UEEO <-> EEO x NMT DVP 400 kV a1,
EEO x UEEO <-> EEO x NMT DVP 220 kV a2,
EEO x UEEO <-> EEO x NMT DVP 110 kV a3,
EEO x UEEO <-> EEO x NMT DVP x kV a4,
EEO x UEEO <-> EEO x NMT KBP 400 kV a5,
EEO x UEEO <-> EEO x NMT KBP 220 kV a6,
EEO x UEEO <-> EEO x NMT KBP 110 kV a7,
EEO x UEEO <-> EEO x NMT KBP x kV a8,
EEO x UEEO <-> EEO x NMT TRPNN TR 400/220 kV/kV a9,
EEO x UEEO <-> EEO x NMT TRPNN TR 400/110 kV/kV a10,
EEO x UEEO <-> EEO x NMT TRPNN TR 220/110 kV/kV a11,
EEO x UEEO <-> EEO x NMT TRPNN TR 400/x kV/kV a12,
EEO x UEEO <-> EEO x NMT TRPNN TR 220/x kV/kV a13,
EEO x UEEO <-> EEO x NMT TRPNN TR 110/x kV/kV a14,
EEO x UEEO <-> EEO x NMT GSS 400 kV a15,
EEO x UEEO <-> EEO x NMT GSS 220 kV a16,
EEO x UEEO <-> EEO x NMT GSS 110 kV a17,
EEO x UEEO <-> EEO x NMT GSS x kV a18,
EEO x UEEO <-> EEO x OP TRPVN TR 400/220 kV/kV a19,
EEO x UEEO <-> EEO x OP TRPVN TR 400/110 kV/kV a20,
EEO x UEEO <-> EEO x OP TRPVN TR 220/110 kV/kV a21,
EEO x UEEO <-> EEO x OP TRPVN TR 400/x kV/kV a22,
EEO x UEEO <-> EEO x OP TRPVN TR 220/x kV/kV a23,
EEO x UEEO <-> EEO x OP TRPVN TR 110/x kV/kV a24,
EEO x UEEO <-> EEO x OP TRPNN TR 400/220 kV/kV a9,
EEO x UEEO <-> EEO x OP TRPNN TR 400/110 kV/kV a10,
EEO x UEEO <-> EEO x OP TRPNN TR 220/110 kV/kV a11,
EEO x UEEO <-> EEO x OP TRPNN TR 400/x kV/kV a12,
EEO x UEEO <-> EEO x OP TRPNN TR 220/x kV/kV a13,
EEO x UEEO <-> EEO x OP TRPNN TR 110/x kV/kV a14,
gde:
a1∈{1, ..., EEO x n_DVP 400 KV} ⟺ EEO x n_DVP 400 KV>0, 
a1∈{0} ⟺ EEO x n_DVP 400 KV=0,
a2∈{1, ..., EEO x n_DVP 220 KV} ⟺ EEO x n_DVP 220 KV>0, 
a2∈{0} ⟺ EEO x n_DVP 220 KV=0,
a3∈{1, ..., EEO x n_DVP 110 KV} ⟺ EEO x n_DVP 110 KV>0, 
a3∈{0} ⟺ EEO x n_DVP 110 KV=0,
a4∈{1, ..., EEO x n_DVP x KV} ⟺ EEO x n_DVP x KV>0, 
a4∈{0} ⟺ EEO x n_DVP x KV=0,
a5∈{1, ..., EEO x n_KBP 400 KV} ⟺ EEO x n_KBP 400 KV>0, 
a5∈{0} ⟺ EEO x n_KBP 400 KV=0,
a6∈{1, ..., EEO x n_KBP 220 KV} ⟺ EEO x n_KBP 220 KV>0, 
a6∈{0} ⟺ EEO x n_KBP 220 KV=0,
a7∈{1, ..., EEO x n_KBP 110 KV} ⟺ EEO x n_KBP 110 KV>0, 
a7∈{0} ⟺ EEO x n_KBP 110 KV=0,
a8∈{1, ..., EEO x n_KBP x KV} ⟺ EEO x n_KBP x KV>0, 
a8∈{0} ⟺ EEO x n_KBP x KV=0,
a9∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, 
a9∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0,
a10∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, 
a10∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0,
a11∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, 
a11∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0,
a12∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, 
a12∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0,
a13∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, 
a13∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0,
a14∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, 
a14∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0,
a15∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, 
a15∈{0} ⟺ EEO x n_GSS 400 kV=0,
a16∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, 
a16∈{0} ⟺ EEO x n_GSS 220 kV=0,
a17∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, 
a17∈{0} ⟺ EEO x n_GSS 110 kV=0,
a18∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, 
a18∈{0} ⟺ EEO x n_GSS x kV=0,
a19∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, 
a19∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0,
a20∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, 
a20∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0,
a21∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, 
a21∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0,
a22∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, 
a22∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0,
a23∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, 
a23∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0,
a24∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, 
a24∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0,
EEO x n_DVP 400 KV, EEO x n_DVP 220 KV, EEO x n_DVP 110 KV, EEO x n_DVP x KV, EEO x n_KBP 400 KV, EEO x n_KBP 220 KV, EEO x n_KBP 110 KV, EEO x n_KBP x KV, EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_TRPNN TR 400/x kV/kV, EEO x n_TRPNN TR 220/x kV/kV, EEO x n_TRPNN TR 110/x kV/kV, EEO x n_GSS 400 kV, EEO x n_GSS 400 kV, EEO x n_GSS 220 kV, EEO x n_GSS 110 kV, EEO x n_GSS x kV, EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_TRPVN TR 400/x kV/kV, EEO x n_TRPVN TR 220/x kV/kV, EEO x n_TRPVN TR 110/x kV/kV∈N0;
### Prethodnici i sledbenici osnovnih elemenata koji ne pripadaju EEO
Prethodnici i sledbenici osnovih elemenata koji ne pripadaju EEO su:
DV 400 kV EEO x (m) EEO y (n):
kraj <-> DV 400 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO y n_DVP 400 kV} ⟺ EEO y n_DVP 400 kV>0, j∈{0} ⟺ EEO y n_DVP 400 kV=0, 
n_EEO∈N, EEO x n_DVP 400 kV, EEO y n_DVP 400 kV∈N0
DV 220 kV EEO x (m) EEO y (n):
kraj <-> DV 220 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO y n_DVP 220 kV} ⟺ EEO y n_DVP 220 kV>0, j∈{0} ⟺ EEO y n_DVP 220 kV=0, 
n_EEO∈N, EEO x n_DVP 220 kV, EEO y n_DVP 220 kV∈N0
DV 110 kV EEO x (m) EEO y (n):
kraj <-> DV 110 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO y n_DVP 110 kV} ⟺ EEO y n_DVP 110 kV>0, j∈{0} ⟺ EEO y n_DVP 110 kV=0, 
n_EEO∈N, EEO x n_DVP 110 kV, EEO y n_DVP 110 kV∈N0
DV x kV EEO x (m) EEO y (n):
kraj <-> DV x kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO y n_DVP x kV} ⟺ EEO y n_DVP x kV>0, j∈{0} ⟺ EEO y n_DVP x kV=0, 
n_EEO∈N, EEO x n_DVP x kV, EEO y n_DVP x kV∈N0
KB 400 kV EEO x (m) EEO y (n):
kraj <-> KB 400 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO y n_KBP 400 kV} ⟺ EEO y n_KBP 400 kV>0, j∈{0} ⟺ EEO y n_KBP 400 kV=0, 
n_EEO∈N, EEO x n_KBP 400 kV, EEO y n_KBP 400 kV∈N0
KB 220 kV EEO x (m) EEO y (n):
kraj <-> KB 220 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO y n_KBP 220 kV} ⟺ EEO y n_KBP 220 kV>0, j∈{0} ⟺ EEO y n_KBP 220 kV=0, 
n_EEO∈N, EEO x n_KBP 220 kV, EEO y n_KBP 220 kV∈N0
KB 110 kV EEO x (m) EEO y (n):
kraj <-> KB 110 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO y n_KBP 110 kV} ⟺ EEO y n_KBP 110 kV>0, j∈{0} ⟺ EEO y n_KBP 110 kV=0, 
n_EEO∈N, EEO x n_KBP 110 kV, EEO y n_KBP 110 kV∈N0
KB x kV EEO x (m) EEO y (n):
kraj <-> KB x kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO y n_KBP x kV} ⟺ EEO y n_KBP x kV>0, j∈{0} ⟺ EEO y n_KBP x kV=0, 
n_EEO∈N, EEO x n_KBP x kV, EEO y n_KBP x kV∈N0
MV (DV+KB) 400 kV EEO x (m) EEO y (n):
kraj <-> MV (DV+KB) 400 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO y n_KBP 400 kV} ⟺ EEO y n_KBP 400 kV>0, j∈{0} ⟺ EEO y n_KBP 400 kV=0, 
n_EEO∈N, EEO x n_DVP 400 kV, EEO y n_KBP 400 kV∈N0
MV (DV+KB) 220 kV EEO x (m) EEO y (n):
kraj <-> MV (DV+KB) 220 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO y n_KBP 220 kV} ⟺ EEO y n_KBP 220 kV>0, j∈{0} ⟺ EEO y n_KBP 220 kV=0, 
n_EEO∈N, EEO x n_DVP 220 kV, EEO y n_KBP 220 kV∈N0
MV (DV+KB) 110 kV EEO x (m) EEO y (n):
kraj <-> MV (DV+KB) 110 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO y n_KBP 110 kV} ⟺ EEO y n_KBP 110 kV>0, j∈{0} ⟺ EEO y n_KBP 110 kV=0, 
n_EEO∈N, EEO x n_DVP 110 kV, EEO y n_KBP 110 kV∈N0
MV (DV+KB) x kV EEO x (m) EEO y (n):
kraj <-> MV (DV+KB) x kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO y n_KBP x kV} ⟺ EEO y n_KBP x kV>0, j∈{0} ⟺ EEO y n_KBP x kV=0, 
n_EEO∈N, EEO x n_DVP x kV, EEO y n_KBP x kV∈N0
MV (KB+DV) 400 kV EEO x (m) EEO y (n):
kraj <-> MV (KB+DV) 400 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO y n_DVP 400 kV} ⟺ EEO y n_DVP 400 kV>0, j∈{0} ⟺ EEO y n_DVP 400 kV=0, 
n_EEO∈N, EEO x n_KBP 400 kV, EEO y n_DVP 400 kV∈N0
MV (KB+DV) 220 kV EEO x (m) EEO y (n):
kraj <-> MV (KB+DV) 220 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO y n_DVP 220 kV} ⟺ EEO y n_DVP 220 kV>0, j∈{0} ⟺ EEO y n_DVP 220 kV=0, 
n_EEO∈N, EEO x n_KBP 220 kV, EEO y n_DVP 220 kV∈N0
MV (KB+DV) 110 kV EEO x (m) EEO y (n):
kraj <-> MV (KB+DV) 110 kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO y n_DVP 110 kV} ⟺ EEO y n_DVP 110 kV>0, j∈{0} ⟺ EEO y n_DVP 110 kV=0, 
n_EEO∈N, EEO x n_KBP 110 kV, EEO y n_DVP 110 kV∈N0
MV (KB+DV) x kV EEO x (m) EEO y (n):
kraj <-> MV (KB+DV) x kV EEO x (m) EEO y (n) <-> kraj,
gde: x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO y n_DVP x kV} ⟺ EEO y n_DVP x kV>0, j∈{0} ⟺ EEO y n_DVP x kV=0, 
n_EEO∈N, EEO x n_KBP x kV, EEO y n_DVP x kV∈N0
### Granični elementi
Osnovni element kome je kao prethodnik, ili jedan od prethodnika, ili sledbenik, ili jedan od sledbenika definisan sa “kraj”, je granični element. Granični element je element preko koga se ostvaruje veza izmedju elekroenergetske opreme PS koja pripada EEO i elekroenergetske opreme PS koja ne pripada EEO.
Granični elementi elektroenergetske opreme koja pripada EEO
Granični elementi elektroenergetske opreme koja pripada EEO su:
IRSU DVP 400 kV i: 
∀i (i≠0) ⟹ ∃ (IRSU DVP 400 kV i) kao granični element ⟺ (n_DVP 400 kV>0 ∧ n_PSS 400 kV = 0), 
i=0 ⟹ ∄ (IRSU DVP 400 kV i) kao granicni element ⟺ (n_DVP 400 kV=0 V n_PSS 400 kV > 0),
i∈{1, ..., n_DVP 400 kV} ⟺ (n_DVP 400 kV>0 ∧ n_PSS 400 kV = 0),
i∈{0} ⟺ (n_DVP 400 kV=0 V n_PSS 400 kV > 0), 
n_DVP 400 kV, n_PSS 400 kV∈N0;
SMT DVP 400 kV i: 
∀i (i≠0) ⟹ ∃ (SMT DVP 400 kV i) kao granični element ⟺ (n_DVP 400 kV>0 ∧ n_PSS 400 kV > 0), 
i=0 ⟹ ∄ (SMT DVP 400 kV i) kao granicni element ⟺ (n_DVP 400 kV=0 V n_PSS 400 kV = 0),
i∈{1, ..., n_DVP 400 kV} ⟺ (n_DVP 400 kV>0 ∧ n_PSS 400 kV > 0),
i∈{0} ⟺ (n_DVP 400 kV=0 V n_PSS 400 kV = 0), 
n_DVP 400 kV, n_PSS 400 kV∈N0;
NMT DVP 400 kV i: 
∀i (i≠0) ⟹ ∃ (NMT DVP 400 kV i) kao granični element ⟺ (n_DVP 400 kV>0 ∧ ), 
i=0 ⟹ ∄ (NMT DVP 400 kV i) kao granicni element ⟺ (n_DVP 400 kV=0 V ),
i∈{1, ..., n_DVP 400 kV} ⟺ (n_DVP 400 kV>0 ∧ ),
i∈{0} ⟺ (n_DVP 400 kV=0 V ), 
n_DVP 400 kV, n_PSS 400 kV∈N0;
IRSU DVP 220 kV i: 
∀i (i≠0) ⟹ ∃ (IRSU DVP 220 kV i) kao granični element ⟺ (n_DVP 220 kV>0 ∧ n_PSS 220 kV = 0), 
i=0 ⟹ ∄ (IRSU DVP 220 kV i) kao granicni element ⟺ (n_DVP 220 kV=0 V n_PSS 400 kV > 0),
i∈{1, ..., n_DVP 220 kV} ⟺ (n_DVP 220 kV>0 ∧ n_PSS 220 kV = 0),
i∈{0} ⟺ (n_DVP 220 kV=0 V n_PSS 400 kV > 0), 
n_DVP 220 kV, n_PSS 400 kV∈N0;
SMT DVP 220 kV i: 
∀i (i≠0) ⟹ ∃ (SMT DVP 220 kV i) kao granični element ⟺ (n_DVP 220 kV>0 ∧ n_PSS 220 kV > 0), 
i=0 ⟹ ∄ (SMT DVP 220 kV i) kao granicni element ⟺ (n_DVP 220 kV=0 V n_PSS 400 kV = 0),
i∈{1, ..., n_DVP 220 kV} ⟺ (n_DVP 220 kV>0 ∧ n_PSS 220 kV > 0),
i∈{0} ⟺ (n_DVP 220 kV=0 V n_PSS 400 kV = 0), 
n_DVP 220 kV, n_PSS 400 kV∈N0;
NMT DVP 220 kV i: 
∀i (i≠0) ⟹ ∃ (NMT DVP 220 kV i) kao granični element ⟺ (n_DVP 220 kV>0 ∧ ), 
i=0 ⟹ ∄ (NMT DVP 220 kV i) kao granicni element ⟺ (n_DVP 220 kV=0 V ),
i∈{1, ..., n_DVP 220 kV} ⟺ (n_DVP 220 kV>0 ∧ ),
i∈{0} ⟺ (n_DVP 220 kV=0 V ), 
n_DVP 220 kV, n_PSS 400 kV∈N0;
IRSU DVP 110 kV i: 
∀i (i≠0) ⟹ ∃ (IRSU DVP 110 kV i) kao granični element ⟺ (n_DVP 110 kV>0 ∧ n_PSS 110 kV = 0), 
i=0 ⟹ ∄ (IRSU DVP 110 kV i) kao granicni element ⟺ (n_DVP 110 kV=0 V n_PSS 400 kV > 0),
i∈{1, ..., n_DVP 110 kV} ⟺ (n_DVP 110 kV>0 ∧ n_PSS 110 kV = 0),
i∈{0} ⟺ (n_DVP 110 kV=0 V n_PSS 400 kV > 0), 
n_DVP 110 kV, n_PSS 400 kV∈N0;
SMT DVP 110 kV i: 
∀i (i≠0) ⟹ ∃ (SMT DVP 110 kV i) kao granični element ⟺ (n_DVP 110 kV>0 ∧ n_PSS 110 kV > 0), 
i=0 ⟹ ∄ (SMT DVP 110 kV i) kao granicni element ⟺ (n_DVP 110 kV=0 V n_PSS 400 kV = 0),
i∈{1, ..., n_DVP 110 kV} ⟺ (n_DVP 110 kV>0 ∧ n_PSS 110 kV > 0),
i∈{0} ⟺ (n_DVP 110 kV=0 V n_PSS 400 kV = 0), 
n_DVP 110 kV, n_PSS 400 kV∈N0;
NMT DVP 110 kV i: 
∀i (i≠0) ⟹ ∃ (NMT DVP 110 kV i) kao granični element ⟺ (n_DVP 110 kV>0 ∧ ), 
i=0 ⟹ ∄ (NMT DVP 110 kV i) kao granicni element ⟺ (n_DVP 110 kV=0 V ),
i∈{1, ..., n_DVP 110 kV} ⟺ (n_DVP 110 kV>0 ∧ ),
i∈{0} ⟺ (n_DVP 110 kV=0 V ), 
n_DVP 110 kV, n_PSS 400 kV∈N0;
IRSU DVP x kV i: 
∀i (i≠0) ⟹ ∃ (IRSU DVP x kV i) kao granični element ⟺ (n_DVP x kV>0 ∧ n_PSS x kV = 0), 
i=0 ⟹ ∄ (IRSU DVP x kV i) kao granicni element ⟺ (n_DVP x kV=0 V n_PSS 400 kV > 0),
i∈{1, ..., n_DVP x kV} ⟺ (n_DVP x kV>0 ∧ n_PSS x kV = 0),
i∈{0} ⟺ (n_DVP x kV=0 V n_PSS 400 kV > 0), 
n_DVP x kV, n_PSS 400 kV∈N0;
SMT DVP x kV i: 
∀i (i≠0) ⟹ ∃ (SMT DVP x kV i) kao granični element ⟺ (n_DVP x kV>0 ∧ n_PSS x kV > 0), 
i=0 ⟹ ∄ (SMT DVP x kV i) kao granicni element ⟺ (n_DVP x kV=0 V n_PSS 400 kV = 0),
i∈{1, ..., n_DVP x kV} ⟺ (n_DVP x kV>0 ∧ n_PSS x kV > 0),
i∈{0} ⟺ (n_DVP x kV=0 V n_PSS 400 kV = 0), 
n_DVP x kV, n_PSS 400 kV∈N0;
NMT DVP x kV i: 
∀i (i≠0) ⟹ ∃ (NMT DVP x kV i) kao granični element ⟺ (n_DVP x kV>0 ∧ ), 
i=0 ⟹ ∄ (NMT DVP x kV i) kao granicni element ⟺ (n_DVP x kV=0 V ),
i∈{1, ..., n_DVP x kV} ⟺ (n_DVP x kV>0 ∧ ),
i∈{0} ⟺ (n_DVP x kV=0 V ), 
n_DVP x kV, n_PSS 400 kV∈N0;
IRSU KBP 400 kV i: 
∀i (i≠0) ⟹ ∃ (IRSU KBP 400 kV i) kao granični element ⟺ (n_KBP 400 kV>0 ∧ n_PSS 400 kV = 0), 
i=0 ⟹ ∄ (IRSU KBP 400 kV i) kao granicni element ⟺ (n_KBP 400 kV=0 V n_PSS 400 kV > 0),
i∈{1, ..., n_KBP 400 kV} ⟺ (n_KBP 400 kV>0 ∧ n_PSS 400 kV = 0),
i∈{0} ⟺ (n_KBP 400 kV=0 V n_PSS 400 kV > 0), 
n_KBP 400 kV, n_PSS 400 kV∈N0;
SMT KBP 400 kV i: 
∀i (i≠0) ⟹ ∃ (SMT KBP 400 kV i) kao granični element ⟺ (n_KBP 400 kV>0 ∧ n_PSS 400 kV > 0), 
i=0 ⟹ ∄ (SMT KBP 400 kV i) kao granicni element ⟺ (n_KBP 400 kV=0 V n_PSS 400 kV = 0),
i∈{1, ..., n_KBP 400 kV} ⟺ (n_KBP 400 kV>0 ∧ n_PSS 400 kV > 0),
i∈{0} ⟺ (n_KBP 400 kV=0 V n_PSS 400 kV = 0), 
n_KBP 400 kV, n_PSS 400 kV∈N0;
NMT KBP 400 kV i: 
∀i (i≠0) ⟹ ∃ (NMT KBP 400 kV i) kao granični element ⟺ (n_KBP 400 kV>0 ∧ ), 
i=0 ⟹ ∄ (NMT KBP 400 kV i) kao granicni element ⟺ (n_KBP 400 kV=0 V ),
i∈{1, ..., n_KBP 400 kV} ⟺ (n_KBP 400 kV>0 ∧ ),
i∈{0} ⟺ (n_KBP 400 kV=0 V ), 
n_KBP 400 kV, n_PSS 400 kV∈N0;
IRSU KBP 220 kV i: 
∀i (i≠0) ⟹ ∃ (IRSU KBP 220 kV i) kao granični element ⟺ (n_KBP 220 kV>0 ∧ n_PSS 220 kV = 0), 
i=0 ⟹ ∄ (IRSU KBP 220 kV i) kao granicni element ⟺ (n_KBP 220 kV=0 V n_PSS 400 kV > 0),
i∈{1, ..., n_KBP 220 kV} ⟺ (n_KBP 220 kV>0 ∧ n_PSS 220 kV = 0),
i∈{0} ⟺ (n_KBP 220 kV=0 V n_PSS 400 kV > 0), 
n_KBP 220 kV, n_PSS 400 kV∈N0;
SMT KBP 220 kV i: 
∀i (i≠0) ⟹ ∃ (SMT KBP 220 kV i) kao granični element ⟺ (n_KBP 220 kV>0 ∧ n_PSS 220 kV > 0), 
i=0 ⟹ ∄ (SMT KBP 220 kV i) kao granicni element ⟺ (n_KBP 220 kV=0 V n_PSS 400 kV = 0),
i∈{1, ..., n_KBP 220 kV} ⟺ (n_KBP 220 kV>0 ∧ n_PSS 220 kV > 0),
i∈{0} ⟺ (n_KBP 220 kV=0 V n_PSS 400 kV = 0), 
n_KBP 220 kV, n_PSS 400 kV∈N0;
NMT KBP 220 kV i: 
∀i (i≠0) ⟹ ∃ (NMT KBP 220 kV i) kao granični element ⟺ (n_KBP 220 kV>0 ∧ ), 
i=0 ⟹ ∄ (NMT KBP 220 kV i) kao granicni element ⟺ (n_KBP 220 kV=0 V ),
i∈{1, ..., n_KBP 220 kV} ⟺ (n_KBP 220 kV>0 ∧ ),
i∈{0} ⟺ (n_KBP 220 kV=0 V ), 
n_KBP 220 kV, n_PSS 400 kV∈N0;
IRSU KBP 110 kV i: 
∀i (i≠0) ⟹ ∃ (IRSU KBP 110 kV i) kao granični element ⟺ (n_KBP 110 kV>0 ∧ n_PSS 110 kV = 0), 
i=0 ⟹ ∄ (IRSU KBP 110 kV i) kao granicni element ⟺ (n_KBP 110 kV=0 V n_PSS 400 kV > 0),
i∈{1, ..., n_KBP 110 kV} ⟺ (n_KBP 110 kV>0 ∧ n_PSS 110 kV = 0),
i∈{0} ⟺ (n_KBP 110 kV=0 V n_PSS 400 kV > 0), 
n_KBP 110 kV, n_PSS 400 kV∈N0;
SMT KBP 110 kV i: 
∀i (i≠0) ⟹ ∃ (SMT KBP 110 kV i) kao granični element ⟺ (n_KBP 110 kV>0 ∧ n_PSS 110 kV > 0), 
i=0 ⟹ ∄ (SMT KBP 110 kV i) kao granicni element ⟺ (n_KBP 110 kV=0 V n_PSS 400 kV = 0),
i∈{1, ..., n_KBP 110 kV} ⟺ (n_KBP 110 kV>0 ∧ n_PSS 110 kV > 0),
i∈{0} ⟺ (n_KBP 110 kV=0 V n_PSS 400 kV = 0), 
n_KBP 110 kV, n_PSS 400 kV∈N0;
NMT KBP 110 kV i: 
∀i (i≠0) ⟹ ∃ (NMT KBP 110 kV i) kao granični element ⟺ (n_KBP 110 kV>0 ∧ ), 
i=0 ⟹ ∄ (NMT KBP 110 kV i) kao granicni element ⟺ (n_KBP 110 kV=0 V ),
i∈{1, ..., n_KBP 110 kV} ⟺ (n_KBP 110 kV>0 ∧ ),
i∈{0} ⟺ (n_KBP 110 kV=0 V ), 
n_KBP 110 kV, n_PSS 400 kV∈N0;
IRSU KBP x kV i: 
∀i (i≠0) ⟹ ∃ (IRSU KBP x kV i) kao granični element ⟺ (n_KBP x kV>0 ∧ n_PSS x kV = 0), 
i=0 ⟹ ∄ (IRSU KBP x kV i) kao granicni element ⟺ (n_KBP x kV=0 V n_PSS 400 kV > 0),
i∈{1, ..., n_KBP x kV} ⟺ (n_KBP x kV>0 ∧ n_PSS x kV = 0),
i∈{0} ⟺ (n_KBP x kV=0 V n_PSS 400 kV > 0), 
n_KBP x kV, n_PSS 400 kV∈N0;
SMT KBP x kV i: 
∀i (i≠0) ⟹ ∃ (SMT KBP x kV i) kao granični element ⟺ (n_KBP x kV>0 ∧ n_PSS x kV > 0), 
i=0 ⟹ ∄ (SMT KBP x kV i) kao granicni element ⟺ (n_KBP x kV=0 V n_PSS 400 kV = 0),
i∈{1, ..., n_KBP x kV} ⟺ (n_KBP x kV>0 ∧ n_PSS x kV > 0),
i∈{0} ⟺ (n_KBP x kV=0 V n_PSS 400 kV = 0), 
n_KBP x kV, n_PSS 400 kV∈N0;
NMT KBP x kV i: 
∀i (i≠0) ⟹ ∃ (NMT KBP x kV i) kao granični element ⟺ (n_KBP x kV>0 ∧ ), 
i=0 ⟹ ∄ (NMT KBP x kV i) kao granicni element ⟺ (n_KBP x kV=0 V ),
i∈{1, ..., n_KBP x kV} ⟺ (n_KBP x kV>0 ∧ ),
i∈{0} ⟺ (n_KBP x kV=0 V ), 
n_KBP x kV, n_PSS 400 kV∈N0;
Granični elementi elektroenergetske opreme koja pripada EEO x
Granični elementi elektroenergetske opreme koja pripada EEO x, gde x∈{1, ..., n_EEO} za n_EEO>1, n_EEO∈N su:
EEO x IRSU DVP 400 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x IRSU DVP 400 kV i) kao granični element ⟺ (EEO x n_DVP 400 kV>0 ∧ EEO x n_PSS 400 kV = 0), 
i=0 ⟹ ∄ (EEO x IRSU DVP 400 kV i) kao granicni element ⟺ (EEO x n_DVP 400 kV=0 V EEO x n_PSS 400 kV > 0),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ (EEO x n_DVP 400 kV>0 ∧ EEO x n_PSS 400 kV = 0),
i∈{0} ⟺ (EEO x n_DVP 400 kV=0 V EEO x n_PSS 400 kV > 0), 
EEO x n_DVP 400 kV, n_PSS 400 kV∈N0;
EEO x SMT DVP 400 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x SMT DVP 400 kV i) kao granični element ⟺ (EEO x n_DVP 400 kV>0 ∧ EEO x n_PSS 400 kV > 0), 
i=0 ⟹ ∄ (EEO x SMT DVP 400 kV i) kao granicni element ⟺ (EEO x n_DVP 400 kV=0 V EEO x n_PSS 400 kV = 0),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ (EEO x n_DVP 400 kV>0 ∧ EEO x n_PSS 400 kV > 0),
i∈{0} ⟺ (EEO x n_DVP 400 kV=0 V EEO x n_PSS 400 kV = 0), 
EEO x n_DVP 400 kV, n_PSS 400 kV∈N0;
EEO x NMT DVP 400 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x NMT DVP 400 kV i) kao granični element ⟺ (EEO x n_DVP 400 kV>0 ∧ ), 
i=0 ⟹ ∄ (EEO x NMT DVP 400 kV i) kao granicni element ⟺ (EEO x n_DVP 400 kV=0 V ),
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ (EEO x n_DVP 400 kV>0 ∧ ),
i∈{0} ⟺ (EEO x n_DVP 400 kV=0 V ), 
EEO x n_DVP 400 kV, n_PSS 400 kV∈N0;
EEO x IRSU DVP 220 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x IRSU DVP 220 kV i) kao granični element ⟺ (EEO x n_DVP 220 kV>0 ∧ EEO x n_PSS 220 kV = 0), 
i=0 ⟹ ∄ (EEO x IRSU DVP 220 kV i) kao granicni element ⟺ (EEO x n_DVP 220 kV=0 V EEO x n_PSS 400 kV > 0),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ (EEO x n_DVP 220 kV>0 ∧ EEO x n_PSS 220 kV = 0),
i∈{0} ⟺ (EEO x n_DVP 220 kV=0 V EEO x n_PSS 400 kV > 0), 
EEO x n_DVP 220 kV, n_PSS 400 kV∈N0;
EEO x SMT DVP 220 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x SMT DVP 220 kV i) kao granični element ⟺ (EEO x n_DVP 220 kV>0 ∧ EEO x n_PSS 220 kV > 0), 
i=0 ⟹ ∄ (EEO x SMT DVP 220 kV i) kao granicni element ⟺ (EEO x n_DVP 220 kV=0 V EEO x n_PSS 400 kV = 0),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ (EEO x n_DVP 220 kV>0 ∧ EEO x n_PSS 220 kV > 0),
i∈{0} ⟺ (EEO x n_DVP 220 kV=0 V EEO x n_PSS 400 kV = 0), 
EEO x n_DVP 220 kV, n_PSS 400 kV∈N0;
EEO x NMT DVP 220 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x NMT DVP 220 kV i) kao granični element ⟺ (EEO x n_DVP 220 kV>0 ∧ ), 
i=0 ⟹ ∄ (EEO x NMT DVP 220 kV i) kao granicni element ⟺ (EEO x n_DVP 220 kV=0 V ),
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ (EEO x n_DVP 220 kV>0 ∧ ),
i∈{0} ⟺ (EEO x n_DVP 220 kV=0 V ), 
EEO x n_DVP 220 kV, n_PSS 400 kV∈N0;
EEO x IRSU DVP 110 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x IRSU DVP 110 kV i) kao granični element ⟺ (EEO x n_DVP 110 kV>0 ∧ EEO x n_PSS 110 kV = 0), 
i=0 ⟹ ∄ (EEO x IRSU DVP 110 kV i) kao granicni element ⟺ (EEO x n_DVP 110 kV=0 V EEO x n_PSS 400 kV > 0),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ (EEO x n_DVP 110 kV>0 ∧ EEO x n_PSS 110 kV = 0),
i∈{0} ⟺ (EEO x n_DVP 110 kV=0 V EEO x n_PSS 400 kV > 0), 
EEO x n_DVP 110 kV, n_PSS 400 kV∈N0;
EEO x SMT DVP 110 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x SMT DVP 110 kV i) kao granični element ⟺ (EEO x n_DVP 110 kV>0 ∧ EEO x n_PSS 110 kV > 0), 
i=0 ⟹ ∄ (EEO x SMT DVP 110 kV i) kao granicni element ⟺ (EEO x n_DVP 110 kV=0 V EEO x n_PSS 400 kV = 0),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ (EEO x n_DVP 110 kV>0 ∧ EEO x n_PSS 110 kV > 0),
i∈{0} ⟺ (EEO x n_DVP 110 kV=0 V EEO x n_PSS 400 kV = 0), 
EEO x n_DVP 110 kV, n_PSS 400 kV∈N0;
EEO x NMT DVP 110 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x NMT DVP 110 kV i) kao granični element ⟺ (EEO x n_DVP 110 kV>0 ∧ ), 
i=0 ⟹ ∄ (EEO x NMT DVP 110 kV i) kao granicni element ⟺ (EEO x n_DVP 110 kV=0 V ),
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ (EEO x n_DVP 110 kV>0 ∧ ),
i∈{0} ⟺ (EEO x n_DVP 110 kV=0 V ), 
EEO x n_DVP 110 kV, n_PSS 400 kV∈N0;
EEO x IRSU DVP x kV i: 
∀i (i≠0) ⟹ ∃ (EEO x IRSU DVP x kV i) kao granični element ⟺ (EEO x n_DVP x kV>0 ∧ EEO x n_PSS x kV = 0), 
i=0 ⟹ ∄ (EEO x IRSU DVP x kV i) kao granicni element ⟺ (EEO x n_DVP x kV=0 V EEO x n_PSS 400 kV > 0),
i∈{1, ..., EEO x n_DVP x kV} ⟺ (EEO x n_DVP x kV>0 ∧ EEO x n_PSS x kV = 0),
i∈{0} ⟺ (EEO x n_DVP x kV=0 V EEO x n_PSS 400 kV > 0), 
EEO x n_DVP x kV, n_PSS 400 kV∈N0;
EEO x SMT DVP x kV i: 
∀i (i≠0) ⟹ ∃ (EEO x SMT DVP x kV i) kao granični element ⟺ (EEO x n_DVP x kV>0 ∧ EEO x n_PSS x kV > 0), 
i=0 ⟹ ∄ (EEO x SMT DVP x kV i) kao granicni element ⟺ (EEO x n_DVP x kV=0 V EEO x n_PSS 400 kV = 0),
i∈{1, ..., EEO x n_DVP x kV} ⟺ (EEO x n_DVP x kV>0 ∧ EEO x n_PSS x kV > 0),
i∈{0} ⟺ (EEO x n_DVP x kV=0 V EEO x n_PSS 400 kV = 0), 
EEO x n_DVP x kV, n_PSS 400 kV∈N0;
EEO x NMT DVP x kV i: 
∀i (i≠0) ⟹ ∃ (EEO x NMT DVP x kV i) kao granični element ⟺ (EEO x n_DVP x kV>0 ∧ ), 
i=0 ⟹ ∄ (EEO x NMT DVP x kV i) kao granicni element ⟺ (EEO x n_DVP x kV=0 V ),
i∈{1, ..., EEO x n_DVP x kV} ⟺ (EEO x n_DVP x kV>0 ∧ ),
i∈{0} ⟺ (EEO x n_DVP x kV=0 V ), 
EEO x n_DVP x kV, n_PSS 400 kV∈N0;
EEO x IRSU KBP 400 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x IRSU KBP 400 kV i) kao granični element ⟺ (EEO x n_KBP 400 kV>0 ∧ EEO x n_PSS 400 kV = 0), 
i=0 ⟹ ∄ (EEO x IRSU KBP 400 kV i) kao granicni element ⟺ (EEO x n_KBP 400 kV=0 V EEO x n_PSS 400 kV > 0),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ (EEO x n_KBP 400 kV>0 ∧ EEO x n_PSS 400 kV = 0),
i∈{0} ⟺ (EEO x n_KBP 400 kV=0 V EEO x n_PSS 400 kV > 0), 
EEO x n_KBP 400 kV, n_PSS 400 kV∈N0;
EEO x SMT KBP 400 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x SMT KBP 400 kV i) kao granični element ⟺ (EEO x n_KBP 400 kV>0 ∧ EEO x n_PSS 400 kV > 0), 
i=0 ⟹ ∄ (EEO x SMT KBP 400 kV i) kao granicni element ⟺ (EEO x n_KBP 400 kV=0 V EEO x n_PSS 400 kV = 0),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ (EEO x n_KBP 400 kV>0 ∧ EEO x n_PSS 400 kV > 0),
i∈{0} ⟺ (EEO x n_KBP 400 kV=0 V EEO x n_PSS 400 kV = 0), 
EEO x n_KBP 400 kV, n_PSS 400 kV∈N0;
EEO x NMT KBP 400 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x NMT KBP 400 kV i) kao granični element ⟺ (EEO x n_KBP 400 kV>0 ∧ ), 
i=0 ⟹ ∄ (EEO x NMT KBP 400 kV i) kao granicni element ⟺ (EEO x n_KBP 400 kV=0 V ),
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ (EEO x n_KBP 400 kV>0 ∧ ),
i∈{0} ⟺ (EEO x n_KBP 400 kV=0 V ), 
EEO x n_KBP 400 kV, n_PSS 400 kV∈N0;
EEO x IRSU KBP 220 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x IRSU KBP 220 kV i) kao granični element ⟺ (EEO x n_KBP 220 kV>0 ∧ EEO x n_PSS 220 kV = 0), 
i=0 ⟹ ∄ (EEO x IRSU KBP 220 kV i) kao granicni element ⟺ (EEO x n_KBP 220 kV=0 V EEO x n_PSS 400 kV > 0),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ (EEO x n_KBP 220 kV>0 ∧ EEO x n_PSS 220 kV = 0),
i∈{0} ⟺ (EEO x n_KBP 220 kV=0 V EEO x n_PSS 400 kV > 0), 
EEO x n_KBP 220 kV, n_PSS 400 kV∈N0;
EEO x SMT KBP 220 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x SMT KBP 220 kV i) kao granični element ⟺ (EEO x n_KBP 220 kV>0 ∧ EEO x n_PSS 220 kV > 0), 
i=0 ⟹ ∄ (EEO x SMT KBP 220 kV i) kao granicni element ⟺ (EEO x n_KBP 220 kV=0 V EEO x n_PSS 400 kV = 0),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ (EEO x n_KBP 220 kV>0 ∧ EEO x n_PSS 220 kV > 0),
i∈{0} ⟺ (EEO x n_KBP 220 kV=0 V EEO x n_PSS 400 kV = 0), 
EEO x n_KBP 220 kV, n_PSS 400 kV∈N0;
EEO x NMT KBP 220 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x NMT KBP 220 kV i) kao granični element ⟺ (EEO x n_KBP 220 kV>0 ∧ ), 
i=0 ⟹ ∄ (EEO x NMT KBP 220 kV i) kao granicni element ⟺ (EEO x n_KBP 220 kV=0 V ),
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ (EEO x n_KBP 220 kV>0 ∧ ),
i∈{0} ⟺ (EEO x n_KBP 220 kV=0 V ), 
EEO x n_KBP 220 kV, n_PSS 400 kV∈N0;
EEO x IRSU KBP 110 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x IRSU KBP 110 kV i) kao granični element ⟺ (EEO x n_KBP 110 kV>0 ∧ EEO x n_PSS 110 kV = 0), 
i=0 ⟹ ∄ (EEO x IRSU KBP 110 kV i) kao granicni element ⟺ (EEO x n_KBP 110 kV=0 V EEO x n_PSS 400 kV > 0),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ (EEO x n_KBP 110 kV>0 ∧ EEO x n_PSS 110 kV = 0),
i∈{0} ⟺ (EEO x n_KBP 110 kV=0 V EEO x n_PSS 400 kV > 0), 
EEO x n_KBP 110 kV, n_PSS 400 kV∈N0;
EEO x SMT KBP 110 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x SMT KBP 110 kV i) kao granični element ⟺ (EEO x n_KBP 110 kV>0 ∧ EEO x n_PSS 110 kV > 0), 
i=0 ⟹ ∄ (EEO x SMT KBP 110 kV i) kao granicni element ⟺ (EEO x n_KBP 110 kV=0 V EEO x n_PSS 400 kV = 0),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ (EEO x n_KBP 110 kV>0 ∧ EEO x n_PSS 110 kV > 0),
i∈{0} ⟺ (EEO x n_KBP 110 kV=0 V EEO x n_PSS 400 kV = 0), 
EEO x n_KBP 110 kV, n_PSS 400 kV∈N0;
EEO x NMT KBP 110 kV i: 
∀i (i≠0) ⟹ ∃ (EEO x NMT KBP 110 kV i) kao granični element ⟺ (EEO x n_KBP 110 kV>0 ∧ ), 
i=0 ⟹ ∄ (EEO x NMT KBP 110 kV i) kao granicni element ⟺ (EEO x n_KBP 110 kV=0 V ),
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ (EEO x n_KBP 110 kV>0 ∧ ),
i∈{0} ⟺ (EEO x n_KBP 110 kV=0 V ), 
EEO x n_KBP 110 kV, n_PSS 400 kV∈N0;
EEO x IRSU KBP x kV i: 
∀i (i≠0) ⟹ ∃ (EEO x IRSU KBP x kV i) kao granični element ⟺ (EEO x n_KBP x kV>0 ∧ EEO x n_PSS x kV = 0), 
i=0 ⟹ ∄ (EEO x IRSU KBP x kV i) kao granicni element ⟺ (EEO x n_KBP x kV=0 V EEO x n_PSS 400 kV > 0),
i∈{1, ..., EEO x n_KBP x kV} ⟺ (EEO x n_KBP x kV>0 ∧ EEO x n_PSS x kV = 0),
i∈{0} ⟺ (EEO x n_KBP x kV=0 V EEO x n_PSS 400 kV > 0), 
EEO x n_KBP x kV, n_PSS 400 kV∈N0;
EEO x SMT KBP x kV i: 
∀i (i≠0) ⟹ ∃ (EEO x SMT KBP x kV i) kao granični element ⟺ (EEO x n_KBP x kV>0 ∧ EEO x n_PSS x kV > 0), 
i=0 ⟹ ∄ (EEO x SMT KBP x kV i) kao granicni element ⟺ (EEO x n_KBP x kV=0 V EEO x n_PSS 400 kV = 0),
i∈{1, ..., EEO x n_KBP x kV} ⟺ (EEO x n_KBP x kV>0 ∧ EEO x n_PSS x kV > 0),
i∈{0} ⟺ (EEO x n_KBP x kV=0 V EEO x n_PSS 400 kV = 0), 
EEO x n_KBP x kV, n_PSS 400 kV∈N0;
EEO x NMT KBP x kV i: 
∀i (i≠0) ⟹ ∃ (EEO x NMT KBP x kV i) kao granični element ⟺ (EEO x n_KBP x kV>0 ∧ ), 
i=0 ⟹ ∄ (EEO x NMT KBP x kV i) kao granicni element ⟺ (EEO x n_KBP x kV=0 V ),
i∈{1, ..., EEO x n_KBP x kV} ⟺ (EEO x n_KBP x kV>0 ∧ ),
i∈{0} ⟺ (EEO x n_KBP x kV=0 V ), 
EEO x n_KBP x kV, n_PSS 400 kV∈N0;
Granični elementi elektroenergetske opreme koja ne pripada EEO
Granični elementi elektroenergetske opreme koja ne pripada EEO su:
DV 400 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST DV 400 kV ∨ ∀ (x, i, y, j): (DV 400 kV EEO x (i) EEO y (j)) ∈ LISTA DV 400 kV) ⟹ ∃ (DV 400 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST DV 400 kV ∨ ∀ (x, i, y, j): (DV 400 kV EEO x (i) EEO y (j)) ∉ LISTA DV 400 kV) ⟹ ∄ (DV 400 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO y n_DVP 400 kV} ⟺ EEO y n_DVP 400 kV>0, j∈{0} ⟺ EEO y n_DVP 400 kV=0, 
n_EEO∈N, EEO x n_DVP 400 kV, EEO y n_DVP 400 kV∈N0;
DV 220 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST DV 220 kV ∨ ∀ (x, i, y, j): (DV 220 kV EEO x (i) EEO y (j)) ∈ LISTA DV 220 kV) ⟹ ∃ (DV 220 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST DV 220 kV ∨ ∀ (x, i, y, j): (DV 220 kV EEO x (i) EEO y (j)) ∉ LISTA DV 220 kV) ⟹ ∄ (DV 220 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO y n_DVP 220 kV} ⟺ EEO y n_DVP 220 kV>0, j∈{0} ⟺ EEO y n_DVP 220 kV=0, 
n_EEO∈N, EEO x n_DVP 220 kV, EEO y n_DVP 220 kV∈N0;
DV 110 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST DV 110 kV ∨ ∀ (x, i, y, j): (DV 110 kV EEO x (i) EEO y (j)) ∈ LISTA DV 110 kV) ⟹ ∃ (DV 110 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST DV 110 kV ∨ ∀ (x, i, y, j): (DV 110 kV EEO x (i) EEO y (j)) ∉ LISTA DV 110 kV) ⟹ ∄ (DV 110 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO y n_DVP 110 kV} ⟺ EEO y n_DVP 110 kV>0, j∈{0} ⟺ EEO y n_DVP 110 kV=0, 
n_EEO∈N, EEO x n_DVP 110 kV, EEO y n_DVP 110 kV∈N0;
DV x kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST DV x kV ∨ ∀ (x, i, y, j): (DV x kV EEO x (i) EEO y (j)) ∈ LISTA DV x kV) ⟹ ∃ (DV x kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST DV x kV ∨ ∀ (x, i, y, j): (DV x kV EEO x (i) EEO y (j)) ∉ LISTA DV x kV) ⟹ ∄ (DV x kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO y n_DVP x kV} ⟺ EEO y n_DVP x kV>0, j∈{0} ⟺ EEO y n_DVP x kV=0, 
n_EEO∈N, EEO x n_DVP x kV, EEO y n_DVP x kV∈N0;
KB 400 kVEEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST KB 400 kV ∨ ∀ (x, i, y, j): (KB 400 kVEEO x (i) EEO y (j)) ∈ LISTA KB 400 kV) ⟹ ∃ (KB 400 kVEEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST KB 400 kV ∨ ∀ (x, i, y, j): (KB 400 kVEEO x (i) EEO y (j)) ∉ LISTA KB 400 kV) ⟹ ∄ (KB 400 kVEEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO y n_KBP 400 kV} ⟺ EEO y n_KBP 400 kV>0, j∈{0} ⟺ EEO y n_KBP 400 kV=0, 
n_EEO∈N, EEO x n_KBP 400 kV, EEO y n_KBP 400 kV∈N0;
KB 220 kVEEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST KB 220 kV ∨ ∀ (x, i, y, j): (KB 220 kVEEO x (i) EEO y (j)) ∈ LISTA KB 220 kV) ⟹ ∃ (KB 220 kVEEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST KB 220 kV ∨ ∀ (x, i, y, j): (KB 220 kVEEO x (i) EEO y (j)) ∉ LISTA KB 220 kV) ⟹ ∄ (KB 220 kVEEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO y n_KBP 220 kV} ⟺ EEO y n_KBP 220 kV>0, j∈{0} ⟺ EEO y n_KBP 220 kV=0, 
n_EEO∈N, EEO x n_KBP 220 kV, EEO y n_KBP 220 kV∈N0;
KB 110 kVEEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST KB 110 kV ∨ ∀ (x, i, y, j): (KB 110 kVEEO x (i) EEO y (j)) ∈ LISTA KB 110 kV) ⟹ ∃ (KB 110 kVEEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST KB 110 kV ∨ ∀ (x, i, y, j): (KB 110 kVEEO x (i) EEO y (j)) ∉ LISTA KB 110 kV) ⟹ ∄ (KB 110 kVEEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO y n_KBP 110 kV} ⟺ EEO y n_KBP 110 kV>0, j∈{0} ⟺ EEO y n_KBP 110 kV=0, 
n_EEO∈N, EEO x n_KBP 110 kV, EEO y n_KBP 110 kV∈N0;
KB x kVEEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST KB x kV ∨ ∀ (x, i, y, j): (KB x kVEEO x (i) EEO y (j)) ∈ LISTA KB x kV) ⟹ ∃ (KB x kVEEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST KB x kV ∨ ∀ (x, i, y, j): (KB x kVEEO x (i) EEO y (j)) ∉ LISTA KB x kV) ⟹ ∄ (KB x kVEEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO y n_KBP x kV} ⟺ EEO y n_KBP x kV>0, j∈{0} ⟺ EEO y n_KBP x kV=0, 
n_EEO∈N, EEO x n_KBP x kV, EEO y n_KBP x kV∈N0;
MV (DV+KB) 400 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (DV+KB) 400 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 400 kV EEO x (i) EEO y (j)) ∈ LISTA MV (DV+KB) 400 kV) ⟹ ∃ (MV (DV+KB) 400 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (DV+KB) 400 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 400 kV EEO x (i) EEO y (j)) ∉ LISTA MV (DV+KB) 400 kV) ⟹ ∄ (MV (DV+KB) 400 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO y n_KBP 400 kV} ⟺ EEO y n_KBP 400 kV>0, j∈{0} ⟺ EEO y n_KBP 400 kV=0, 
n_EEO∈N, EEO x n_DVP 400 kV, EEO y n_KBP 400 kV∈N0;
MV (DV+KB) 220 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (DV+KB) 220 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 220 kV EEO x (i) EEO y (j)) ∈ LISTA MV (DV+KB) 220 kV) ⟹ ∃ (MV (DV+KB) 220 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (DV+KB) 220 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 220 kV EEO x (i) EEO y (j)) ∉ LISTA MV (DV+KB) 220 kV) ⟹ ∄ (MV (DV+KB) 220 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO y n_KBP 220 kV} ⟺ EEO y n_KBP 220 kV>0, j∈{0} ⟺ EEO y n_KBP 220 kV=0, 
n_EEO∈N, EEO x n_DVP 220 kV, EEO y n_KBP 220 kV∈N0;
MV (DV+KB) 110 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (DV+KB) 110 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 110 kV EEO x (i) EEO y (j)) ∈ LISTA MV (DV+KB) 110 kV) ⟹ ∃ (MV (DV+KB) 110 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (DV+KB) 110 kV ∨ ∀ (x, i, y, j): (MV (DV+KB) 110 kV EEO x (i) EEO y (j)) ∉ LISTA MV (DV+KB) 110 kV) ⟹ ∄ (MV (DV+KB) 110 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO y n_KBP 110 kV} ⟺ EEO y n_KBP 110 kV>0, j∈{0} ⟺ EEO y n_KBP 110 kV=0, 
n_EEO∈N, EEO x n_DVP 110 kV, EEO y n_KBP 110 kV∈N0;
MV (DV+KB) x kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (DV+KB) x kV ∨ ∀ (x, i, y, j): (MV (DV+KB) x kV EEO x (i) EEO y (j)) ∈ LISTA MV (DV+KB) x kV) ⟹ ∃ (MV (DV+KB) x kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (DV+KB) x kV ∨ ∀ (x, i, y, j): (MV (DV+KB) x kV EEO x (i) EEO y (j)) ∉ LISTA MV (DV+KB) x kV) ⟹ ∄ (MV (DV+KB) x kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO y n_KBP x kV} ⟺ EEO y n_KBP x kV>0, j∈{0} ⟺ EEO y n_KBP x kV=0, 
n_EEO∈N, EEO x n_DVP x kV, EEO y n_KBP x kV∈N0;
MV (KB+DV) 400 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (KB+DV) 400 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 400 kV EEO x (i) EEO y (j)) ∈ LISTA MV (KB+DV) 400 kV) ⟹ ∃ (MV (KB+DV) 400 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (KB+DV) 400 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 400 kV EEO x (i) EEO y (j)) ∉ LISTA MV (KB+DV) 400 kV) ⟹ ∄ (MV (KB+DV) 400 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO y n_DVP 400 kV} ⟺ EEO y n_DVP 400 kV>0, j∈{0} ⟺ EEO y n_DVP 400 kV=0, 
n_EEO∈N, EEO x n_KBP 400 kV, EEO y n_DVP 400 kV∈N0;
MV (KB+DV) 220 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (KB+DV) 220 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 220 kV EEO x (i) EEO y (j)) ∈ LISTA MV (KB+DV) 220 kV) ⟹ ∃ (MV (KB+DV) 220 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (KB+DV) 220 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 220 kV EEO x (i) EEO y (j)) ∉ LISTA MV (KB+DV) 220 kV) ⟹ ∄ (MV (KB+DV) 220 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO y n_DVP 220 kV} ⟺ EEO y n_DVP 220 kV>0, j∈{0} ⟺ EEO y n_DVP 220 kV=0, 
n_EEO∈N, EEO x n_KBP 220 kV, EEO y n_DVP 220 kV∈N0;
MV (KB+DV) 110 kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (KB+DV) 110 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 110 kV EEO x (i) EEO y (j)) ∈ LISTA MV (KB+DV) 110 kV) ⟹ ∃ (MV (KB+DV) 110 kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (KB+DV) 110 kV ∨ ∀ (x, i, y, j): (MV (KB+DV) 110 kV EEO x (i) EEO y (j)) ∉ LISTA MV (KB+DV) 110 kV) ⟹ ∄ (MV (KB+DV) 110 kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO y n_DVP 110 kV} ⟺ EEO y n_DVP 110 kV>0, j∈{0} ⟺ EEO y n_DVP 110 kV=0, 
n_EEO∈N, EEO x n_KBP 110 kV, EEO y n_DVP 110 kV∈N0;
MV (KB+DV) x kV EEO x (i) EEO y (j):
(∀ (x, i, y, j) ∈ POVEZANOST MV (KB+DV) x kV ∨ ∀ (x, i, y, j): (MV (KB+DV) x kV EEO x (i) EEO y (j)) ∈ LISTA MV (KB+DV) x kV) ⟹ ∃ (MV (KB+DV) x kV EEO x (i) EEO y (j)),
(∀ (x, i, y, j) ∉ POVEZANOST MV (KB+DV) x kV ∨ ∀ (x, i, y, j): (MV (KB+DV) x kV EEO x (i) EEO y (j)) ∉ LISTA MV (KB+DV) x kV) ⟹ ∄ (MV (KB+DV) x kV EEO x (i) EEO y (j)),
gde x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO y n_DVP x kV} ⟺ EEO y n_DVP x kV>0, j∈{0} ⟺ EEO y n_DVP x kV=0, 
n_EEO∈N, EEO x n_KBP x kV, EEO y n_DVP x kV∈N0;
### Veza graničnih elemenata
Povezanost graničnih elemenata elektroenergetske opreme koja pripada EEO x i EEO y, gde x,y ∈{1, ..., n_EEO}, x≠y, n_EEO>1, n_EEO∈N, sa graničnim elementima elektroenergetske opreme koja ne pripada EEO definisana je sa:
(EEO x IRSU DVP 400 kV i <-> DV 400 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 400 kV = 0,
(EEO x SMT DVP 400 kV i <-> DV 400 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 400 kV > 0,
EEO x NMT DVP 400 kV i <-> DV 400 kV EEO x (i) EEO y (j),
(DV 400 kV EEO x (i) EEO y (j) <-> EEO y IRSU DVP 400 kV j) ⟺ EEO y n_PSS 400 kV = 0,
(DV 400 kV EEO x (i) EEO y (j) <-> EEO y SMT DVP 400 kV j) ⟺ EEO y n_PSS 400 kV > 0,
DV 400 kV EEO x (i) EEO y (j) <-> EEO y NMT DVP 400 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO y n_DVP 400 kV} ⟺ EEO y n_DVP 400 kV>0, j∈{0} ⟺ EEO y n_DVP 400 kV=0, 
n_EEO∈N, EEO x n_DVP 400 kV, EEO y n_DVP 400 kV∈N0;
(EEO x IRSU DVP 220 kV i <-> DV 220 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 220 kV = 0,
(EEO x SMT DVP 220 kV i <-> DV 220 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 220 kV > 0,
EEO x NMT DVP 220 kV i <-> DV 220 kV EEO x (i) EEO y (j),
(DV 220 kV EEO x (i) EEO y (j) <-> EEO y IRSU DVP 220 kV j) ⟺ EEO y n_PSS 220 kV = 0,
(DV 220 kV EEO x (i) EEO y (j) <-> EEO y SMT DVP 220 kV j) ⟺ EEO y n_PSS 220 kV > 0,
DV 220 kV EEO x (i) EEO y (j) <-> EEO y NMT DVP 220 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO y n_DVP 220 kV} ⟺ EEO y n_DVP 220 kV>0, j∈{0} ⟺ EEO y n_DVP 220 kV=0, 
n_EEO∈N, EEO x n_DVP 220 kV, EEO y n_DVP 220 kV∈N0;
(EEO x IRSU DVP 110 kV i <-> DV 110 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 110 kV = 0,
(EEO x SMT DVP 110 kV i <-> DV 110 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 110 kV > 0,
EEO x NMT DVP 110 kV i <-> DV 110 kV EEO x (i) EEO y (j),
(DV 110 kV EEO x (i) EEO y (j) <-> EEO y IRSU DVP 110 kV j) ⟺ EEO y n_PSS 110 kV = 0,
(DV 110 kV EEO x (i) EEO y (j) <-> EEO y SMT DVP 110 kV j) ⟺ EEO y n_PSS 110 kV > 0,
DV 110 kV EEO x (i) EEO y (j) <-> EEO y NMT DVP 110 kV j,
gde: 
x, y∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO y n_DVP 110 kV} ⟺ EEO y n_DVP 110 kV>0, j∈{0} ⟺ EEO y n_DVP 110 kV=0, 
n_EEO∈N, EEO x n_DVP 110 kV, EEO y n_DVP 110 kV∈N0;
(EEO x IRSU DVP x kV i <-> DV x kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS x kV = 0,
(EEO x SMT DVP x kV i <-> DV x kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS x kV > 0,
EEO x NMT DVP x kV i <-> DV x kV EEO x (i) EEO y (j),
(DV x kV EEO x (i) EEO y (j) <-> EEO y IRSU DVP x kV j) ⟺ EEO y n_PSS x kV = 0,
(DV x kV EEO x (i) EEO y (j) <-> EEO y SMT DVP x kV j) ⟺ EEO y n_PSS x kV > 0,
DV x kV EEO x (i) EEO y (j) <-> EEO y NMT DVP x kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO y n_DVP x kV} ⟺ EEO y n_DVP x kV>0, j∈{0} ⟺ EEO y n_DVP x kV=0, 
n_EEO∈N, EEO x n_DVP x kV, EEO y n_DVP x kV∈N0;
(EEO x IRSU KBP 400 kV i <-> KB 400 kVEEO x (i) EEO y (j)) ⟺ EEO x n_PSS 400 kV = 0,
(EEO x SMT KBP 400 kV i <-> KB 400 kVEEO x (i) EEO y (j)) ⟺ EEO x n_PSS 400 kV > 0,
EEO x NMT KBP 400 kV i <-> KB 400 kVEEO x (i) EEO y (j),
(KB 400 kVEEO x (i) EEO y (j) <-> EEO y IRSU KBP 400 kV j) ⟺ EEO y n_PSS 400 kV = 0,
(KB 400 kVEEO x (i) EEO y (j) <-> EEO y SMT KBP 400 kV j) ⟺ EEO y n_PSS 400 kV > 0,
KB 400 kVEEO x (i) EEO y (j) <-> EEO y NMT KBP 400 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO y n_KBP 400 kV} ⟺ EEO y n_KBP 400 kV>0, j∈{0} ⟺ EEO y n_KBP 400 kV=0, 
n_EEO∈N, EEO x n_KBP 400 kV, EEO y n_KBP 400 kV∈N0;
(EEO x IRSU KBP 220 kV i <-> KB 220 kVEEO x (i) EEO y (j)) ⟺ EEO x n_PSS 220 kV = 0,
(EEO x SMT KBP 220 kV i <-> KB 220 kVEEO x (i) EEO y (j)) ⟺ EEO x n_PSS 220 kV > 0,
EEO x NMT KBP 220 kV i <-> KB 220 kVEEO x (i) EEO y (j),
(KB 220 kVEEO x (i) EEO y (j) <-> EEO y IRSU KBP 220 kV j) ⟺ EEO y n_PSS 220 kV = 0,
(KB 220 kVEEO x (i) EEO y (j) <-> EEO y SMT KBP 220 kV j) ⟺ EEO y n_PSS 220 kV > 0,
KB 220 kVEEO x (i) EEO y (j) <-> EEO y NMT KBP 220 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO y n_KBP 220 kV} ⟺ EEO y n_KBP 220 kV>0, j∈{0} ⟺ EEO y n_KBP 220 kV=0, 
n_EEO∈N, EEO x n_KBP 220 kV, EEO y n_KBP 220 kV∈N0;
(EEO x IRSU KBP 110 kV i <-> KB 110 kVEEO x (i) EEO y (j)) ⟺ EEO x n_PSS 110 kV = 0,
(EEO x SMT KBP 110 kV i <-> KB 110 kVEEO x (i) EEO y (j)) ⟺ EEO x n_PSS 110 kV > 0,
EEO x NMT KBP 110 kV i <-> KB 110 kVEEO x (i) EEO y (j),
(KB 110 kVEEO x (i) EEO y (j) <-> EEO y IRSU KBP 110 kV j) ⟺ EEO y n_PSS 110 kV = 0,
(KB 110 kVEEO x (i) EEO y (j) <-> EEO y SMT KBP 110 kV j) ⟺ EEO y n_PSS 110 kV > 0,
KB 110 kVEEO x (i) EEO y (j) <-> EEO y NMT KBP 110 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO y n_KBP 110 kV} ⟺ EEO y n_KBP 110 kV>0, j∈{0} ⟺ EEO y n_KBP 110 kV=0, 
n_EEO∈N, EEO x n_KBP 110 kV, EEO y n_KBP 110 kV∈N0;
(EEO x IRSU KBP x kV i <-> KB x kVEEO x (i) EEO y (j)) ⟺ EEO x n_PSS x kV = 0,
(EEO x SMT KBP x kV i <-> KB x kVEEO x (i) EEO y (j)) ⟺ EEO x n_PSS x kV > 0,
EEO x NMT KBP x kV i <-> KB x kVEEO x (i) EEO y (j),
(KB x kVEEO x (i) EEO y (j) <-> EEO y IRSU KBP x kV j) ⟺ EEO y n_PSS x kV = 0,
(KB x kVEEO x (i) EEO y (j) <-> EEO y SMT KBP x kV j) ⟺ EEO y n_PSS x kV > 0,
KB x kVEEO x (i) EEO y (j) <-> EEO y NMT KBP x kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO y n_KBP x kV} ⟺ EEO y n_KBP x kV>0, j∈{0} ⟺ EEO y n_KBP x kV=0, 
n_EEO∈N, EEO x n_KBP x kV, EEO y n_KBP x kV∈N0;
(EEO x IRSU DVP 400 kV i <-> MV (DV+KB) 400 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 400 kV = 0,
(EEO x SMT DVP 400 kV i <-> MV (DV+KB) 400 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 400 kV > 0,
EEO x NMT DVP 400 kV i <-> MV (DV+KB) 400 kV EEO x (i) EEO y (j),
(MV (DV+KB) 400 kV EEO x (i) EEO y (j) <-> EEO y IRSU KBP 400 kV j) ⟺ EEO y n_PSS 400 kV = 0,
(MV (DV+KB) 400 kV EEO x (i) EEO y (j) <-> EEO y SMT KBP 400 kV j) ⟺ EEO y n_PSS 400 kV > 0,
MV (DV+KB) 400 kV EEO x (i) EEO y (j) <-> EEO y NMT KBP 400 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
j∈{1, ..., EEO y n_KBP 400 kV} ⟺ EEO y n_KBP 400 kV>0, j∈{0} ⟺ EEO y n_KBP 400 kV=0, 
n_EEO∈N, EEO x n_DVP 400 kV, EEO y n_KBP 400 kV∈N0;
(EEO x IRSU DVP 220 kV i <-> MV (DV+KB) 220 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 220 kV = 0,
(EEO x SMT DVP 220 kV i <-> MV (DV+KB) 220 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 220 kV > 0,
EEO x NMT DVP 220 kV i <-> MV (DV+KB) 220 kV EEO x (i) EEO y (j),
(MV (DV+KB) 220 kV EEO x (i) EEO y (j) <-> EEO y IRSU KBP 220 kV j) ⟺ EEO y n_PSS 220 kV = 0,
(MV (DV+KB) 220 kV EEO x (i) EEO y (j) <-> EEO y SMT KBP 220 kV j) ⟺ EEO y n_PSS 220 kV > 0,
MV (DV+KB) 220 kV EEO x (i) EEO y (j) <-> EEO y NMT KBP 220 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
j∈{1, ..., EEO y n_KBP 220 kV} ⟺ EEO y n_KBP 220 kV>0, j∈{0} ⟺ EEO y n_KBP 220 kV=0, 
n_EEO∈N, EEO x n_DVP 220 kV, EEO y n_KBP 220 kV∈N0;
(EEO x IRSU DVP 110 kV i <-> MV (DV+KB) 110 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 110 kV = 0,
(EEO x SMT DVP 110 kV i <-> MV (DV+KB) 110 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 110 kV > 0,
EEO x NMT DVP 110 kV i <-> MV (DV+KB) 110 kV EEO x (i) EEO y (j),
(MV (DV+KB) 110 kV EEO x (i) EEO y (j) <-> EEO y IRSU KBP 110 kV j) ⟺ EEO y n_PSS 110 kV = 0,
(MV (DV+KB) 110 kV EEO x (i) EEO y (j) <-> EEO y SMT KBP 110 kV j) ⟺ EEO y n_PSS 110 kV > 0,
MV (DV+KB) 110 kV EEO x (i) EEO y (j) <-> EEO y NMT KBP 110 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
j∈{1, ..., EEO y n_KBP 110 kV} ⟺ EEO y n_KBP 110 kV>0, j∈{0} ⟺ EEO y n_KBP 110 kV=0, 
n_EEO∈N, EEO x n_DVP 110 kV, EEO y n_KBP 110 kV∈N0;
(EEO x IRSU DVP x kV i <-> MV (DV+KB) x kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS x kV = 0,
(EEO x SMT DVP x kV i <-> MV (DV+KB) x kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS x kV > 0,
EEO x NMT DVP x kV i <-> MV (DV+KB) x kV EEO x (i) EEO y (j),
(MV (DV+KB) x kV EEO x (i) EEO y (j) <-> EEO y IRSU KBP x kV j) ⟺ EEO y n_PSS x kV = 0,
(MV (DV+KB) x kV EEO x (i) EEO y (j) <-> EEO y SMT KBP x kV j) ⟺ EEO y n_PSS x kV > 0,
MV (DV+KB) x kV EEO x (i) EEO y (j) <-> EEO y NMT KBP x kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
j∈{1, ..., EEO y n_KBP x kV} ⟺ EEO y n_KBP x kV>0, j∈{0} ⟺ EEO y n_KBP x kV=0, 
n_EEO∈N, EEO x n_DVP x kV, EEO y n_KBP x kV∈N0;
(EEO x IRSU KBP 400 kV i <-> MV (KB+DV) 400 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 400 kV = 0,
(EEO x SMT KBP 400 kV i <-> MV (KB+DV) 400 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 400 kV > 0,
EEO x NMT KBP 400 kV i <-> MV (KB+DV) 400 kV EEO x (i) EEO y (j),
(MV (KB+DV) 400 kV EEO x (i) EEO y (j) <-> EEO y IRSU DVP 400 kV j) ⟺ EEO y n_PSS 400 kV = 0,
(MV (KB+DV) 400 kV EEO x (i) EEO y (j) <-> EEO y SMT DVP 400 kV j) ⟺ EEO y n_PSS 400 kV > 0,
MV (KB+DV) 400 kV EEO x (i) EEO y (j) <-> EEO y NMT DVP 400 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
j∈{1, ..., EEO y n_DVP 400 kV} ⟺ EEO y n_DVP 400 kV>0, j∈{0} ⟺ EEO y n_DVP 400 kV=0, 
n_EEO∈N, EEO x n_KBP 400 kV, EEO y n_DVP 400 kV∈N0;
(EEO x IRSU KBP 220 kV i <-> MV (KB+DV) 220 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 220 kV = 0,
(EEO x SMT KBP 220 kV i <-> MV (KB+DV) 220 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 220 kV > 0,
EEO x NMT KBP 220 kV i <-> MV (KB+DV) 220 kV EEO x (i) EEO y (j),
(MV (KB+DV) 220 kV EEO x (i) EEO y (j) <-> EEO y IRSU DVP 220 kV j) ⟺ EEO y n_PSS 220 kV = 0,
(MV (KB+DV) 220 kV EEO x (i) EEO y (j) <-> EEO y SMT DVP 220 kV j) ⟺ EEO y n_PSS 220 kV > 0,
MV (KB+DV) 220 kV EEO x (i) EEO y (j) <-> EEO y NMT DVP 220 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
j∈{1, ..., EEO y n_DVP 220 kV} ⟺ EEO y n_DVP 220 kV>0, j∈{0} ⟺ EEO y n_DVP 220 kV=0, 
n_EEO∈N, EEO x n_KBP 220 kV, EEO y n_DVP 220 kV∈N0;
(EEO x IRSU KBP 110 kV i <-> MV (KB+DV) 110 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 110 kV = 0,
(EEO x SMT KBP 110 kV i <-> MV (KB+DV) 110 kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS 110 kV > 0,
EEO x NMT KBP 110 kV i <-> MV (KB+DV) 110 kV EEO x (i) EEO y (j),
(MV (KB+DV) 110 kV EEO x (i) EEO y (j) <-> EEO y IRSU DVP 110 kV j) ⟺ EEO y n_PSS 110 kV = 0,
(MV (KB+DV) 110 kV EEO x (i) EEO y (j) <-> EEO y SMT DVP 110 kV j) ⟺ EEO y n_PSS 110 kV > 0,
MV (KB+DV) 110 kV EEO x (i) EEO y (j) <-> EEO y NMT DVP 110 kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
j∈{1, ..., EEO y n_DVP 110 kV} ⟺ EEO y n_DVP 110 kV>0, j∈{0} ⟺ EEO y n_DVP 110 kV=0, 
n_EEO∈N, EEO x n_KBP 110 kV, EEO y n_DVP 110 kV∈N0;
(EEO x IRSU KBP x kV i <-> MV (KB+DV) x kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS x kV = 0,
(EEO x SMT KBP x kV i <-> MV (KB+DV) x kV EEO x (i) EEO y (j)) ⟺ EEO x n_PSS x kV > 0,
EEO x NMT KBP x kV i <-> MV (KB+DV) x kV EEO x (i) EEO y (j),
(MV (KB+DV) x kV EEO x (i) EEO y (j) <-> EEO y IRSU DVP x kV j) ⟺ EEO y n_PSS x kV = 0,
(MV (KB+DV) x kV EEO x (i) EEO y (j) <-> EEO y SMT DVP x kV j) ⟺ EEO y n_PSS x kV > 0,
MV (KB+DV) x kV EEO x (i) EEO y (j) <-> EEO y NMT DVP x kV j,
gde: 
x, y ∈{1, ..., n_EEO}, x ≠ y, n_EEO>1, 
i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
j∈{1, ..., EEO y n_DVP x kV} ⟺ EEO y n_DVP x kV>0, j∈{0} ⟺ EEO y n_DVP x kV=0, 
n_EEO∈N, EEO x n_KBP x kV, EEO y n_DVP x kV∈N0;
### Matrica povezanosti EEO
Proizvoljna dva EEO iz skupa EEO x​, gde x∈{1,2, …,n_EEO​}, n_EEO>1, n_EEO∈N, su povezana ako i samo ako postoji makar jedan osnovni element iz skupa osnovnih elemenata elektroenergetske opreme koja ne pripada EEO koji ih spaja. Broj EEO u PS je definisan sa n_EEO.
Za svaki osnovni element iz skupa osnovnih elemenata elektroenergetske opreme koja ne pripada EEO definiše se opšta matrica povezanosti. Opšte matrice povezanosti uključuju sve moguće kombinacije povezanosti svaka dva EEO iz skupa EEO x​, gde x∈{1,2, …,n_EEO​}, n_EEO>1, n_EEO∈N. Stvarne matrice povezanosti koje određuju kako su povezani EEO u PS predstavljaju submatrice opštih matrica povezanosti EEO u PS.
Matrice povezanosti EEO na 400 kV
Opšta matrica povezanosti - DV 400 kV
Svaki red matrice OPŠTA POVEZANOST DV 400 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_DVP 400 kV},
j∈{1, …, EEO y n_DVP 400 kV},
EEO x n_DVP 400 kV>0, EEO y n_DVP 400 kV>0
EEO x n_DVP 400 kV, EEO y n_DVP 400 kV ∈N.
Matrica OPŠTA POVEZANOST DV 400 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST DV 400 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – DV 400 kV
Matrica POVEZANOST DV 400 kV predstavlja submatricu matrice OPŠTA POVEZANOST DV 400 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju DV 400 kV.
Ukoliko

Tada

Opšta matrica povezanosti - KB 400 kV
Svaki red matrice OPŠTA POVEZANOST KB 400 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_KBP 400 kV},
j∈{1, …, EEO y n_KBP 400 kV},
EEO x n_KBP 400 kV>0, EEO y n_KBP 400 kV>0
EEO x n_KBP 400 kV, EEO y n_KBP 400 kV ∈N.
Matrica OPŠTA POVEZANOST KB 400 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST KB 400 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – KB 400 kV
Matrica POVEZANOST KB 400 kV predstavlja submatricu matrice OPŠTA POVEZANOST KB 400 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju KB 400 kV.
Ukoliko

Tada

Opšta matrica povezanosti - MV (DV+KB) 400 kV
Svaki red matrice OPŠTA POVEZANOST MV (DV+KB) 400 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_DVP 400 kV},
j∈{1, …, EEO y n_KBP 400 kV},
EEO x n_DVP 400 kV>0, EEO y n_KBP 400 kV>0
EEO x n_DVP 400 kV, EEO y n_KBP 400 kV ∈N.
Matrica OPŠTA POVEZANOST MV (DV+KB) 400 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST MV (DV+KB) 400 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – MV (DV+KB) 400 kV
Matrica POVEZANOST MV (DV+KB) 400 kV predstavlja submatricu matrice OPŠTA POVEZANOST MV (DV+KB) 400 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju MV (DV+KB) 400 kV.
Ukoliko

Tada

Opšta matrica povezanosti - MV (KB+DV) 400 kV
Svaki red matrice OPŠTA POVEZANOST MV (KB+DV) 400 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_KBP 400 kV},
j∈{1, …, EEO y n_DVP 400 kV},
EEO x n_KBP 400 kV>0, EEO y n_DVP 400 kV>0
EEO x n_KBP 400 kV, EEO y n_DVP 400 kV ∈N.
Matrica OPŠTA POVEZANOST MV (KB+DV) 400 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST MV (KB+DV) 400 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – MV (KB+DV) 400 kV
Matrica POVEZANOST MV (KB+DV) 400 kV predstavlja submatricu matrice OPŠTA POVEZANOST MV (KB+DV) 400 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju MV (KB+DV) 400 kV.
Ukoliko

Tada

Matrice povezanosti EEO na 220 kV
Opšta matrica povezanosti - DV 220 kV
Svaki red matrice OPŠTA POVEZANOST DV 220 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_DVP 220 kV},
j∈{1, …, EEO y n_DVP 220 kV},
EEO x n_DVP 220 kV>0, EEO y n_DVP 220 kV>0
EEO x n_DVP 220 kV, EEO y n_DVP 220 kV ∈N.
Matrica OPŠTA POVEZANOST DV 220 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST DV 220 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – DV 220 kV
Matrica POVEZANOST DV 220 kV predstavlja submatricu matrice OPŠTA POVEZANOST DV 220 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju DV 220 kV.
Ukoliko

Tada

Opšta matrica povezanosti - KB 220 kV
Svaki red matrice OPŠTA POVEZANOST KB 220 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_KBP 220 kV},
j∈{1, …, EEO y n_KBP 220 kV},
EEO x n_KBP 220 kV>0, EEO y n_KBP 220 kV>0
EEO x n_KBP 220 kV, EEO y n_KBP 220 kV ∈N.
Matrica OPŠTA POVEZANOST KB 220 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST KB 220 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – KB 220 kV
Matrica POVEZANOST KB 220 kV predstavlja submatricu matrice OPŠTA POVEZANOST KB 220 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju KB 220 kV.
Ukoliko

Tada

Opšta matrica povezanosti - MV (DV+KB) 220 kV
Svaki red matrice OPŠTA POVEZANOST MV (DV+KB) 220 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_DVP 220 kV},
j∈{1, …, EEO y n_KBP 220 kV},
EEO x n_DVP 220 kV>0, EEO y n_KBP 220 kV>0
EEO x n_DVP 220 kV, EEO y n_KBP 220 kV ∈N.
Matrica OPŠTA POVEZANOST MV (DV+KB) 220 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST MV (DV+KB) 220 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – MV (DV+KB) 220 kV
Matrica POVEZANOST MV (DV+KB) 220 kV predstavlja submatricu matrice OPŠTA POVEZANOST MV (DV+KB) 220 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju MV (DV+KB) 220 kV.
Ukoliko

Tada

Opšta matrica povezanosti - MV (KB+DV) 220 kV
Svaki red matrice OPŠTA POVEZANOST MV (KB+DV) 220 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_KBP 220 kV},
j∈{1, …, EEO y n_DVP 220 kV},
EEO x n_KBP 220 kV>0, EEO y n_DVP 220 kV>0
EEO x n_KBP 220 kV, EEO y n_DVP 220 kV ∈N.
Matrica OPŠTA POVEZANOST MV (KB+DV) 220 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST MV (KB+DV) 220 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – MV (KB+DV) 220 kV
Matrica POVEZANOST MV (KB+DV) 220 kV predstavlja submatricu matrice OPŠTA POVEZANOST MV (KB+DV) 220 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju MV (KB+DV) 220 kV.
Ukoliko

Tada

Matrice povezanosti EEO na 110 kV
Opšta matrica povezanosti - DV 110 kV
Svaki red matrice OPŠTA POVEZANOST DV 110 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_DVP 110 kV},
j∈{1, …, EEO y n_DVP 110 kV},
EEO x n_DVP 110 kV>0, EEO y n_DVP 110 kV>0
EEO x n_DVP 110 kV, EEO y n_DVP 110 kV ∈N.
Matrica OPŠTA POVEZANOST DV 110 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST DV 110 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – DV 110 kV
Matrica POVEZANOST DV 110 kV predstavlja submatricu matrice OPŠTA POVEZANOST DV 110 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju DV 110 kV.
Ukoliko

Tada

Opšta matrica povezanosti - KB 110 kV
Svaki red matrice OPŠTA POVEZANOST KB 110 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_KBP 110 kV},
j∈{1, …, EEO y n_KBP 110 kV},
EEO x n_KBP 110 kV>0, EEO y n_KBP 110 kV>0
EEO x n_KBP 110 kV, EEO y n_KBP 110 kV ∈N.
Matrica OPŠTA POVEZANOST KB 110 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST KB 110 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – KB 110 kV
Matrica POVEZANOST KB 110 kV predstavlja submatricu matrice OPŠTA POVEZANOST KB 110 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju KB 110 kV.
Ukoliko

Tada

Opšta matrica povezanosti - MV (DV+KB) 110 kV
Svaki red matrice OPŠTA POVEZANOST MV (DV+KB) 110 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_DVP 110 kV},
j∈{1, …, EEO y n_KBP 110 kV},
EEO x n_DVP 110 kV>0, EEO y n_KBP 110 kV>0
EEO x n_DVP 110 kV, EEO y n_KBP 110 kV ∈N.
Matrica OPŠTA POVEZANOST MV (DV+KB) 110 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST MV (DV+KB) 110 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – MV (DV+KB) 110 kV
Matrica POVEZANOST MV (DV+KB) 110 kV predstavlja submatricu matrice OPŠTA POVEZANOST MV (DV+KB) 110 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju MV (DV+KB) 110 kV.
Ukoliko

Tada

Opšta matrica povezanosti - MV (KB+DV) 110 kV
Svaki red matrice OPŠTA POVEZANOST MV (KB+DV) 110 kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_KBP 110 kV},
j∈{1, …, EEO y n_DVP 110 kV},
EEO x n_KBP 110 kV>0, EEO y n_DVP 110 kV>0
EEO x n_KBP 110 kV, EEO y n_DVP 110 kV ∈N.
Matrica OPŠTA POVEZANOST MV (KB+DV) 110 kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST MV (KB+DV) 110 kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – MV (KB+DV) 110 kV
Matrica POVEZANOST MV (KB+DV) 110 kV predstavlja submatricu matrice OPŠTA POVEZANOST MV (KB+DV) 110 kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju MV (KB+DV) 110 kV.
Ukoliko

Tada

Matrice povezanosti EEO na x kV
Opšta matrica povezanosti - DV x kV
Svaki red matrice OPŠTA POVEZANOST DV x kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_DVP x kV},
j∈{1, …, EEO y n_DVP x kV},
EEO x n_DVP x kV>0, EEO y n_DVP x kV>0
EEO x n_DVP x kV, EEO y n_DVP x kV ∈N.
Matrica OPŠTA POVEZANOST DV x kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST DV x kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – DV x kV
Matrica POVEZANOST DV x kV predstavlja submatricu matrice OPŠTA POVEZANOST DV x kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju DV x kV.
Ukoliko

Tada

Opšta matrica povezanosti - KB x kV
Svaki red matrice OPŠTA POVEZANOST KB x kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_KBP x kV},
j∈{1, …, EEO y n_KBP x kV},
EEO x n_KBP x kV>0, EEO y n_KBP x kV>0
EEO x n_KBP x kV, EEO y n_KBP x kV ∈N.
Matrica OPŠTA POVEZANOST KB x kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST KB x kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – KB x kV
Matrica POVEZANOST KB x kV predstavlja submatricu matrice OPŠTA POVEZANOST KB x kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju KB x kV.
Ukoliko

Tada

Opšta matrica povezanosti - MV (DV+KB) x kV
Svaki red matrice OPŠTA POVEZANOST MV (DV+KB) x kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_DVP x kV},
j∈{1, …, EEO y n_KBP x kV},
EEO x n_DVP x kV>0, EEO y n_KBP x kV>0
EEO x n_DVP x kV, EEO y n_KBP x kV ∈N.
Matrica OPŠTA POVEZANOST MV (DV+KB) x kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST MV (DV+KB) x kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – MV (DV+KB) x kV
Matrica POVEZANOST MV (DV+KB) x kV predstavlja submatricu matrice OPŠTA POVEZANOST MV (DV+KB) x kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju MV (DV+KB) x kV.
Ukoliko

Tada

Opšta matrica povezanosti - MV (KB+DV) x kV
Svaki red matrice OPŠTA POVEZANOST MV (KB+DV) x kV je uređena četvorka (x,i,y,j), gde:
x∈{1, …,n_EEO},
y∈{1, …,n_EEO},
y > x,
n_EEO>1,
n_EEO∈N.
Za svaku dozvoljenu kombinaciju (x,y) formiraju se sve moguće kombinacije i i j, gde:
i∈{1, …,EEO x n_KBP x kV},
j∈{1, …, EEO y n_DVP x kV},
EEO x n_KBP x kV>0, EEO y n_DVP x kV>0
EEO x n_KBP x kV, EEO y n_DVP x kV ∈N.
Matrica OPŠTA POVEZANOST MV (KB+DV) x kV ima formu
,
čija dimenzija je
.
Ukupan broj redova matrice OPŠTA POVEZANOST MV (KB+DV) x kV je označen sa R i definisan je sa

Submatrica opšte matrice povezanosti – MV (KB+DV) x kV
Matrica POVEZANOST MV (KB+DV) x kV predstavlja submatricu matrice OPŠTA POVEZANOST MV (KB+DV) x kV i nastaje izbacivanjem određenih redova. Ako postoji skup indeksa
,
važi da
,
čija dimenzija je
,
odnosno
,
gde kardinalnost skupa  odgovara broju MV (KB+DV) x kV.
Ukoliko

Tada

## Status uklopnog stanja
Za svaki osnovni element elektroenergetske opreme, odnosno list unutar EEO koji je potekao od nivoa podele, odnosno grane koja u svom nazivu sadrži oznaku “RO” definiše se status uklopnog stanja koji može biti:
uključen,
isključen.
Ukoliko je status uklopnog stanja osnovnog elementa “uključen”
veza tog elementa sa definisanim prethodnikom,
veza tog elementa sa definisanim sledbenikom,
veza tog elementa koji je prethodnik nekom drugom osnovnom elementu,
veza tog elementa koji je sledbenik nekom drugom osnovnom elementu,
nije prekinuta.
Ukoliko je status uklopnog stanja osnovnog elementa “isključen”
veza tog elementa sa definisanim prethodnikom/prethodnicima,
veza tog elementa sa definisanim sledbenikom/sledbenicima,
veza tog elementa koji je prethodnik nekom drugom osnovnom elementu,
veza tog elementa koji je sledbenik nekom drugom osnovnom elementu,
je prekinuta.
Status uklopnog stanja “uključen” u binarnom obliku je 1.
Status uklopnog stanja “isključen” u binarnom obliku je 0.
Za definisanje statusa uklopnog stanja RO koristimo

gde je:
s - funkcija statusa uklopnog stanja,
rasklopni element - argument funkcije,
s(rasklopni element) - status uklopnog stanja rasklopnog elementa.
### Definisanje statusa uklopnog stanja RO u EEO
SR DVP 400 kV i GSS j:
∀ (i,j): ∃ (SR DVP 400 kV i GSS j) ⇒ ∃ s(SR DVP 400 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_DVP 400 kV, n_GSS 400 kV∈N0;
SR DVP 400 kV i PSS k:
∀ (i,k): ∃ (SR DVP 400 kV i PSS k) ⇒ ∃ s(SR DVP 400 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_DVP 400 kV, n_PSS 400 kV∈N0;
P DVP 400 kV i:
∀ (i): ∃ (P DVP 400 kV i) ⇒ ∃ s(P DVP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
IRSU DVP 400 kV i:
∀ (i): ∃ (IRSU DVP 400 kV i) ⇒ ∃ s(IRSU DVP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., n_DVP 400 kV} ⟺ n_DVP 400 kV>0, i∈{0} ⟺ n_DVP 400 kV=0, 
n_DVP 400 kV∈N0;
SR DVP 220 kV i GSS j:
∀ (i,j): ∃ (SR DVP 220 kV i GSS j) ⇒ ∃ s(SR DVP 220 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_DVP 220 kV, n_GSS 220 kV∈N0;
SR DVP 220 kV i PSS k:
∀ (i,k): ∃ (SR DVP 220 kV i PSS k) ⇒ ∃ s(SR DVP 220 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_DVP 220 kV, n_PSS 220 kV∈N0;
P DVP 220 kV i:
∀ (i): ∃ (P DVP 220 kV i) ⇒ ∃ s(P DVP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
IRSU DVP 220 kV i:
∀ (i): ∃ (IRSU DVP 220 kV i) ⇒ ∃ s(IRSU DVP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., n_DVP 220 kV} ⟺ n_DVP 220 kV>0, i∈{0} ⟺ n_DVP 220 kV=0, 
n_DVP 220 kV∈N0;
SR DVP 110 kV i GSS j:
∀ (i,j): ∃ (SR DVP 110 kV i GSS j) ⇒ ∃ s(SR DVP 110 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_DVP 110 kV, n_GSS 110 kV∈N0;
SR DVP 110 kV i PSS k:
∀ (i,k): ∃ (SR DVP 110 kV i PSS k) ⇒ ∃ s(SR DVP 110 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_DVP 110 kV, n_PSS 110 kV∈N0;
P DVP 110 kV i:
∀ (i): ∃ (P DVP 110 kV i) ⇒ ∃ s(P DVP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
IRSU DVP 110 kV i:
∀ (i): ∃ (IRSU DVP 110 kV i) ⇒ ∃ s(IRSU DVP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., n_DVP 110 kV} ⟺ n_DVP 110 kV>0, i∈{0} ⟺ n_DVP 110 kV=0, 
n_DVP 110 kV∈N0;
SR DVP x kV i GSS j:
∀ (i,j): ∃ (SR DVP x kV i GSS j) ⇒ ∃ s(SR DVP x kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_DVP x kV, n_GSS x kV∈N0;
SR DVP x kV i PSS k:
∀ (i,k): ∃ (SR DVP x kV i PSS k) ⇒ ∃ s(SR DVP x kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_DVP x kV, n_PSS x kV∈N0;
P DVP x kV i:
∀ (i): ∃ (P DVP x kV i) ⇒ ∃ s(P DVP x kV i) ∈ {0,1},
gde: i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
IRSU DVP x kV i:
∀ (i): ∃ (IRSU DVP x kV i) ⇒ ∃ s(IRSU DVP x kV i) ∈ {0,1},
gde: i∈{1, ..., n_DVP x kV} ⟺ n_DVP x kV>0, i∈{0} ⟺ n_DVP x kV=0, 
n_DVP x kV∈N0;
SR KBP 400 kV i GSS j:
∀ (i,j): ∃ (SR KBP 400 kV i GSS j) ⇒ ∃ s(SR KBP 400 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_KBP 400 kV, n_GSS 400 kV∈N0;
SR KBP 400 kV i PSS k:
∀ (i,k): ∃ (SR KBP 400 kV i PSS k) ⇒ ∃ s(SR KBP 400 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_KBP 400 kV, n_PSS 400 kV∈N0;
P KBP 400 kV i:
∀ (i): ∃ (P KBP 400 kV i) ⇒ ∃ s(P KBP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
IRSU KBP 400 kV i:
∀ (i): ∃ (IRSU KBP 400 kV i) ⇒ ∃ s(IRSU KBP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., n_KBP 400 kV} ⟺ n_KBP 400 kV>0, i∈{0} ⟺ n_KBP 400 kV=0, 
n_KBP 400 kV∈N0;
SR KBP 220 kV i GSS j:
∀ (i,j): ∃ (SR KBP 220 kV i GSS j) ⇒ ∃ s(SR KBP 220 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_KBP 220 kV, n_GSS 220 kV∈N0;
SR KBP 220 kV i PSS k:
∀ (i,k): ∃ (SR KBP 220 kV i PSS k) ⇒ ∃ s(SR KBP 220 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_KBP 220 kV, n_PSS 220 kV∈N0;
P KBP 220 kV i:
∀ (i): ∃ (P KBP 220 kV i) ⇒ ∃ s(P KBP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
IRSU KBP 220 kV i:
∀ (i): ∃ (IRSU KBP 220 kV i) ⇒ ∃ s(IRSU KBP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., n_KBP 220 kV} ⟺ n_KBP 220 kV>0, i∈{0} ⟺ n_KBP 220 kV=0, 
n_KBP 220 kV∈N0;
SR KBP 110 kV i GSS j:
∀ (i,j): ∃ (SR KBP 110 kV i GSS j) ⇒ ∃ s(SR KBP 110 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_KBP 110 kV, n_GSS 110 kV∈N0;
SR KBP 110 kV i PSS k:
∀ (i,k): ∃ (SR KBP 110 kV i PSS k) ⇒ ∃ s(SR KBP 110 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_KBP 110 kV, n_PSS 110 kV∈N0;
P KBP 110 kV i:
∀ (i): ∃ (P KBP 110 kV i) ⇒ ∃ s(P KBP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
IRSU KBP 110 kV i:
∀ (i): ∃ (IRSU KBP 110 kV i) ⇒ ∃ s(IRSU KBP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., n_KBP 110 kV} ⟺ n_KBP 110 kV>0, i∈{0} ⟺ n_KBP 110 kV=0, 
n_KBP 110 kV∈N0;
SR KBP x kV i GSS j:
∀ (i,j): ∃ (SR KBP x kV i GSS j) ⇒ ∃ s(SR KBP x kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_KBP x kV, n_GSS x kV∈N0;
SR KBP x kV i PSS k:
∀ (i,k): ∃ (SR KBP x kV i PSS k) ⇒ ∃ s(SR KBP x kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_KBP x kV, n_PSS x kV∈N0;
P KBP x kV i:
∀ (i): ∃ (P KBP x kV i) ⇒ ∃ s(P KBP x kV i) ∈ {0,1},
gde: i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
IRSU KBP x kV i:
∀ (i): ∃ (IRSU KBP x kV i) ⇒ ∃ s(IRSU KBP x kV i) ∈ {0,1},
gde: i∈{1, ..., n_KBP x kV} ⟺ n_KBP x kV>0, i∈{0} ⟺ n_KBP x kV=0, 
n_KBP x kV∈N0;
SR TRPVN TR 400/220 kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPVN TR 400/220 kV/kV i GSS j) ⇒ ∃ s(SR TRPVN TR 400/220 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/220 kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/220 kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPVN TR 400/220 kV/kV i PSS k) ⇒ ∃ s(SR TRPVN TR 400/220 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/220 kV/kV, n_PSS 400 kV∈N0;
IR TRPVN TR 400/220 kV/kV i:
∀ (i): ∃ (IR TRPVN TR 400/220 kV/kV i) ⇒ ∃ s(IR TRPVN TR 400/220 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
P TRPVN TR 400/220 kV/kV i:
∀ (i): ∃ (P TRPVN TR 400/220 kV/kV i) ⇒ ∃ s(P TRPVN TR 400/220 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/220 kV/kV} ⟺ n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/220 kV/kV=0, 
n_TRPVN TR 400/220 kV/kV∈N0;
SR TRPVN TR 400/110 kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPVN TR 400/110 kV/kV i GSS j) ⇒ ∃ s(SR TRPVN TR 400/110 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/110 kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/110 kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPVN TR 400/110 kV/kV i PSS k) ⇒ ∃ s(SR TRPVN TR 400/110 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/110 kV/kV, n_PSS 400 kV∈N0;
IR TRPVN TR 400/110 kV/kV i:
∀ (i): ∃ (IR TRPVN TR 400/110 kV/kV i) ⇒ ∃ s(IR TRPVN TR 400/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
P TRPVN TR 400/110 kV/kV i:
∀ (i): ∃ (P TRPVN TR 400/110 kV/kV i) ⇒ ∃ s(P TRPVN TR 400/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/110 kV/kV} ⟺ n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/110 kV/kV=0, 
n_TRPVN TR 400/110 kV/kV∈N0;
SR TRPVN TR 220/110 kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPVN TR 220/110 kV/kV i GSS j) ⇒ ∃ s(SR TRPVN TR 220/110 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/110 kV/kV, n_GSS 220 kV∈N0;
SR TRPVN TR 220/110 kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPVN TR 220/110 kV/kV i PSS k) ⇒ ∃ s(SR TRPVN TR 220/110 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPVN TR 220/110 kV/kV, n_PSS 220 kV∈N0;
IR TRPVN TR 220/110 kV/kV i:
∀ (i): ∃ (IR TRPVN TR 220/110 kV/kV i) ⇒ ∃ s(IR TRPVN TR 220/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
P TRPVN TR 220/110 kV/kV i:
∀ (i): ∃ (P TRPVN TR 220/110 kV/kV i) ⇒ ∃ s(P TRPVN TR 220/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 220/110 kV/kV} ⟺ n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/110 kV/kV=0, 
n_TRPVN TR 220/110 kV/kV∈N0;
SR TRPVN TR 400/x kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPVN TR 400/x kV/kV i GSS j) ⇒ ∃ s(SR TRPVN TR 400/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_TRPVN TR 400/x kV/kV, n_GSS 400 kV∈N0;
SR TRPVN TR 400/x kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPVN TR 400/x kV/kV i PSS k) ⇒ ∃ s(SR TRPVN TR 400/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, k∈{1, ..., n_PSS 400 kV} ⟺ n_PSS 400 kV>0, k∈{0} ⟺ n_PSS 400 kV=0, 
n_TRPVN TR 400/x kV/kV, n_PSS 400 kV∈N0;
IR TRPVN TR 400/x kV/kV i:
∀ (i): ∃ (IR TRPVN TR 400/x kV/kV i) ⇒ ∃ s(IR TRPVN TR 400/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
P TRPVN TR 400/x kV/kV i:
∀ (i): ∃ (P TRPVN TR 400/x kV/kV i) ⇒ ∃ s(P TRPVN TR 400/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 400/x kV/kV} ⟺ n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 400/x kV/kV=0, 
n_TRPVN TR 400/x kV/kV∈N0;
SR TRPVN TR 220/x kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPVN TR 220/x kV/kV i GSS j) ⇒ ∃ s(SR TRPVN TR 220/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPVN TR 220/x kV/kV, n_GSS 220 kV∈N0;
SR TRPVN TR 220/x kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPVN TR 220/x kV/kV i PSS k) ⇒ ∃ s(SR TRPVN TR 220/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPVN TR 220/x kV/kV, n_PSS 220 kV∈N0;
IR TRPVN TR 220/x kV/kV i:
∀ (i): ∃ (IR TRPVN TR 220/x kV/kV i) ⇒ ∃ s(IR TRPVN TR 220/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
P TRPVN TR 220/x kV/kV i:
∀ (i): ∃ (P TRPVN TR 220/x kV/kV i) ⇒ ∃ s(P TRPVN TR 220/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 220/x kV/kV} ⟺ n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 220/x kV/kV=0, 
n_TRPVN TR 220/x kV/kV∈N0;
SR TRPVN TR 110/x kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPVN TR 110/x kV/kV i GSS j) ⇒ ∃ s(SR TRPVN TR 110/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPVN TR 110/x kV/kV, n_GSS 110 kV∈N0;
SR TRPVN TR 110/x kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPVN TR 110/x kV/kV i PSS k) ⇒ ∃ s(SR TRPVN TR 110/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPVN TR 110/x kV/kV, n_PSS 110 kV∈N0;
IR TRPVN TR 110/x kV/kV i:
∀ (i): ∃ (IR TRPVN TR 110/x kV/kV i) ⇒ ∃ s(IR TRPVN TR 110/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
P TRPVN TR 110/x kV/kV i:
∀ (i): ∃ (P TRPVN TR 110/x kV/kV i) ⇒ ∃ s(P TRPVN TR 110/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPVN TR 110/x kV/kV} ⟺ n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPVN TR 110/x kV/kV=0, 
n_TRPVN TR 110/x kV/kV∈N0;
SR TRPNN TR 400/220 kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPNN TR 400/220 kV/kV i GSS j) ⇒ ∃ s(SR TRPNN TR 400/220 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_GSS 220 kV∈N0;
SR TRPNN TR 400/220 kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPNN TR 400/220 kV/kV i PSS k) ⇒ ∃ s(SR TRPNN TR 400/220 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, k∈{1, ..., n_PSS 220 kV} ⟺ n_PSS 220 kV>0, k∈{0} ⟺ n_PSS 220 kV=0, 
n_TRPNN TR 400/220 kV/kV, n_PSS 220 kV∈N0;
IR TRPNN TR 400/220 kV/kV i:
∀ (i): ∃ (IR TRPNN TR 400/220 kV/kV i) ⇒ ∃ s(IR TRPNN TR 400/220 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
P TRPNN TR 400/220 kV/kV i:
∀ (i): ∃ (P TRPNN TR 400/220 kV/kV i) ⇒ ∃ s(P TRPNN TR 400/220 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/220 kV/kV} ⟺ n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/220 kV/kV=0, 
n_TRPNN TR 400/220 kV/kV∈N0;
SR TRPNN TR 400/110 kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPNN TR 400/110 kV/kV i GSS j) ⇒ ∃ s(SR TRPNN TR 400/110 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_GSS 110 kV∈N0;
SR TRPNN TR 400/110 kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPNN TR 400/110 kV/kV i PSS k) ⇒ ∃ s(SR TRPNN TR 400/110 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPNN TR 400/110 kV/kV, n_PSS 110 kV∈N0;
IR TRPNN TR 400/110 kV/kV i:
∀ (i): ∃ (IR TRPNN TR 400/110 kV/kV i) ⇒ ∃ s(IR TRPNN TR 400/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
P TRPNN TR 400/110 kV/kV i:
∀ (i): ∃ (P TRPNN TR 400/110 kV/kV i) ⇒ ∃ s(P TRPNN TR 400/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/110 kV/kV} ⟺ n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/110 kV/kV=0, 
n_TRPNN TR 400/110 kV/kV∈N0;
SR TRPNN TR 220/110 kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPNN TR 220/110 kV/kV i GSS j) ⇒ ∃ s(SR TRPNN TR 220/110 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_GSS 110 kV∈N0;
SR TRPNN TR 220/110 kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPNN TR 220/110 kV/kV i PSS k) ⇒ ∃ s(SR TRPNN TR 220/110 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, k∈{1, ..., n_PSS 110 kV} ⟺ n_PSS 110 kV>0, k∈{0} ⟺ n_PSS 110 kV=0, 
n_TRPNN TR 220/110 kV/kV, n_PSS 110 kV∈N0;
IR TRPNN TR 220/110 kV/kV i:
∀ (i): ∃ (IR TRPNN TR 220/110 kV/kV i) ⇒ ∃ s(IR TRPNN TR 220/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
P TRPNN TR 220/110 kV/kV i:
∀ (i): ∃ (P TRPNN TR 220/110 kV/kV i) ⇒ ∃ s(P TRPNN TR 220/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 220/110 kV/kV} ⟺ n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/110 kV/kV=0, 
n_TRPNN TR 220/110 kV/kV∈N0;
SR TRPNN TR 400/x kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPNN TR 400/x kV/kV i GSS j) ⇒ ∃ s(SR TRPNN TR 400/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 400/x kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPNN TR 400/x kV/kV i PSS k) ⇒ ∃ s(SR TRPNN TR 400/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 400/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 400/x kV/kV i:
∀ (i): ∃ (IR TRPNN TR 400/x kV/kV i) ⇒ ∃ s(IR TRPNN TR 400/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
P TRPNN TR 400/x kV/kV i:
∀ (i): ∃ (P TRPNN TR 400/x kV/kV i) ⇒ ∃ s(P TRPNN TR 400/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 400/x kV/kV} ⟺ n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 400/x kV/kV=0, 
n_TRPNN TR 400/x kV/kV∈N0;
SR TRPNN TR 220/x kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPNN TR 220/x kV/kV i GSS j) ⇒ ∃ s(SR TRPNN TR 220/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 220/x kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPNN TR 220/x kV/kV i PSS k) ⇒ ∃ s(SR TRPNN TR 220/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 220/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 220/x kV/kV i:
∀ (i): ∃ (IR TRPNN TR 220/x kV/kV i) ⇒ ∃ s(IR TRPNN TR 220/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
P TRPNN TR 220/x kV/kV i:
∀ (i): ∃ (P TRPNN TR 220/x kV/kV i) ⇒ ∃ s(P TRPNN TR 220/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 220/x kV/kV} ⟺ n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 220/x kV/kV=0, 
n_TRPNN TR 220/x kV/kV∈N0;
SR TRPNN TR 110/x kV/kV i GSS j:
∀ (i,j): ∃ (SR TRPNN TR 110/x kV/kV i GSS j) ⇒ ∃ s(SR TRPNN TR 110/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_GSS x kV∈N0;
SR TRPNN TR 110/x kV/kV i PSS k:
∀ (i,k): ∃ (SR TRPNN TR 110/x kV/kV i PSS k) ⇒ ∃ s(SR TRPNN TR 110/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, k∈{1, ..., n_PSS x kV} ⟺ n_PSS x kV>0, k∈{0} ⟺ n_PSS x kV=0, 
n_TRPNN TR 110/x kV/kV, n_PSS x kV∈N0;
IR TRPNN TR 110/x kV/kV i:
∀ (i): ∃ (IR TRPNN TR 110/x kV/kV i) ⇒ ∃ s(IR TRPNN TR 110/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
P TRPNN TR 110/x kV/kV i:
∀ (i): ∃ (P TRPNN TR 110/x kV/kV i) ⇒ ∃ s(P TRPNN TR 110/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., n_TRPNN TR 110/x kV/kV} ⟺ n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ n_TRPNN TR 110/x kV/kV=0, 
n_TRPNN TR 110/x kV/kV∈N0;
SR GSP 400 kV i GSS j:
∀ (i,j): ∃ (SR GSP 400 kV i GSS j) ⇒ ∃ s(SR GSP 400 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, i∈{0} ⟺ n_GSP 400 kV=0, j∈{i,i+1} ⟺ n_GSP 400 kV>0, j∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
P GSP 400 kV i:
∀ (i): ∃ (P GSP 400 kV i) ⇒ ∃ s(P GSP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., n_GSP 400 kV} ⟺ n_GSP 400 kV>0, i∈{0} ⟺ n_GSP 400 kV=0, 
n_GSP 400 kV∈N0;
SR GSP 220 kV i GSS j:
∀ (i,j): ∃ (SR GSP 220 kV i GSS j) ⇒ ∃ s(SR GSP 220 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, i∈{0} ⟺ n_GSP 220 kV=0, j∈{i,i+1} ⟺ n_GSP 220 kV>0, j∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
P GSP 220 kV i:
∀ (i): ∃ (P GSP 220 kV i) ⇒ ∃ s(P GSP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., n_GSP 220 kV} ⟺ n_GSP 220 kV>0, i∈{0} ⟺ n_GSP 220 kV=0, 
n_GSP 220 kV∈N0;
SR GSP 110 kV i GSS j:
∀ (i,j): ∃ (SR GSP 110 kV i GSS j) ⇒ ∃ s(SR GSP 110 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, i∈{0} ⟺ n_GSP 110 kV=0, j∈{i,i+1} ⟺ n_GSP 110 kV>0, j∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
P GSP 110 kV i:
∀ (i): ∃ (P GSP 110 kV i) ⇒ ∃ s(P GSP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., n_GSP 110 kV} ⟺ n_GSP 110 kV>0, i∈{0} ⟺ n_GSP 110 kV=0, 
n_GSP 110 kV∈N0;
SR GSP x kV i GSS j:
∀ (i,j): ∃ (SR GSP x kV i GSS j) ⇒ ∃ s(SR GSP x kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, i∈{0} ⟺ n_GSP x kV=0, j∈{i,i+1} ⟺ n_GSP x kV>0, j∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
P GSP x kV i:
∀ (i): ∃ (P GSP x kV i) ⇒ ∃ s(P GSP x kV i) ∈ {0,1},
gde: i∈{1, ..., n_GSP x kV} ⟺ n_GSP x kV>0, i∈{0} ⟺ n_GSP x kV=0, 
n_GSP x kV∈N0;
SR PSP 400 kV i GSS j:
∀ (i,j): ∃ (SR PSP 400 kV i GSS j) ⇒ ∃ s(SR PSP 400 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, i∈{0} ⟺ n_PSP 400 kV=0, j∈{1, ..., n_GSS 400 kV} ⟺ n_GSS 400 kV>0, j∈{0} ⟺ n_GSS 400 kV=0, 
n_PSP 400 kV, n_GSS 400 kV∈N0;
SR PSP 400 kV i PSS i:
∀ (i): ∃ (SR PSP 400 kV i PSS i) ⇒ ∃ s(SR PSP 400 kV i PSS i) ∈ {0,1},
gde: i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, i∈{0} ⟺ n_PSP 400 kV=0, 
n_PSP 400 kV∈N0;
P PSP 400 kV i:
∀ (i): ∃ (P PSP 400 kV i) ⇒ ∃ s(P PSP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., n_PSP 400 kV} ⟺ n_PSP 400 kV>0, i∈{0} ⟺ n_PSP 400 kV=0, 
n_PSP 400 kV∈N0;
SR PSP 220 kV i GSS j:
∀ (i,j): ∃ (SR PSP 220 kV i GSS j) ⇒ ∃ s(SR PSP 220 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, i∈{0} ⟺ n_PSP 220 kV=0, j∈{1, ..., n_GSS 220 kV} ⟺ n_GSS 220 kV>0, j∈{0} ⟺ n_GSS 220 kV=0, 
n_PSP 220 kV, n_GSS 220 kV∈N0;
SR PSP 220 kV i PSS i:
∀ (i): ∃ (SR PSP 220 kV i PSS i) ⇒ ∃ s(SR PSP 220 kV i PSS i) ∈ {0,1},
gde: i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, i∈{0} ⟺ n_PSP 220 kV=0, 
n_PSP 220 kV∈N0;
P PSP 220 kV i:
∀ (i): ∃ (P PSP 220 kV i) ⇒ ∃ s(P PSP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., n_PSP 220 kV} ⟺ n_PSP 220 kV>0, i∈{0} ⟺ n_PSP 220 kV=0, 
n_PSP 220 kV∈N0;
SR PSP 110 kV i GSS j:
∀ (i,j): ∃ (SR PSP 110 kV i GSS j) ⇒ ∃ s(SR PSP 110 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, i∈{0} ⟺ n_PSP 110 kV=0, j∈{1, ..., n_GSS 110 kV} ⟺ n_GSS 110 kV>0, j∈{0} ⟺ n_GSS 110 kV=0, 
n_PSP 110 kV, n_GSS 110 kV∈N0;
PSP 110 kV i PSS i:
∀ (i): ∃ (PSP 110 kV i PSS i) ⇒ ∃ s(PSP 110 kV i PSS i) ∈ {0,1},
gde: i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, i∈{0} ⟺ n_PSP 110 kV=0, 
n_PSP 110 kV∈N0;
P PSP 110 kV i:
∀ (i): ∃ (P PSP 110 kV i) ⇒ ∃ s(P PSP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., n_PSP 110 kV} ⟺ n_PSP 110 kV>0, i∈{0} ⟺ n_PSP 110 kV=0, 
n_PSP 110 kV∈N0;
SR PSP x kV i GSS j:
∀ (i,j): ∃ (SR PSP x kV i GSS j) ⇒ ∃ s(SR PSP x kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, i∈{0} ⟺ n_PSP x kV=0, j∈{1, ..., n_GSS x kV} ⟺ n_GSS x kV>0, j∈{0} ⟺ n_GSS x kV=0, 
n_PSP x kV, n_GSS x kV∈N0;
PSP x kV i PSS i:
∀ (i): ∃ (PSP x kV i PSS i) ⇒ ∃ s(PSP x kV i PSS i) ∈ {0,1},
gde: i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, i∈{0} ⟺ n_PSP x kV=0, 
n_PSP x kV∈N0;
P PSP x kV i:
∀ (i): ∃ (P PSP x kV i) ⇒ ∃ s(P PSP x kV i) ∈ {0,1},
gde: i∈{1, ..., n_PSP x kV} ⟺ n_PSP x kV>0, i∈{0} ⟺ n_PSP x kV=0, 
n_PSP x kV∈N0;
Definisanje statusa uklopnog stanja RO za x-ti EEO
EEO x SR DVP 400 kV i GSS j:
∀ (i,j): ∃ (EEO x SR DVP 400 kV i GSS j) ⇒ ∃ s(EEO x SR DVP 400 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x SR DVP 400 kV i PSS k:
∀ (i,k): ∃ (EEO x SR DVP 400 kV i PSS k) ⇒ ∃ s(EEO x SR DVP 400 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_DVP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x P DVP 400 kV i:
∀ (i): ∃ (EEO x P DVP 400 kV i) ⇒ ∃ s(EEO x P DVP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x IRSU DVP 400 kV i:
∀ (i): ∃ (EEO x IRSU DVP 400 kV i) ⇒ ∃ s(EEO x IRSU DVP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 400 kV} ⟺ EEO x n_DVP 400 kV>0, i∈{0} ⟺ EEO x n_DVP 400 kV=0, 
EEO x n_DVP 400 kV∈N0;
EEO x SR DVP 220 kV i GSS j:
∀ (i,j): ∃ (EEO x SR DVP 220 kV i GSS j) ⇒ ∃ s(EEO x SR DVP 220 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x SR DVP 220 kV i PSS k:
∀ (i,k): ∃ (EEO x SR DVP 220 kV i PSS k) ⇒ ∃ s(EEO x SR DVP 220 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_DVP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x P DVP 220 kV i:
∀ (i): ∃ (EEO x P DVP 220 kV i) ⇒ ∃ s(EEO x P DVP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x IRSU DVP 220 kV i:
∀ (i): ∃ (EEO x IRSU DVP 220 kV i) ⇒ ∃ s(EEO x IRSU DVP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 220 kV} ⟺ EEO x n_DVP 220 kV>0, i∈{0} ⟺ EEO x n_DVP 220 kV=0, 
EEO x n_DVP 220 kV∈N0;
EEO x SR DVP 110 kV i GSS j:
∀ (i,j): ∃ (EEO x SR DVP 110 kV i GSS j) ⇒ ∃ s(EEO x SR DVP 110 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x SR DVP 110 kV i PSS k:
∀ (i,k): ∃ (EEO x SR DVP 110 kV i PSS k) ⇒ ∃ s(EEO x SR DVP 110 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_DVP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x P DVP 110 kV i:
∀ (i): ∃ (EEO x P DVP 110 kV i) ⇒ ∃ s(EEO x P DVP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x IRSU DVP 110 kV i:
∀ (i): ∃ (EEO x IRSU DVP 110 kV i) ⇒ ∃ s(EEO x IRSU DVP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP 110 kV} ⟺ EEO x n_DVP 110 kV>0, i∈{0} ⟺ EEO x n_DVP 110 kV=0, 
EEO x n_DVP 110 kV∈N0;
EEO x SR DVP x kV i GSS j:
∀ (i,j): ∃ (EEO x SR DVP x kV i GSS j) ⇒ ∃ s(EEO x SR DVP x kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_DVP x kV, EEO x n_GSS x kV∈N0;
EEO x SR DVP x kV i PSS k:
∀ (i,k): ∃ (EEO x SR DVP x kV i PSS k) ⇒ ∃ s(EEO x SR DVP x kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_DVP x kV, EEO x n_PSS x kV∈N0;
EEO x P DVP x kV i:
∀ (i): ∃ (EEO x P DVP x kV i) ⇒ ∃ s(EEO x P DVP x kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x IRSU DVP x kV i:
∀ (i): ∃ (EEO x IRSU DVP x kV i) ⇒ ∃ s(EEO x IRSU DVP x kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_DVP x kV} ⟺ EEO x n_DVP x kV>0, i∈{0} ⟺ EEO x n_DVP x kV=0, 
EEO x n_DVP x kV∈N0;
EEO x SR KBP 400 kV i GSS j:
∀ (i,j): ∃ (EEO x SR KBP 400 kV i GSS j) ⇒ ∃ s(EEO x SR KBP 400 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_GSS 400 kV∈N0;
EEO x SR KBP 400 kV i PSS k:
∀ (i,k): ∃ (EEO x SR KBP 400 kV i PSS k) ⇒ ∃ s(EEO x SR KBP 400 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_KBP 400 kV, EEO x n_PSS 400 kV∈N0;
EEO x P KBP 400 kV i:
∀ (i): ∃ (EEO x P KBP 400 kV i) ⇒ ∃ s(EEO x P KBP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x IRSU KBP 400 kV i:
∀ (i): ∃ (EEO x IRSU KBP 400 kV i) ⇒ ∃ s(EEO x IRSU KBP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 400 kV} ⟺ EEO x n_KBP 400 kV>0, i∈{0} ⟺ EEO x n_KBP 400 kV=0, 
EEO x n_KBP 400 kV∈N0;
EEO x SR KBP 220 kV i GSS j:
∀ (i,j): ∃ (EEO x SR KBP 220 kV i GSS j) ⇒ ∃ s(EEO x SR KBP 220 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_GSS 220 kV∈N0;
EEO x SR KBP 220 kV i PSS k:
∀ (i,k): ∃ (EEO x SR KBP 220 kV i PSS k) ⇒ ∃ s(EEO x SR KBP 220 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_KBP 220 kV, EEO x n_PSS 220 kV∈N0;
EEO x P KBP 220 kV i:
∀ (i): ∃ (EEO x P KBP 220 kV i) ⇒ ∃ s(EEO x P KBP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x IRSU KBP 220 kV i:
∀ (i): ∃ (EEO x IRSU KBP 220 kV i) ⇒ ∃ s(EEO x IRSU KBP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 220 kV} ⟺ EEO x n_KBP 220 kV>0, i∈{0} ⟺ EEO x n_KBP 220 kV=0, 
EEO x n_KBP 220 kV∈N0;
EEO x SR KBP 110 kV i GSS j:
∀ (i,j): ∃ (EEO x SR KBP 110 kV i GSS j) ⇒ ∃ s(EEO x SR KBP 110 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_GSS 110 kV∈N0;
EEO x SR KBP 110 kV i PSS k:
∀ (i,k): ∃ (EEO x SR KBP 110 kV i PSS k) ⇒ ∃ s(EEO x SR KBP 110 kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_KBP 110 kV, EEO x n_PSS 110 kV∈N0;
EEO x P KBP 110 kV i:
∀ (i): ∃ (EEO x P KBP 110 kV i) ⇒ ∃ s(EEO x P KBP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x IRSU KBP 110 kV i:
∀ (i): ∃ (EEO x IRSU KBP 110 kV i) ⇒ ∃ s(EEO x IRSU KBP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP 110 kV} ⟺ EEO x n_KBP 110 kV>0, i∈{0} ⟺ EEO x n_KBP 110 kV=0, 
EEO x n_KBP 110 kV∈N0;
EEO x SR KBP x kV i GSS j:
∀ (i,j): ∃ (EEO x SR KBP x kV i GSS j) ⇒ ∃ s(EEO x SR KBP x kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_KBP x kV, EEO x n_GSS x kV∈N0;
EEO x SR KBP x kV i PSS k:
∀ (i,k): ∃ (EEO x SR KBP x kV i PSS k) ⇒ ∃ s(EEO x SR KBP x kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_KBP x kV, EEO x n_PSS x kV∈N0;
EEO x P KBP x kV i:
∀ (i): ∃ (EEO x P KBP x kV i) ⇒ ∃ s(EEO x P KBP x kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x IRSU KBP x kV i:
∀ (i): ∃ (EEO x IRSU KBP x kV i) ⇒ ∃ s(EEO x IRSU KBP x kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_KBP x kV} ⟺ EEO x n_KBP x kV>0, i∈{0} ⟺ EEO x n_KBP x kV=0, 
EEO x n_KBP x kV∈N0;
EEO x SR TRPVN TR 400/220 kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPVN TR 400/220 kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPVN TR 400/220 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SR TRPVN TR 400/220 kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPVN TR 400/220 kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPVN TR 400/220 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x IR TRPVN TR 400/220 kV/kV i:
∀ (i): ∃ (EEO x IR TRPVN TR 400/220 kV/kV i) ⇒ ∃ s(EEO x IR TRPVN TR 400/220 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x P TRPVN TR 400/220 kV/kV i:
∀ (i): ∃ (EEO x P TRPVN TR 400/220 kV/kV i) ⇒ ∃ s(EEO x P TRPVN TR 400/220 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/220 kV/kV} ⟺ EEO x n_TRPVN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/220 kV/kV=0, 
EEO x n_TRPVN TR 400/220 kV/kV∈N0;
EEO x SR TRPVN TR 400/110 kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPVN TR 400/110 kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPVN TR 400/110 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SR TRPVN TR 400/110 kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPVN TR 400/110 kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPVN TR 400/110 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x IR TRPVN TR 400/110 kV/kV i:
∀ (i): ∃ (EEO x IR TRPVN TR 400/110 kV/kV i) ⇒ ∃ s(EEO x IR TRPVN TR 400/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x P TRPVN TR 400/110 kV/kV i:
∀ (i): ∃ (EEO x P TRPVN TR 400/110 kV/kV i) ⇒ ∃ s(EEO x P TRPVN TR 400/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/110 kV/kV} ⟺ EEO x n_TRPVN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/110 kV/kV=0, 
EEO x n_TRPVN TR 400/110 kV/kV∈N0;
EEO x SR TRPVN TR 220/110 kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPVN TR 220/110 kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPVN TR 220/110 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SR TRPVN TR 220/110 kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPVN TR 220/110 kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPVN TR 220/110 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x IR TRPVN TR 220/110 kV/kV i:
∀ (i): ∃ (EEO x IR TRPVN TR 220/110 kV/kV i) ⇒ ∃ s(EEO x IR TRPVN TR 220/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x P TRPVN TR 220/110 kV/kV i:
∀ (i): ∃ (EEO x P TRPVN TR 220/110 kV/kV i) ⇒ ∃ s(EEO x P TRPVN TR 220/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 220/110 kV/kV} ⟺ EEO x n_TRPVN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/110 kV/kV=0, 
EEO x n_TRPVN TR 220/110 kV/kV∈N0;
EEO x SR TRPVN TR 400/x kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPVN TR 400/x kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPVN TR 400/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, 
EEO x n_TRPVN TR 400/x kV/kV, EEO x n_GSS 400 kV∈N0;
EEO x SR TRPVN TR 400/x kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPVN TR 400/x kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPVN TR 400/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, k∈{1, ..., EEO x n_PSS 400 kV} ⟺ EEO x n_PSS 400 kV>0, k∈{0} ⟺ EEO x n_PSS 400 kV=0, 
EEO x n_TRPVN TR 400/x kV/kV, EEO x n_PSS 400 kV∈N0;
EEO x IR TRPVN TR 400/x kV/kV i:
∀ (i): ∃ (EEO x IR TRPVN TR 400/x kV/kV i) ⇒ ∃ s(EEO x IR TRPVN TR 400/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x P TRPVN TR 400/x kV/kV i:
∀ (i): ∃ (EEO x P TRPVN TR 400/x kV/kV i) ⇒ ∃ s(EEO x P TRPVN TR 400/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 400/x kV/kV} ⟺ EEO x n_TRPVN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 400/x kV/kV=0, 
EEO x n_TRPVN TR 400/x kV/kV∈N0;
EEO x SR TRPVN TR 220/x kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPVN TR 220/x kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPVN TR 220/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPVN TR 220/x kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SR TRPVN TR 220/x kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPVN TR 220/x kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPVN TR 220/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPVN TR 220/x kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x IR TRPVN TR 220/x kV/kV i:
∀ (i): ∃ (EEO x IR TRPVN TR 220/x kV/kV i) ⇒ ∃ s(EEO x IR TRPVN TR 220/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x P TRPVN TR 220/x kV/kV i:
∀ (i): ∃ (EEO x P TRPVN TR 220/x kV/kV i) ⇒ ∃ s(EEO x P TRPVN TR 220/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 220/x kV/kV} ⟺ EEO x n_TRPVN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 220/x kV/kV=0, 
EEO x n_TRPVN TR 220/x kV/kV∈N0;
EEO x SR TRPVN TR 110/x kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPVN TR 110/x kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPVN TR 110/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPVN TR 110/x kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SR TRPVN TR 110/x kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPVN TR 110/x kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPVN TR 110/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPVN TR 110/x kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x IR TRPVN TR 110/x kV/kV i:
∀ (i): ∃ (EEO x IR TRPVN TR 110/x kV/kV i) ⇒ ∃ s(EEO x IR TRPVN TR 110/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x P TRPVN TR 110/x kV/kV i:
∀ (i): ∃ (EEO x P TRPVN TR 110/x kV/kV i) ⇒ ∃ s(EEO x P TRPVN TR 110/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPVN TR 110/x kV/kV} ⟺ EEO x n_TRPVN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPVN TR 110/x kV/kV=0, 
EEO x n_TRPVN TR 110/x kV/kV∈N0;
EEO x SR TRPNN TR 400/220 kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPNN TR 400/220 kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPNN TR 400/220 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_GSS 220 kV∈N0;
EEO x SR TRPNN TR 400/220 kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPNN TR 400/220 kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPNN TR 400/220 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, k∈{1, ..., EEO x n_PSS 220 kV} ⟺ EEO x n_PSS 220 kV>0, k∈{0} ⟺ EEO x n_PSS 220 kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV, EEO x n_PSS 220 kV∈N0;
EEO x IR TRPNN TR 400/220 kV/kV i:
∀ (i): ∃ (EEO x IR TRPNN TR 400/220 kV/kV i) ⇒ ∃ s(EEO x IR TRPNN TR 400/220 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x P TRPNN TR 400/220 kV/kV i:
∀ (i): ∃ (EEO x P TRPNN TR 400/220 kV/kV i) ⇒ ∃ s(EEO x P TRPNN TR 400/220 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/220 kV/kV} ⟺ EEO x n_TRPNN TR 400/220 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/220 kV/kV=0, 
EEO x n_TRPNN TR 400/220 kV/kV∈N0;
EEO x SR TRPNN TR 400/110 kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPNN TR 400/110 kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPNN TR 400/110 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SR TRPNN TR 400/110 kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPNN TR 400/110 kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPNN TR 400/110 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x IR TRPNN TR 400/110 kV/kV i:
∀ (i): ∃ (EEO x IR TRPNN TR 400/110 kV/kV i) ⇒ ∃ s(EEO x IR TRPNN TR 400/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x P TRPNN TR 400/110 kV/kV i:
∀ (i): ∃ (EEO x P TRPNN TR 400/110 kV/kV i) ⇒ ∃ s(EEO x P TRPNN TR 400/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/110 kV/kV} ⟺ EEO x n_TRPNN TR 400/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/110 kV/kV=0, 
EEO x n_TRPNN TR 400/110 kV/kV∈N0;
EEO x SR TRPNN TR 220/110 kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPNN TR 220/110 kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPNN TR 220/110 kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_GSS 110 kV∈N0;
EEO x SR TRPNN TR 220/110 kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPNN TR 220/110 kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPNN TR 220/110 kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, k∈{1, ..., EEO x n_PSS 110 kV} ⟺ EEO x n_PSS 110 kV>0, k∈{0} ⟺ EEO x n_PSS 110 kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV, EEO x n_PSS 110 kV∈N0;
EEO x IR TRPNN TR 220/110 kV/kV i:
∀ (i): ∃ (EEO x IR TRPNN TR 220/110 kV/kV i) ⇒ ∃ s(EEO x IR TRPNN TR 220/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x P TRPNN TR 220/110 kV/kV i:
∀ (i): ∃ (EEO x P TRPNN TR 220/110 kV/kV i) ⇒ ∃ s(EEO x P TRPNN TR 220/110 kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 220/110 kV/kV} ⟺ EEO x n_TRPNN TR 220/110 kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/110 kV/kV=0, 
EEO x n_TRPNN TR 220/110 kV/kV∈N0;
EEO x SR TRPNN TR 400/x kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPNN TR 400/x kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPNN TR 400/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SR TRPNN TR 400/x kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPNN TR 400/x kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPNN TR 400/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 400/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 400/x kV/kV i:
∀ (i): ∃ (EEO x IR TRPNN TR 400/x kV/kV i) ⇒ ∃ s(EEO x IR TRPNN TR 400/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x P TRPNN TR 400/x kV/kV i:
∀ (i): ∃ (EEO x P TRPNN TR 400/x kV/kV i) ⇒ ∃ s(EEO x P TRPNN TR 400/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 400/x kV/kV} ⟺ EEO x n_TRPNN TR 400/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 400/x kV/kV=0, 
EEO x n_TRPNN TR 400/x kV/kV∈N0;
EEO x SR TRPNN TR 220/x kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPNN TR 220/x kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPNN TR 220/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SR TRPNN TR 220/x kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPNN TR 220/x kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPNN TR 220/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 220/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 220/x kV/kV i:
∀ (i): ∃ (EEO x IR TRPNN TR 220/x kV/kV i) ⇒ ∃ s(EEO x IR TRPNN TR 220/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x P TRPNN TR 220/x kV/kV i:
∀ (i): ∃ (EEO x P TRPNN TR 220/x kV/kV i) ⇒ ∃ s(EEO x P TRPNN TR 220/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 220/x kV/kV} ⟺ EEO x n_TRPNN TR 220/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 220/x kV/kV=0, 
EEO x n_TRPNN TR 220/x kV/kV∈N0;
EEO x SR TRPNN TR 110/x kV/kV i GSS j:
∀ (i,j): ∃ (EEO x SR TRPNN TR 110/x kV/kV i GSS j) ⇒ ∃ s(EEO x SR TRPNN TR 110/x kV/kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_GSS x kV∈N0;
EEO x SR TRPNN TR 110/x kV/kV i PSS k:
∀ (i,k): ∃ (EEO x SR TRPNN TR 110/x kV/kV i PSS k) ⇒ ∃ s(EEO x SR TRPNN TR 110/x kV/kV i PSS k) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, k∈{1, ..., EEO x n_PSS x kV} ⟺ EEO x n_PSS x kV>0, k∈{0} ⟺ EEO x n_PSS x kV=0, 
EEO x n_TRPNN TR 110/x kV/kV, EEO x n_PSS x kV∈N0;
EEO x IR TRPNN TR 110/x kV/kV i:
∀ (i): ∃ (EEO x IR TRPNN TR 110/x kV/kV i) ⇒ ∃ s(EEO x IR TRPNN TR 110/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x P TRPNN TR 110/x kV/kV i:
∀ (i): ∃ (EEO x P TRPNN TR 110/x kV/kV i) ⇒ ∃ s(EEO x P TRPNN TR 110/x kV/kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_TRPNN TR 110/x kV/kV} ⟺ EEO x n_TRPNN TR 110/x kV/kV>0, i∈{0} ⟺ EEO x n_TRPNN TR 110/x kV/kV=0, 
EEO x n_TRPNN TR 110/x kV/kV∈N0;
EEO x SR GSP 400 kV i GSS j:
∀ (i,j): ∃ (EEO x SR GSP 400 kV i GSS j) ⇒ ∃ s(EEO x SR GSP 400 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, i∈{0} ⟺ EEO x n_GSP 400 kV=0, j∈{i,i+1} ⟺ EEO x n_GSP 400 kV>0, j∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x P GSP 400 kV i:
∀ (i): ∃ (EEO x P GSP 400 kV i) ⇒ ∃ s(EEO x P GSP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_GSP 400 kV} ⟺ EEO x n_GSP 400 kV>0, i∈{0} ⟺ EEO x n_GSP 400 kV=0, 
EEO x n_GSP 400 kV∈N0;
EEO x SR GSP 220 kV i GSS j:
∀ (i,j): ∃ (EEO x SR GSP 220 kV i GSS j) ⇒ ∃ s(EEO x SR GSP 220 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, i∈{0} ⟺ EEO x n_GSP 220 kV=0, j∈{i,i+1} ⟺ EEO x n_GSP 220 kV>0, j∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x P GSP 220 kV i:
∀ (i): ∃ (EEO x P GSP 220 kV i) ⇒ ∃ s(EEO x P GSP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_GSP 220 kV} ⟺ EEO x n_GSP 220 kV>0, i∈{0} ⟺ EEO x n_GSP 220 kV=0, 
EEO x n_GSP 220 kV∈N0;
EEO x SR GSP 110 kV i GSS j:
∀ (i,j): ∃ (EEO x SR GSP 110 kV i GSS j) ⇒ ∃ s(EEO x SR GSP 110 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, i∈{0} ⟺ EEO x n_GSP 110 kV=0, j∈{i,i+1} ⟺ EEO x n_GSP 110 kV>0, j∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x P GSP 110 kV i:
∀ (i): ∃ (EEO x P GSP 110 kV i) ⇒ ∃ s(EEO x P GSP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_GSP 110 kV} ⟺ EEO x n_GSP 110 kV>0, i∈{0} ⟺ EEO x n_GSP 110 kV=0, 
EEO x n_GSP 110 kV∈N0;
EEO x SR GSP x kV i GSS j:
∀ (i,j): ∃ (EEO x SR GSP x kV i GSS j) ⇒ ∃ s(EEO x SR GSP x kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, i∈{0} ⟺ EEO x n_GSP x kV=0, j∈{i,i+1} ⟺ EEO x n_GSP x kV>0, j∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x P GSP x kV i:
∀ (i): ∃ (EEO x P GSP x kV i) ⇒ ∃ s(EEO x P GSP x kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_GSP x kV} ⟺ EEO x n_GSP x kV>0, i∈{0} ⟺ EEO x n_GSP x kV=0, 
EEO x n_GSP x kV∈N0;
EEO x SR PSP 400 kV i GSS j:
∀ (i,j): ∃ (EEO x SR PSP 400 kV i GSS j) ⇒ ∃ s(EEO x SR PSP 400 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, i∈{0} ⟺ EEO x n_PSP 400 kV=0, j∈{1, ..., EEO x n_GSS 400 kV} ⟺ EEO x n_GSS 400 kV>0, j∈{0} ⟺ EEO x n_GSS 400 kV=0, EEO x n_PSP 400 kV, 
EEO x n_GSS 400 kV∈N0;
EEO x SR PSP 400 kV i PSS i:
∀ (i): ∃ (EEO x SR PSP 400 kV i PSS i) ⇒ ∃ s(EEO x SR PSP 400 kV i PSS i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, i∈{0} ⟺ EEO x n_PSP 400 kV=0, 
EEO x n_PSP 400 kV∈N0;
EEO x P PSP 400 kV i:
∀ (i): ∃ (EEO x P PSP 400 kV i) ⇒ ∃ s(EEO x P PSP 400 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 400 kV} ⟺ EEO x n_PSP 400 kV>0, i∈{0} ⟺ EEO x n_PSP 400 kV=0, 
EEO x n_PSP 400 kV∈N0;
EEO x SR PSP 220 kV i GSS j:
∀ (i,j): ∃ (EEO x SR PSP 220 kV i GSS j) ⇒ ∃ s(EEO x SR PSP 220 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, i∈{0} ⟺ EEO x n_PSP 220 kV=0, j∈{1, ..., EEO x n_GSS 220 kV} ⟺ EEO x n_GSS 220 kV>0, j∈{0} ⟺ EEO x n_GSS 220 kV=0, EEO x n_PSP 220 kV, 
EEO x n_GSS 220 kV∈N0;
EEO x SR PSP 220 kV i PSS i:
∀ (i): ∃ (EEO x SR PSP 220 kV i PSS i) ⇒ ∃ s(EEO x SR PSP 220 kV i PSS i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, i∈{0} ⟺ EEO x n_PSP 220 kV=0, 
EEO x n_PSP 220 kV∈N0;
EEO x P PSP 220 kV i:
∀ (i): ∃ (EEO x P PSP 220 kV i) ⇒ ∃ s(EEO x P PSP 220 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 220 kV} ⟺ EEO x n_PSP 220 kV>0, i∈{0} ⟺ EEO x n_PSP 220 kV=0, 
EEO x n_PSP 220 kV∈N0;
EEO x SR PSP 110 kV i GSS j:
∀ (i,j): ∃ (EEO x SR PSP 110 kV i GSS j) ⇒ ∃ s(EEO x SR PSP 110 kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, i∈{0} ⟺ EEO x n_PSP 110 kV=0, j∈{1, ..., EEO x n_GSS 110 kV} ⟺ EEO x n_GSS 110 kV>0, j∈{0} ⟺ EEO x n_GSS 110 kV=0, EEO x n_PSP 110 kV, 
EEO x n_GSS 110 kV∈N0;
EEO x PSP 110 kV i PSS i:
∀ (i): ∃ (EEO x PSP 110 kV i PSS i) ⇒ ∃ s(EEO x PSP 110 kV i PSS i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, i∈{0} ⟺ EEO x n_PSP 110 kV=0, 
EEO x n_PSP 110 kV∈N0;
EEO x P PSP 110 kV i:
∀ (i): ∃ (EEO x P PSP 110 kV i) ⇒ ∃ s(EEO x P PSP 110 kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP 110 kV} ⟺ EEO x n_PSP 110 kV>0, i∈{0} ⟺ EEO x n_PSP 110 kV=0, 
EEO x n_PSP 110 kV∈N0;
EEO x SR PSP x kV i GSS j:
∀ (i,j): ∃ (EEO x SR PSP x kV i GSS j) ⇒ ∃ s(EEO x SR PSP x kV i GSS j) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, i∈{0} ⟺ EEO x n_PSP x kV=0, j∈{1, ..., EEO x n_GSS x kV} ⟺ EEO x n_GSS x kV>0, j∈{0} ⟺ EEO x n_GSS x kV=0, EEO x n_PSP x kV, 
EEO x n_GSS x kV∈N0;
EEO x PSP x kV i PSS i:
∀ (i): ∃ (EEO x PSP x kV i PSS i) ⇒ ∃ s(EEO x PSP x kV i PSS i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, i∈{0} ⟺ EEO x n_PSP x kV=0, 
EEO x n_PSP x kV∈N0;
EEO x P PSP x kV i:
∀ (i): ∃ (EEO x P PSP x kV i) ⇒ ∃ s(EEO x P PSP x kV i) ∈ {0,1},
gde: i∈{1, ..., EEO x n_PSP x kV} ⟺ EEO x n_PSP x kV>0, i∈{0} ⟺ EEO x n_PSP x kV=0, 
EEO x n_PSP x kV∈N0;
Status uklopnog stanja RO za svaki EEO x, gde x ∈{1, ..., n_EEO}, n_EEO>1, n_EEO∈N, definiše korisnik.

# Opis elektroenergetske opreme
## Vodovi
### Dalekovodi
### Kablovi
### Mešoviti vodovi
## Energetski transformatori
## Rasklopna oprema
### Prekidač
### Sabirnički rastavljač
### Izlazni rastavljač / linijski rastavljač
### Uzemljenje trase dalekovoda / uzemljenje dalekovoda
### Uzemljenje prekidača dalekovodnog polja
## Merna oprema
### Strujni merni transformator - SMT
### Naponski merni transformator – NMT
## Sistemi sabirnica
### Glavni sistem sabirnica
### Pomoćni sistem sabirnica


# Kvarovi
## Podela kvara


# Relejna zaštita
## Zaštita dalekovoda
### Distantna zaštita dalekovoda
### Diferencijalna zaštita dalekovoda
### APU funkcija
## Zaštita transformatora
## Zaštita sabirnica
### Osnovna zaštita sabirnica
Zaštita od otkaza prekidača
### Rezervna zaštita sabirnica
## Segmenti elektroenergetske opreme

# Primeri
## Selektivno delovanje relejne zaštite
## Neselektivno delovanje relejne zaptite