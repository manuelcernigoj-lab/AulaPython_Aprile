"""
Sistema di gestione studenti
Immagina di dover creare un sistema di gestione per una scuola che deve mantenere
le informazioni sugli studenti, i professori e le lezioni. Seguendo il paradigma 
della programmazione orientata agli oggetti (OOP), dovrai implementare le classi 
necessarie usando incapsulamento, ereditarietà e polimorfismo.

Specifiche
1. Classe Persona:
    - Crea una classe base chiamata Persona che rappresenti una persona generica.
    - Attributi:
        - nome: stringa
        - eta: intero
    - Metodi:
        - __init__(self, nome, eta): costruttore che inizializza nome ed eta.
        - presentazione(self): metodo che stampa una frase con il nome e l'età della persona.
    - Regola 1 - Incapsulamento: Gli attributi nome ed eta devono essere privati. 
      Usa getter e setter per accedere e modificare il nome e l'età.
2. Classe Studente:
    - Crea una sottoclasse di Persona chiamata Studente.
    - Attributi:
        - voti: lista di interi che rappresentano i voti dello studente.
    - Metodi:
        - __init__(self, nome, eta, voti): costruttore che inizializza il nome, l'età e i 
          voti dello studente.
        - calcola_media(self): metodo che restituisce la media dei voti.
        - Override del metodo presentazione(self) per includere la media dei voti nella 
          presentazione.
    - Regola 2 - Ereditarietà: Studente eredita dalla classe Persona.
3. Classe Professore:
    - Crea una sottoclasse di Persona chiamata Professore.
    - Attributi:
        - materia: stringa che rappresenta la materia insegnata.
    - Metodi:
        - __init__(self, nome, eta, materia): costruttore che inizializza il nome, l'età 
          e la materia insegnata dal professore.
        - Override del metodo presentazione(self) per includere la materia nella presentazione.
    - Regola 3 - Polimorfismo: Sia la classe Studente che la classe Professore devono 
      fornire una versione specifica del metodo presentazione, rendendolo polimorfico.
"""

class Persona:
    
    def __init__(self,                      # costruttore
                nome: str,
                eta: int):
        self.__nome = nome
        self.__eta = eta
    
    def presentazione(self):                # metodo che stampa una frase con il nome e l'età della persona.
        print(f"Ciao! Mi chiamo {self.__nome} e ho {self.__eta} anni!")

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,
             nuovo_nome):
        if type(nuovo_nome) == str and  nuovo_nome != "":
            self.__nome = nuovo_nome
            print(f"Nome modificato, nuovo nome: {nuovo_nome}")
        else:
            print(f"Impossibile modificare il nome, valore inserito invalido: {nuovo_nome}")
    
    @property
    def eta(self):
        return self.__eta
    
    @eta.setter
    def eta(self,
             nuova_eta):
        if type(nuova_eta) == int and  nuova_eta > 0:
            self.__eta = nuova_eta
            print(f"eta modificato, nuova eta: {nuova_eta}")
        else:
            print(f"Impossibile modificare il eta, valore inserito invalido: {nuova_eta}")
    
class Studente(Persona):
    
    def __init__(self,                      # costruttore
                nome: str,
                eta: int,
                voti: list = []):                  
        super().__init__(nome,
                         eta)
        self.voti = voti

    def calcola_media(self):                # metodo che restituisce la media dei voti.
        if not self.voti:
            print("Nessun voto disponibile.")
        else:
            media = sum(self.voti) / len(self.voti)
            return media
            #print(f"La tua media è: {media:.2f}")

    def presentazione(self):                # metodo che stampa una frase con il nome e l'età della persona.
        #media = sum(self.voti) / len(self.voti) if self.voti else 0
        print(f"Ciao! Mi chiamo {self.nome} e ho {self.eta} anni. La mia media è {self.media:.2f}")

class Professore(Persona):
    
    def __init__(self,                      # costruttore
                nome: str,
                eta: int,
                materia: str):                  
        super().__init__(nome,
                         eta)
        self.materia = materia

    def presentazione(self):                # metodo che stampa una frase con il nome e l'età della persona.
        print(f"Ciao! Mi chiamo {self.nome} e ho {self.eta} anni. Sono professore di {self.materia}")

manu = Studente("Manuel", 33, [30, 25, 23])
manu.presentazione()
manu.calcola_media()
piero = Professore("Piero", 53, "Storia")
piero.presentazione()



        

    
        
        

    
