"""
5. Visualizzazione dei Risultati: Per ogni punto sopra, stampa i risultati in modo
   chiaro e leggibile, con messaggi appropriati che spiegano cosa sta mostrando il
   programma e salva un file txt con tutto.
"""

import analisi
import datetime as dt

def log_vendite():

    report = analisi.report_vendite()
    try:
        with open("260504_lezione_15/02_analizzatore_dati_vendita/report_vendite.txt", "a") as f:
            f.write(f"Log vendite inserite il {dt.datetime.now().strftime('%d-%m-%Y %H:%M')}:\n{report}\n\n")
            print(report)

    except FileNotFoundError:
        print("File non trovato")