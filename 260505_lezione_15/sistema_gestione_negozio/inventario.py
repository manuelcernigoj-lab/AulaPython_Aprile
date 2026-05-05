# --- modulo Inventario ---

from prodotto import Prodotto as pr
from datetime import datetime as dt

class Inventario:
    
    def __init__(self, guadagno_totale = 0):
        self.prodotti = []
        self.rapporto_vendite = ""
        self.guadagno_totale = guadagno_totale
    
    def aggiungi_prodotto(self, nuovo_prodotto: pr):
        self.prodotti.append(nuovo_prodotto)
        return True
        
    def rimuovi_prodotto(self, nome):
        nuova_lista = [p for p in self.prodotti if p.nome != nome]

        if len(nuova_lista) == len(self.prodotti):
            print(f"Prodotto: {nome} non è presente nell'inventario")    
            return False

        self.prodotti = nuova_lista
        return True
    
    def aggiorna_prodotto(self, prodotto_aggiornato: pr):
        nuova_lista = [prodotto_aggiornato if p.nome == prodotto_aggiornato.nome else p for p in self.prodotti]
        
        if len([p for p in nuova_lista if p.nome == prodotto_aggiornato.nome]) == 0:
            print(f"Prodotto {prodotto_aggiornato.nome} non trovato nell'inventario")
            return False
        
        self.prodotti = nuova_lista
        return True
    
    def vendi_prodotto(self, nome: str, venduti: int):
        for p in self.prodotti:
            if p.nome == nome:
                if p.quantita < venduti:
                    print(f"Scorte insufficienti: disponibili {p.quantita} unità")
                    return False
                fatturato = p.prezzo * venduti
                p.quantita -= venduti
                self.guadagno_totale += fatturato
                self.rapporto_vendite += f"""Data: {dt.now().strftime("%d/%m/%y %H:%M")}
Prodotto: {p.nome}
Quantità: {venduti}
Fatturato: {fatturato}\n"""
                return True
    
        # eseguito solo se il for finisce senza trovare il prodotto
        print(f"Prodotto {nome} non trovato nell'inventario")
        return False

    def stampa_inventario(self):
        for p in self.prodotti:
            print(p.descrivi())

    def trova_prodotto(self, nome):
        trovato = [p for p in self.prodotti if p.nome == nome]
        return trovato

            

"""         
# --- test inventario ---

import prodotto as pr
from inventario import Inventario

# --- creazione inventario e prodotti ---
inv = Inventario()

inv.aggiungi_prodotto(pr.Prodotto("Mela", 0.50, 100))
inv.aggiungi_prodotto(pr.Prodotto("Pera", 0.80, 50))
inv.aggiungi_prodotto(pr.Prodotto("Banana", 1.20, 30))

print("=== Inventario iniziale ===")
inv.stampa_inventario()

# --- vendita prodotti ---
print("\n=== Vendite ===")
print(inv.vendi_prodotto("Mela", 20))        # ✅ dovrebbe funzionare
print(inv.vendi_prodotto("Pera", 100))       # ❌ scorte insufficienti
print(inv.vendi_prodotto("Kiwi", 5))         # ❌ prodotto non trovato

print("\n=== Inventario dopo vendite ===")
inv.stampa_inventario()
print(f"Guadagno totale: {inv.guadagno_totale:.2f}€")

# --- aggiornamento prodotti ---
print("\n=== Aggiornamenti ===")
print(inv.aggiorna_prodotto(pr.Prodotto("Banana", 0.99, 60)))   # ✅ aggiorna prezzo e quantità
print(inv.aggiorna_prodotto(pr.Prodotto("Mango", 2.00, 20)))    # ❌ non trovato

print("\n=== Inventario dopo aggiornamenti ===")
inv.stampa_inventario()

# --- rimozione prodotti ---
print("\n=== Rimozioni ===")
print(inv.rimuovi_prodotto("Pera"))          # ✅ rimossa
print(inv.rimuovi_prodotto("Pera"))          # ❌ non più presente

print("\n=== Inventario finale ===")
inv.stampa_inventario()

# --- rapporto vendite ---
print("\n=== Rapporto vendite ===")
print(inv.rapporto_vendite) """