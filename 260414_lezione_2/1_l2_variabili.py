#VARIABILI E TIPI DI DATI

#numeri (int) 
num = 15 

#numeri con virgola mobile (float)
num1 = 0.5
num2 = 34.5

#carattere (char)
char = 'a'

#stringa (str)
nome = "Aurora"
msg = "Ciao a tutti!"

s = "Python"

#stampa un carattere in base all'indice 
#stamperà la prima lettera dato che gli indici partono da 0
print(s[0])

#stamperà la terza lettera 
print(s[2])

#CONCATENA stringa
saluto = "Ciao"
nome = "Aurora"
messaggio = saluto + " " + nome
print(messaggio)

#METODI STRINGA
s = "Ciao, mondo!"

#len(), è una funzione, ottiene la lunghezza della stringa
print(len(s))

#upper(), converte la stringa in maiuscolo
print(s.upper())

#lower(), converte la stringa in minuscolo
print(s.lower())

#split(), divide la stringa in una lista di sottostringhe in base al delimitatore
print(s.split(","))

#replace(), sostituisce parti di una stringa con un'altra
print(s.replace("mondo", "universo"))

#booleani (bool) 
bool1 = True
bool2 = False

print(bool1)

#operatori di confronto 
x = 5 
y = 10

print(x == y)
print(x != y)
print(x < y)

#operatori logici AND, OR, NOT
z = 7

print(x < z and y > z)  
print(x < z or z > y)
print(not(x < y))

#COLLECTIONS
#lista, tipo list, definita da [], modificabile, ordinata
numeri = [1, 2, 3, 4, 5]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5] #lista eterogenea

print(numeri[0])
print(numeri[2])

#modificabilità lista
numeri[2] = 10

print(numeri)

#metodi liste
numeri2 = [3, 1, 4, 2, 5]

#len() ottiene la lunghezza della lista
print(len(numeri2))

#append(), aggiunge un elemento alla fine della lista
numeri2.append(6)
print(numeri2)

#insert(), inserisce un elemento in una posizione specifica
numeri2.insert(2, 10)
print(numeri2)

#remove(), rimuove un elemento (e non in base all'indice in questo caso)
numeri2.remove(10)
print(numeri2)

#sort(), ordina gli elementi della lista
numeri2.sort()
print(numeri2)