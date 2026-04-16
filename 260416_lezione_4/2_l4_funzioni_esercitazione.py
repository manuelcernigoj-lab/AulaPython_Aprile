"""
Scrivi un programma che esegua le seguenti operazioni:

1.  Chiedi all'utente di inserire un numero intero positivo n. 
    Se l'utente inserisce un numero negativo o zero, continua a chiedere un numero 
    fino a quando non viene inserito un numero positivo.
2.  Genera una lista di numeri interi casuali tra 1 e n (incluso). 
    La lunghezza della lista deve essere n. -> si fa con range
3.  Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
    -> prima faccio creare la lista del punto 2
4.  Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
5.  Utilizza un ciclo per determinare se un numero è primo. 
    La funzione deve restituire True se il numero è primo, altrimenti False.
6.  Utilizza un ciclo for per stampare tutti i numeri primi nella lista.
7.  Infine, utilizza una struttura if per determinare se la somma di tutti i numeri 
    nella lista è un numero primo e stampa il risultato
"""

# --- Funzione 1. ---
def int_pos():
    while True:
        num = int(input("Inserisci un numero intero positivo: "))
        if num <= 0:
            True
        else:
            break

# --- Funzione 2. ---
def list_gen():
    n = int(input("Inserisci un numero intero positivo: "))

    import random
    rand_list = []
    for i in range(1, random.randrange(2, n)):
        rand_list.append(i)
    
    print(f"Ho generato una lista di numeri casuali tra 1 e {n}: {rand_list}")
    return rand_list

# --- Funzione 3. ---
def even_sum():
    lista = list_gen()
    pari = []
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            pari.append(lista[i])
        else:
            pass
    print(f"La somma dei numeri pari nella lista è: {sum(pari)}")

# --- Funzione 4. ---


# --- Funzione 5. ---


# --- Funzione 6. ---


# --- Funzione 7. ---


# --- MENU ---
menu = int(input("Che putno dell'esercizio vuoi vedere? Da 1 a 7 "))

match menu:
    case 1:
        int_pos()
    case 2:
        list_gen()
    case 3:
        even_sum()
    case 4:
        pass
    case 5:
        pass
    case 6:
        pass
    case 7:
        pass
    case _:
        print(f"Inserito valore errato: {menu}")