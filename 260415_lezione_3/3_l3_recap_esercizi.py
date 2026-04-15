"""
1.  Utilizzo di if
        Scrivi un sistema che prendee in input un numero e stampa "Pari" se il numero 
        è pari, "Dispari" se il numero è dispari.
"""
# input del numero dall'utente
num = int(input("Inserisci un numero:"))

# verifica pari/dispari e print
if (num % 2) == 0:
    print("Pari")
else:
    print("Dispari")

"""
2.  Utilizzo di while e range
        Scrivi un sistema che predne in input un numero intero positivo n e stampa tutti i numeri
        da n a 0 (compreso), decrementando di 1. Deve potersi ripetere all'infinito.
"""
# il loop continua finché l'utente risponde "si"
ans = "si"
while ans == "si":
    # input del numero da cui partire per il conto alla rovescia
    num = int(input("Inserisci un numero:"))

    # --- conto alla rovescia ---
    for c in range(num + 1):                            # ad ogni iterazione stampa num - c, scendendo da num fino a 0
        print(num - c)
    ans = input("Vuoi continuare: si / no?").lower()    # input per decidere se ripetere o terminare
    
    # --- verifica risposta ---
    if ans == "si":
        print("Continuiamo!")
    else:                                               # qualsiasi risposta diversa da "si" termina il loop
        print("Stop!")

"""
3.  Utilizzo di for
        Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di ciascun numero della lista
"""

# lista che raccoglie i numeri inseriti dall'utente
lista = []
continua = True             # flag di controllo del loop

# il loop continua finché l'utente non sceglie di procedere
while continua:

    # input del numero da aggiungere alla lista
    num = int(input("Inserisci un numero intero da aggiungere alla lista:"))
    lista.append(num)

    # input per decidere se aggiungere un altro numero o procedere
    ans = input("Vuoi aggiungere un altro numero? Digita [si] per confermare, qualsiasi altro tasto per procedere:").lower()

    if ans != "si":
        continua = False    # interrompe il loop al prossimo controllo del while

# --- stampa dei quadrati ---
print("La lista dei tuoi numeri al quadrato è:")
for n in range(len(lista)):
    print(lista[n] ** 2)    # eleva al quadrato ogni elemento della lista

"""
4.  Utilizzo di if, while e for insieme
        Scrivi un sistema che prende in input una lista di numeri interi che precedenemente è stata
        valorizzata dall'utente. Il sistema deve: 
            - utilizzare un ciclo for per trovare il numero massimo nella lista
            - utilizzare un ciclo while pper contare quanti numeri sono presenti nella lista
            - utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, altrimenti
              stampare il numero massimo trovato e il numero di elementi nella lista.
"""