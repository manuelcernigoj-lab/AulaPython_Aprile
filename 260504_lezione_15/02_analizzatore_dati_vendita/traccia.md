### Esercizio: Analizzatore di Dati di Vendita

Sei stato incaricato di scrivere un programma Python che analizza un insieme di dati
di vendita. I dati di vendita sono rappresentati come una lista di numeri, dove
ciascun numero rappresenta l'importo totale delle vendite in un giorno specifico. Il
tuo programma dovrebbe fare quanto segue:

#### Requisiti:

1. Inserimento dei Dati: Chiedi all'utente di inserire una serie di importi di vendita,
   separati da spazi. Converti questi importi in una lista di numeri interi.
2. Gestione delle Eccezioni: Durante la conversione degli importi in numeri interi,
   gestisci qualsiasi ValueError che possa sorgere a causa di un inserimento errato (ad
   esempio, l'utente inserisce una lettera invece di un numero), informando l'utente
   dell'errore e chiedendogli di reinserire i dati.
3. Calcolo del Totale e della Media: Calcola il totale e la media delle vendite. Stampa
   entrambi i valori con un messaggio appropriato. Se la lista è vuota (ad esempio, se
   l'utente non inserisce alcun dato), stampa un messaggio che indica che non sono
   presenti dati di vendita.
4. Vendite Sopra la Media: Trova e stampa una lista di tutti i giorni in cui le vendite
   hanno superato la media delle vendite di tutto il periodo. Assicurati di gestire
   correttamente il caso in cui non ci siano vendite sopra la media.
5. Visualizzazione dei Risultati: Per ogni punto sopra, stampa i risultati in modo
   chiaro e leggibile, con messaggi appropriati che spiegano cosa sta mostrando il
   programma e salva un file txt con tutto.