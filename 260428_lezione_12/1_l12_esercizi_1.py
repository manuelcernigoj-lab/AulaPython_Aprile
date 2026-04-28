"""
Un'azienda vuole gestire i suoi impiegati tramite un sistema informatico. Esistono
diversi ruoli all'interno dell'ufficio, ma tutti gli impiegati hanno alcune
caratteristiche comuni, come il nome, il cognome e lo stipendio. 


Inoltre, ogni impiegato ha un metodo per calcolare il suo stipendio mensile, che
può variare a seconda del ruolo.


Obiettivi:


Creare una classe astratta Impiegato con:

Un costruttore che accetta nome, cognome e stipendio base.

Un metodo astratto calcola_stipendio() che dovrà essere implementato dalle
classi derivate.

Creare due classi derivate:

ImpiegatoFisso: riceve lo stipendio base senza modifiche.

ImpiegatoAProvvigione: riceve lo stipendio base più un bonus basato sulle
vendite.

Implementare una funzione che stampi le informazioni degli impiegati e il loro
stipendio calcolato.
"""

import random
from abc import ABC, abstractmethod

class Impiegato(ABC):
    
    def __init__(self,
                 nome: str,
                 cognome: str,
                 stipendio_base: float = 1700.0):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
    
    @abstractmethod
    def calcola_stipendio(self):
        pass

    def info(self):
        return f"{self.nome} {self.cognome}"

class ImpiegatoFisso(Impiegato):

    def __init__(self,
                 nome: str,
                 cognome: str,
                 stipendio_base: float = 1700.0):
        super().__init__(nome,
                         cognome,
                         stipendio_base)
    
    def calcola_stipendio(self):
        stipendio = self.stipendio_base
        return stipendio
    
class ImpiegatoAProvvigione(Impiegato):

    def __init__(self,
                 nome: str,
                 cognome: str,
                 stipendio_base: float = 1700.0, 
                 vendite: float = 0.0):
        super().__init__(nome,
                         cognome,
                         stipendio_base)
        self.vendite = vendite
    
    def vendi(self):
        self.vendite += random.uniform(100, 100000)
        print(f"Le tue vendite mensili sono state di: {self.vendite:.2f}")
        
    def calcola_stipendio(self):
        bonus = self.vendite * 0.05
        stipendio = self.stipendio_base + bonus
        return stipendio




mario = ImpiegatoFisso("Mario", "Rossi")
print(mario.info(), mario.calcola_stipendio())

"""
Aggiungere la classe astratta promozione che va in entrambe le classi 
derivate e ha un emtodo verificato da if per aumentare lo 
stipendio al raggingimento di condizioni x scelte da voi
"""
    

