from inventario import Inventario as inv

class Admin:
    
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        
    def visualizza_vendite(self, inventario: inv):
        if len(inventario.rapporto_vendite) == 0:
            print("Nessuna vendita registrata.")
            return
        print(inventario.rapporto_vendite)
    
    def visualizza_guadagno(self, inventario: inv):
        print(f"Guadagno totale: {inventario.guadagno_totale:.2f}€")
        
    def aggiungi_articolo(self, inventario: inv, nome, prezzo, quantita):
        inventario.aggiungi_articolo(nome, prezzo, quantita)
        
    def rimuovi_articolo(self, inventario: inv, nome):
        inventario.rimuovi_articolo(nome)
        
    def aggiorna_articolo(self, inventario: inv, nome, prezzo, quantita):
        inventario.aggiorna_articolo(nome, prezzo, quantita)
    
    # --- properties ---
    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password
    
    # descrizione account admin
    def descrivi(self): 
        return f"**Administrator Account**\n--- CREDENZIALI ---\nUsername: {self.username}\nPassword: {self.password}"