"""
creare una classe ContoBancario che incapsula le informazioni di un conto e 
fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare
l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate
al saldo del conto.

1. Classe ContoBancario:
    - Attributi privati:
        - __titolare (stringa che rappresenta il nome del titolare del conto)
        - __saldo (decimale che rappresenta il saldo del conto)
    - Metodi pubblici:
        - deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
        - preleva(importo): sottrae un importo dal saldo solo se ci sono fondi 
          sufficienti e l'importo è positivo.
        - visualizza_saldo(): restituisce il saldo corrente senza permettere la sua 
        modifica diretta.
2. Gestione dei Metodi e Sicurezza:
    - I metodi deposita e preleva devono controllare che gli importi siano validi 
      (e.g., non negativi).
    - Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, 
      applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota).
"""

class ContoBancario:
    
    def __init__(self,                      # costruttore
                 titolare: str,             # nome del titolare del conto
                 saldo: float):             # saldo del conto
        self.__titolare = titolare          # privato
        self.__saldo = saldo                # privato
    
    def deposita(self,
                 importo: float):
        if importo > 0:
            self.__saldo += importo
            print(f"DEPOSITO ESEGUITO - hai depositato {importo:.2f}€ sul conto")
        else:
            print(f"ERRORE - inserito importo negativo: {importo:.2f}€")
    
    def preleva(self,
                importo: float):
        if importo > 0:
            if self.__saldo > 0 :
                if self.__saldo > importo:
                    self.__saldo -= importo
                    print(f"PRELIEVO ESEGUITO - hai prelevato {importo:.2f}€ dal conto")
                else:
                    print(f"ERRORE - saldo conto insufficente")
            else:
                print(f"ERRORE - saldo conto negativo, impossibile prelevare")
        else:
            print(f"ERRORE - inserito importo negativo")

    @property                               # per definire il getter di __saldo
    def visualizza_saldo(self):
        print(f"Il tuo saldo è di {self.__saldo:.2f}€")
        return self.__saldo
    
    @property
    def titolare(self):
        print(f"Il conto è intestato a {self.__titolare}")
        return self.__titolare

    @titolare.setter
    def titolare(self,
                 nuovo_titolare):
        if type(nuovo_titolare) == str and nuovo_titolare != "":
            self.__titolare = nuovo_titolare
            print(f"Titolare conto modificato, nuovo titolare: {nuovo_titolare}")
        else:
            print(f"Impossibile modificare il titolare, valore inserito invalido: {nuovo_titolare}")
 
    
conto = ContoBancario("Manu", 1000.50)
conto.visualizza_saldo
conto.preleva(2000)
conto.visualizza_saldo
conto.preleva(50)
conto.visualizza_saldo
conto.deposita(1200)
conto.visualizza_saldo
conto.titolare
conto.titolare = ""
conto.titolare = "Paolo"
conto.titolare
    
