from inventario import Inventario as inv
from prodotto import Prodotto as pr
from datetime import datetime as dt

class Cliente:
    
    def __init__(self, nome: str, cognome: str, username: str, password: str):
        self.__nome = nome
        self.__cognome = cognome
        self.__username = username
        self.__password = password
        self.storico_acquisti = ""

    def acquista_prodotto(self, inventario: inv, nome: str, acquistati: int):
        prodotto = inventario.trova_prodotto(nome)      
        if prodotto is None:
            print(f"Prodotto '{nome}' non trovato nell'inventario")
            return False
        if inventario.vendi_prodotto(nome, acquistati):
            spesa = prodotto.prezzo * acquistati
            self.storico_acquisti += f"""Data: {dt.now().strftime("%d/%m/%y %H:%M")}
Prodotto: {prodotto.nome}
Quantità: {acquistati}
Spesa: {spesa}\n"""
            return True
            
    def visualizza_storico(self):
        if len(self.storico_acquisti) > 0:
            print(self.storico_acquisti) 
        else:
            print(f"Nessun acquisto effettuato da {self.nome} {self.cognome}")
    
    # --- properties ---
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome
    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password
    
    def __str__(self):
        return f"Cliente: {self.nome} {self.cognome}, Username: {self.username}"
    
    # metodo per descrizione profilo cliente
    def descrivi(self): 
        return f"Cliente: {self.nome} {self.cognome}\n--- CREDENZIALI ---\nUsername: {self.username}\nPassword: {self.password}"
