"""
Esercizio: Sistema Astratto di Trasporto Merci


Requisiti
1. Classe Astratta: VeicoloTrasporto
Crea una classe astratta chiamata VeicoloTrasporto, che rappresenti un veicolo generico per il trasporto di merci.

La classe deve contenere:

Attributi comuni (protetti)
_targa : stringa

_peso_massimo : intero (capacità di carico in kg)

_carico_attuale : intero (inizialmente 0)

Metodi
Un costruttore che inizializza i campi comuni.

Un metodo concreto:

carica(peso)

 Aumenta il carico attuale se possibile, altrimenti segnala che il peso supera la capacità.

Un metodo concreto:

scarica()

 Riporta il carico attuale a 0.

Un metodo astratto:

costo_manutenzione()

 Ogni veicolo deve avere un costo di manutenzione calcolato secondo regole diverse.


2. Sottoclassi Concrete
Crea almeno tre sottoclassi che estendono la classe astratta e implementano il metodo costo_manutenzione() secondo regole differenti:

a) Camion
Attributo extra: numero_assi

Regola manutenzione (esempio):

100 € per asse + 1 € per kg di carico massimo

b) Furgone
Attributo extra: alimentazione (es. “diesel”, “elettrico”)

Regola manutenzione:

Se elettrico: 200 €

Se diesel: 150 €

c) Motocarro
Attributo extra: anni_servizio

Regola manutenzione:

50 € per ogni anno di servizio


3. Classe GestoreFlotta
Crea una classe che gestisca un elenco di veicoli:

Attributi
veicoli: lista di oggetti derivati da VeicoloTrasporto.


Metodi
aggiungi_veicolo(veicolo)

rimuovi_veicolo(targa)

costo_totale_manutenzione():

 Somma dei costi di manutenzione di tutti i veicoli (polimorfismo sugli oggetti astratti).

stampa_veicoli():

 Elenca targa, tipo e carico attuale.

→ usare tutti i principi dell'OOP
→ aggiungi veicolo costruttore normale
→ rimuovi veicolo deve lavorare poliformico
vedi metodo del rettangolo, fare prova con classe astratta
poi traslare
"""

from abc import ABC, abstractmethod

# --- classe astratta base ---

class VeicoloTrasporto(ABC):
    
    def __init__(self,
                _targa: str,
                _peso_massimo: int,
                _carico_attuale: int = 0):
        self._targa = _targa
        self._peso_massimo = _peso_massimo
        self._carico_attuale = _carico_attuale
    
    def carica(self,
               peso):
        self._carico_attuale += peso
        if self._carico_attuale > self._peso_massimo:
            self._carico_attuale -= peso
            print(f"Capacità massima: {self._peso_massimo}kg")
            print(f"Carico attuale: {self._carico_attuale}kg")
            print(f"OPERAZIONE NON CONSENTISA: {peso}kg + {self._carico_attuale}kg supera la capacità massima")
            print("Diminuire il carico")
        else:
            print(f"CARICO COMPLETATO:\nCarico attuale: {self._carico_attuale}kg")
    
    def scarica(self):
        if self._carico_attuale == 0:
            print("Veicolo vuoto, utilizza 'carica' per caricarlo!")
        else:
            self._carico_attuale = 0
            print(f"VEICOLO SCARICATO:\nCarico attuale: {self._carico_attuale}kg")

    @abstractmethod
    def costo_manutenzione(self):
        pass

    @property
    def targa(self):
        return self._targa
    @property
    def peso_massimo(self):
        return self._peso_massimo
    @property
    def carico_attuale(self):
        return self._carico_attuale
    
    def info(self):
        return f"Targa: {self.targa} | Capacità: {self.peso_massimo}kg | Carico attuale: {self.carico_attuale}kg"

# --- sottoclassi concrete ---

class Camion(VeicoloTrasporto):
    
    def __init__(self,
                 _targa,
                 _peso_massimo,
                 _carico_attuale = 0,
                 numero_assi: int = 2):
        super().__init__(_targa,
                         _peso_massimo,
                         _carico_attuale)
        self.numero_assi = numero_assi
    
    def costo_manutenzione(self):
        # 100€ per asse + 1€ per kg di carico massimo
        return (100 * self.numero_assi) + (1 * self._peso_massimo)    


class Furgone(VeicoloTrasporto):
    pass

class Motocarro(VeicoloTrasporto):
    pass

class GestoreFlotta:
    
    def __init__(self):
        self.veicoli: list[VeicoloTrasporto] = []

    # --- aggiungi veicolo ---
    def aggiungi_veicolo(self,
                         veicolo: VeicoloTrasporto):
        self.veicoli.append(veicolo)
        print(f"Veicolo {veicolo.targa} aggiunto alla flotta.")
    
    # --- rimuovi veicolo ---
    def rimuovi_veicolo(self,
                        targa: str):
        if targa in self.veicoli:
            

        





# --- MENU ---
MENU = """Benvenuto nel Gestore Flotta!
Selezione la funzione:
----------------------------------------
|   1. Aggiungi veicolo                |
|   2. Rimuovi veicolo                 |
|   3. Visualizza flotta               |
|   4. Invia veicolo                   |
|   5. Costo manutenzione              |
|   6. Esci                            |
----------------------------------------
"""

AGGIUNGI_VEICOLO = """Scegli il tipo di veicolo:
----------------------------------------
|   1. Camion                          |
|   2. Furgone                         |
|   3. Motocarro                       |
----------------------------------------
"""


print(MENU)
scelta = int(input("Scelta: "))

match scelta:
    case 1:
        print(AGGIUNGI_VEICOLO)
        tipo = int(input("Selezionato: "))
        targa = input("Targa: ").upper()
        peso_max = int(input("Peso massimo (kg): "))

        
        GestoreFlotta.aggiungi_veicolo()
    case 2:
        GestoreFlotta.rimuovi_veicolo()
    case 3:
        pass
    case 4:
        pass
    case 5:
        pass
    case 6:
        pass
    case _:
        print("Scelta non valida")

