"""
Crea una classe chiamata Libro. 
Questa classe dovrebbe avere:
- Tre attributi: titolo, autore e pagine.
- Un metodo descrizione che restituisca una stringa del tipo
"Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine."
"""

class Libro:
    
    # definizione attributi titolo, autore e pagine
    def __init__(self, titolo, autore, pagine):                     # costruttore
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    # definizione metodo .descrizione()
    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine")

# instanziazione di 4 diverse classi Libro
Libro1 = Libro("The Echo of Whispering Pines", "Elena Vance", 342)
Libro2 = Libro("Circuit Souls", "Marcus Thorne", 289)
Libro3 = Libro("The Midnight Cartographer", "Julian Sterling", 415)
Libro4 = Libro("A Recipe for stardust", "Sanae Ishii", 192)

# print della descrizione con il metodo .descrizione()
Libro1.descrizione()