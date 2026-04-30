
# leggi
file = open("260430_lezione_14/prova.txt", "r")
contenuto = file.read()
riga = file.readline()
print(contenuto)

# scrivi
file = open("260430_lezione_14/prova.txt", "w")
file.write("Questo è un esempio di scrittuta su file")
file.close()            # importantissimo