# --- modulo Prodotto ---

class Prodotto:         # rappresenta un singolo prodotto in inventario

    def __init__(self, nome: str, prezzo: float, quantita: int):
        self.__nome = nome
        self.__prezzo = prezzo
        self.__quantita = quantita
        
    # --- properties/setters ---
    @property
    def nome(self):
        return self.__nome
    
    @property
    def prezzo(self):
        return self.__prezzo
    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
        self.__prezzo = nuovo_prezzo

    @property
    def quantita(self):
        return self.__quantita
    @quantita.setter
    def quantita(self, nuova_quantità):
        self.__quantita = nuova_quantità
        
    # metodo per descrizione completa prodotto
    def descrivi(self): 
        return f"Prodotto: {self.__nome}\nPrezzo: {self.__prezzo:.2f}€\nQuantità: {self.__quantita}\n"
    