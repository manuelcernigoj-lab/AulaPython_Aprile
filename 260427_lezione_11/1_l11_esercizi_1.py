"""
creare una classe base MetodoPagamento e diverse classi derivate che rappresentano
diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in
azione, permettendo alle diverse sottoclassi di implementare i loro specifici
comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe
base.

1. Classe MetodoPagamento:
    - Metodi:
        - effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
2. Classi Derivate:
    - CartaDiCredito:
        - Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
    - PayPal:
        - Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
    - BonificoBancario:
        - Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
3. GestorePagamenti:
- Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza 
  preoccuparsi del dettaglio del metodo di pagamento.

flusso:
- ciao, come ti chiami
- quanto credito hai radomizzi un credito
- come vuoi pagare (metodo)
- quanto vuoi pagare (importo a cui aggungere commissione)
- se credito insufficiente: errore.

Nota: 
  usare metodo polimorfico
Extra: 
  aggiungere commissione differente in base al tipo di pagamento
"""
import random

class MetodoPagamento:

    COMMISSIONE = 0.0

    def __init__(self):
        self.credito = round(random.uniform(1, 100), 2)
    
    def effettua_pagamento(self,
                           importo: float):
        tot = round(importo * (1 + self.COMMISSIONE), 2)
        commissione = round(importo * self.COMMISSIONE, 2)

        # importo = int(input("Inserisci l'importo in € per il pagamento: "))

        if importo <= 0:
            print(" Transazione negata: importo non valido.")
        elif tot > self.credito:
            print(
                f"  Transazione negata: credito insufficiente.\n"
                f"  Richiesto: {tot}€ | Disponibile: {self.credito}€"
                )
        else:
            self.credito = round(self.credito - tot, 2)
            print(
                f"  Pagamento eseguito: {importo}€ "
                f"+ commissione {commissione}€ = {tot}€\n"
                f"  Credito residuo: {self.credito}€"
                )  
            
class CartaDiCredito(MetodoPagamento):

    # commissione 2%
    COMMISSIONE = 0.02

    def __init__(self):
        super().__init__()                      # eredita credito random

    def effettua_pagamento(self, 
                           importo: float):
        print("[Carta di Credito]")
        super().effettua_pagamento(importo)     # riusa metodo base

class PayPal(MetodoPagamento):

    # commissione 3.5%
    COMMISSIONE = 0.035

    def __init__(self):
        super().__init__()                      # eredita credito random

    def effettua_pagamento(self, 
                           importo: float):
        print("[Pay Pal]")
        super().effettua_pagamento(importo)     # riusa metodo base

class BonificoBancario(MetodoPagamento):

    # No commissione
    COMMISSIONE = 0.0

    def __init__(self):
        super().__init__()                      # eredita credito random

    def effettua_pagamento(self, 
                           importo: float):
        print("[Bonifico Bancario]")
        super().effettua_pagamento(importo)     # riusa metodo base
            
class GestorePagamenti:

    METODI = {
        "1": ("Carta di Credito", CartaDiCredito),
        "2": ("PayPal",           PayPal),
        "3": ("Bonifico Bancario", BonificoBancario),
    }

    def avvia(self):
        nome = input("Ciao! Come ti chiami? ").strip()
        print(f"Benvenuto, {nome}!")

        print("\nMetodi di pagamento disponibili:")
        for key, (label, _) in self.METODI.items():
            cls = self.METODI[key][1]
            print(f"  {key}. {label}\n  (commissione: {cls.COMMISSIONE*100:.1f}%)")

        scelta = input("Scegli un metodo (1 | 2 | 3): ").strip()
        if scelta not in self.METODI:
            print("Scelta non valida.")
            return

        label, Cls = self.METODI[scelta]
        metodo: MetodoPagamento = Cls()  # polymorphic instantiation
        print(f"\nCredito disponibile su {label}: {metodo.credito}€")

        importo = float(input("Quanto vuoi pagare (€)? "))
        print()
        metodo.effettua_pagamento(importo)  # gestisce tutto internamente
    
gestore = GestorePagamenti()
gestore.avvia()