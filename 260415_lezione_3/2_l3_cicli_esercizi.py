"""
1.  Chiedi all'utente di inserire un numero. Il programma dovrebbe fare un conto 
    alla rovescia a partire da quel numero fino a zero, stampando ogni numero e chiedere
    se si vuole ripetere o no.
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
2.  Chiedi all'utente di inserire un numero. Il programma dovrebbe controllare se
    il numero inserito è primo/pari o no. Se è primo, lo salva e stampa "Il numero è primo."
    Altrimenti, stampa "Il numero non è primo." Si ferma quando ha 5 numeri primi.
"""
# inizializzazione lista vuota
lista = []

# ciclo while per far fermare il codice solo quando ha salvato 5 numeri primi
while len(lista) < 5:

    # chiedere il numero in input
    num = int(input("Inserisci un numero:"))

    # se il numero è primo, salva dentro la lista e stampa un messaggio
    if (num % 2) != 0:
        lista.append(num)
        print("Il numero è primo")
    # se il numero NON è primo, stampa un messaggio
    else:
        print("Il numero non è primo")

# stampa la lista con i numeri primi
print("Hai 5 numeri primi:", lista)