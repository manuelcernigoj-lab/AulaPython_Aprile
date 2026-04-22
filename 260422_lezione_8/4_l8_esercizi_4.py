"""
--- Esercizio 2 ---
Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che 
produce e vende vari tipi di prodotti. Gli studenti dovranno creare una classe base 
chiamata Prodotto e diverse classi parallele che rappresentano diversi tipi di prodotti. 
Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario e le vendite dei
prodotti.

  1. Classe Prodotto:
      o Attributi:
        • nome (stringa che descrive il nome del prodotto)
        • costo_produzione (costo per produrre il prodotto)
        • prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
      o Metodi:
        • calcola_profitto: restituisce la differenza tra il prezzo di vendita e il 
          costo di produzione.
  2. Classi parallele:
      o Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
      o Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per 
        abbigliamento e garanzia per Elettronica.
  3. Classe Fabbrica:
      o Attributi:
        • inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
        • aggiungi_prodotto: aggiunge prodotti all'inventario.
        • vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto 
          realizzato dalla vendita
        • resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.
"""

# SuperClasse Prodotto
class Prodotto:
    
    def __init__(self,                          # costruttore per Prodotto
                 nome: str,                     # nome del prodotto
                 costo_produzione: float,       # costo per produrre il prodotto
                 prezzo_vendita: float):        # prezzo a cui il prodotto viene venduto al pubblico
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self) -> float:        # metodo calcola_profitto(): vendita - produzione
        return self.prezzo_vendita - self.costo_produzione


# SottoClasse Elettronica
class Elettronica(Prodotto):
    
    def __init__(self, 
                 nome: str, 
                 costo_produzione: float, 
                 prezzo_vendita: float, 
                 garanzia: int):
        super().__init__(nome,                  # inizializza attributi del genitore
                         costo_produzione, 
                         prezzo_vendita)  
        self.garanzia = garanzia                # anni di garanzia


# SottoClasse Abbigliamento
class Abbigliamento(Prodotto):
    
    def __init__(self, 
                 nome: str, 
                 costo_produzione: float, 
                 prezzo_vendita: float, 
                 materiale: str):
        super().__init__(nome,                  # inizializza attributi del genitore
                         costo_produzione, 
                         prezzo_vendita)
        self.materiale = materiale              # materiale del prodotto


# Classe Fabbrica — gestisce l'inventario
class Fabbrica:
    
    def __init__(self):                         # costruttore per Fabbrica
        self.inventario = {}                    # { oggetto_Prodotto: quantità }

    # metodo aggiungi_prodotto(): definisce/incrementa quantità dei prodotti
    def aggiungi_prodotto(self,               
                          prodotto: Prodotto,
                          quantita: int):
        if prodotto in self.inventario:         # se già presente, incrementa quantità
            self.inventario[prodotto] += quantita
        else:                                   # altrimenti, definisce quantità
            self.inventario[prodotto] = quantita
        print("\n--- Aggiunta prodotti ---")
        print(f"Aggiunto: {prodotto.nome} x {quantita}")

    # metodo vendi_prodotto(): diminuisce quantità dei prodotti
    def vendi_prodotto(self,
                       prodotto: Prodotto, 
                       quantita: int):
        
        # se prodotto non è in nventario o è presente quantità insufficiente: errore
        if prodotto not in self.inventario or self.inventario[prodotto] < quantita:
            print(f"Scorte insufficienti per {prodotto.nome}")
            return
        
        # se prodotto è in nventario: diminuisci quantità e calcola profitto
        self.inventario[prodotto] -= quantita
        profitto_totale = prodotto.calcola_profitto() * quantita
        print("\n--- Vendita prodotti ---")
        print(f"""Venduto: {prodotto.nome} x {quantita}\nProfitto: €{profitto_totale:.2f}""")

    # metodo reso_prodotto(): incrementa quantità dei prodotti resi
    def reso_prodotto(self, 
                      prodotto: Prodotto, 
                      quantita: int):
        if prodotto not in self.inventario:     # se non presente: errore
            print(f"{prodotto.nome} non trovato in inventario")
            return
        self.inventario[prodotto] += quantita   # se già presente: incrementa inventario
        print("\n--- Reso prodotti ---")
        print(f"Reso accettato: {prodotto.nome} x {quantita}")

    # metodo consulta_inventario(): riepilogo dell'inventario
    def consulta_inventario(self):
        print("\n--- Inventario ---")
        for prodotto, quantita in self.inventario.items():
            print(f"""{prodotto.nome}: {quantita} unità""")

# --- Test ---
laptop = Elettronica("Laptop", costo_produzione=500, prezzo_vendita=899, garanzia=2)
tshirt = Abbigliamento("T-shirt", costo_produzione=8, prezzo_vendita=25, materiale="cotone")

fabbrica = Fabbrica()
fabbrica.aggiungi_prodotto(laptop, 10)
fabbrica.aggiungi_prodotto(tshirt, 50)
fabbrica.consulta_inventario()

fabbrica.vendi_prodotto(laptop, 3)
fabbrica.reso_prodotto(tshirt, 5)
fabbrica.consulta_inventario()