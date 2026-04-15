#CICLO WHILE - ripete il codice finché una condizione è vera
conteggio = 0

while conteggio <5:
    print(conteggio)
    conteggio += 1
    
#WHILE con booleano
controllore = True

while controllore:
    print ("ciao") 
    
    scelta = input("Vuoi continuare? ")
    
    if scelta == "no":
        controllore = False
        
#CICLO FOR con lista
numeri = [1, 2, 3, 4, 5]   

#per ogni numero della lista, stampa il numero
for numero in numeri:
    print(numero)       
    
#RANGE(), sequenza di numeri che possono essere iterati

#solo stop definito
for i in range(81):
    print(i)    
    
#start e stop definiti
for i in range(5, 10): 
    print(i)
    
#start, stop e step definiti
for i in range (5, 55, 5):
    print(i)