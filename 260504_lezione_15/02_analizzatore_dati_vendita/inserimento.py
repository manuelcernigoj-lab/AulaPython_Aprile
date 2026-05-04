"""
1. Inserimento dei Dati: Chiedi all'utente di inserire una serie di importi di vendita,
   separati da spazi. Converti questi importi in una lista di numeri interi.
2. Gestione delle Eccezioni: Durante la conversione degli importi in numeri interi,
   gestisci qualsiasi ValueError che possa sorgere a causa di un inserimento errato (ad
   esempio, l'utente inserisce una lettera invece di un numero), informando l'utente
   dell'errore e chiedendogli di reinserire i dati.
"""

def inserisci_vendite():
      
   check = True

   while check:
      importi = input("Inserirsci gli importi di vendita degli ultimi giorni separati da spazi (es. 10 5 36 820 50): ")
      vendite = importi.split(" ")
      vendite_int = []
      
      # conversione: str → int
      for v in vendite:
         try:
            vendite_int.append(int(v))
         except ValueError:
            print(f"ERRORE: trovato un valore anomalo nella lista '{v}' → inserisci solo interi separati da spazi.")     
            break
      # eseguito solo se il for loop termina senza 'break'
      else:
         check = False
   
   print(f"VENDITE INSERITE: {vendite_int}")
   return vendite_int

""" 
# --- Test ---
inserisci_vendite()
"""