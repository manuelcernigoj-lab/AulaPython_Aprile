"""
Esercizio 5 (Facile) @staticmethod: 
Crea una classe chiamata Convertitore. Questa classe dovrebbe avere:
- Un metodo statico euro_in_dollari che accetti un importo in euro e restituisca 
  il valore convertito in dollari, usando un tasso fisso di 1.08.
- Un metodo statico km_in_miglia che accetti una distanza in chilometri e restituisca 
  il valore convertito in miglia, usando un fattore fisso di 0.621371.
Testa la classe chiamando entrambi i metodi direttamente dalla classe, senza creare alcun oggetto.
"""

class Convertitore:

    @staticmethod                               # metodo statico 1
    def euro_in_dollari(euro):
        return round(euro * 1.08, 2)            # conversione usando il tasso fisso [€ / $]: 1.08
    
    @staticmethod                               # metodo statico 2
    def km_in_miglia(km):
        return round(km * 0.621371, 2)          # conversione usando il tasso fisso [km / m]: 0.621371

# test della classe richiamando entrambi i metodi di conversione nel print()
print(f"""Euro convertiti in Dollari:  {Convertitore.euro_in_dollari(74)}
Km convertiti in Miglia:   {Convertitore.km_in_miglia(200)}""")