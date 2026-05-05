"""
Esercizio 1
Creare una classe base Animale e diverse classi derivate che rappresentano diversi tipi di
animali in uno zoo.
Ogni classe derivata avrà attributi e metodi specifici che riflettono le caratteristiche e
comportamenti unici degli animali che rappresentano.
  - Classe Animale:
      - Attributi:
          - nome (stringa che descrive il nome dell' animale)
          - eta (intero che rappresenta l'età dell'animale)
      - Metodi:
          - fai_suono(): un metodo che stampa un suono generico dell'animale.
  - Classi Figlie:
      - Creare almeno tre classi Figlie di Animale ES: Leone, Giraffa, e Pinguino.
      - Ogni classe avrà attributi e metodi specifici:
          - Per esempio, la classe Leone potrebbe avere un metodo caccia() che stampa un
            messaggio su come il leone sta cacciando.
"""

# SuperClasse Animale
class Animale:

    def __init__(self, nome: str, eta: int):                # costruttore
        self.nome = nome                                    # attributo di istanza
        self.eta = eta                                      # attributo di istanza
    
    def fai_suono(self):                                    # metodo fai_suono(): fa suono generico
        print(f"{self.nome} fa suono generico.")

# SottoClasse Leone derivata da Animale
class Leone(Animale):
    
    def ruggisci(self):                                     # # metodo ruggisci(): ruggisce                          
        print(f"{self.nome} ruggisce.")
    
    def caccia(self):                                       # metodo caccia() specifico per il leone
        print(f"Il leone {self.nome} sta cacciando.")

# SottoClasse Giraffa derivata da Animale
class Giraffa(Animale):
    
    def landisci(self):                                     # metodo landisci(): landisce                          
        print(f"{self.nome} landisce.")
    
    def alza_il_collo(self):                                # metodo alza_il_collo() specifico per la giraffa
        print(f"La giraffa {self.nome} sta alzando il collo.")

# SottoClasse Pinguino derivata da Animale
class Pinguino(Animale):
    
    def garrisci(self):                                     # metodo garrisci(): garrisce                          
        print(f"{self.nome} garrisce.")
    
    def nuota(self):                                        # metodo nuota() specifico per il pinguino
        print(f"Il pinguino {self.nome} sta nuotando.")

animale = Animale("Animale", 5)
leone = Leone("Alex", 3)
giraffa = Giraffa("Melman", 4)
pinguino = Pinguino("Skipper", 6)

print("Che versi fanno gli animali dello zoo?")
animale.fai_suono()
leone.ruggisci()
giraffa.landisci()
pinguino.garrisci()

print("\nChe cosa stanno facendo gli animali dello zoo?")
leone.caccia()
giraffa.alza_il_collo()
pinguino.nuota()