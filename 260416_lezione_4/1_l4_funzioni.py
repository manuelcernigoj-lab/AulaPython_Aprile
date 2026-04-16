"""
1. Esercizio Base: Indovina il numero 
Descrizione: Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). 
L'utente deve indovinare quale numero è stato generato. 
Dopo ogni tentativo, il programma dovrebbe dire all'utente se il numero da 
indovinare è più alto o più basso rispetto al numero inserito. 
Il gioco termina quando l'utente indovina il numero o decide di uscire.
"""

import random

def num_guess():
    
    rand_num = random.randrange(1, 100)
    num_user = int(input("Ho generato un numero tra 1 e 100, indovina qual'è!"))
    
    ans = ""
    while rand_num != num_user and ans != "si":
        if rand_num > num_user:
            num_user = int(input("Mi spiace non hai indovinato! Il numero da indovinare è più alto"))
            ans = input("Se desiderii uscire digita [si], premi invio per ritentare").lower()
        elif rand_num < num_user:
            num_user = int(input("Mi spiace non hai indovinato! Il numero da indovinare è più basso"))
            ans = input("Se desiderii uscire digita [si], premi invio per ritentare").lower()
        else:
            print(f"Congratulazioni hai indovinato! Il numero era: {rand_num}")      

    if rand_num != num_user:
        print(f"Sei uscito dal gioco! Il numero era: {rand_num}")

num_guess()
