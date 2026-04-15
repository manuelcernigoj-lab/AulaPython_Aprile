#CONTROLLO DEL FLUSSO: CONDIZIONI / CICLI
#condizione if

#se la condizione numero>0 è vera, viene stampato il codice 
#se il numero è uguale a 100, viene stampato un altro blocco di codice
#altrimenti, se nessuna delle due if è vera, si esegue l'elif
#se anche l'elif è falsa, si esegue l'else

numero = 10

if numero >0:
    print("il numero è positivo.")
    if numero == 100: #if annidato
        print("wow!")
elif numero <0:
    print("Il numero è negativo.")      
else:
    print("Il numero è zero.")  