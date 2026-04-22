"""
Esercizio 6 (Facile) @classmethod: 
Crea una classe chiamata Animale. Questa classe deve avere:
- Un attributo di classe numero_animali, inizializzato a 0.
- Due attributi di istanza: nome e specie, passati al costruttore.
- Il costruttore deve incrementare numero_animali di 1 ogni volta che 
  viene creato un nuovo animale.
- Un metodo di classe quanti_animali che stampi una stringa del tipo 
  "Numero di animali creati: 'numero_animali'".
Crea almeno 3 oggetti Animale e poi chiama quanti_animali direttamente 
dalla classe, senza usare nessuna delle istanze create.
"""

class Animale:

    numero_animali = 0                                      # attributo di classe: contatore

    def __init__(self, nome, specie):                       # costruttore
        self.nome = nome                                    # attributo di istanza
        self.specie = specie                                # attributo di istanza
        Animale.numero_animali += 1                         # aumento del contatore
    
    @classmethod                                            # metodo di classe
    def quanti_animali(cls):
        print(f"Numero di animali creati: {cls.numero_animali}")

# creazione delle istanze animali
a1 = Animale("Fido", "Cane")
a2 = Animale("Tina", "Gatto")
a3 = Animale("Jack", "Pappagallo")

# chiamata del metodo .quanti_animali()
Animale.quanti_animali()
