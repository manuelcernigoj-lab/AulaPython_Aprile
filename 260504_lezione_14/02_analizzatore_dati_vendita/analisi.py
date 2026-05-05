""" 
3. Calcolo del Totale e della Media: Calcola il totale e la media delle vendite. Stampa
   entrambi i valori con un messaggio appropriato. Se la lista è vuota (ad esempio, se
   l'utente non inserisce alcun dato), stampa un messaggio che indica che non sono
   presenti dati di vendita.
4. Vendite Sopra la Media: Trova e stampa una lista di tutti i giorni in cui le vendite
   hanno superato la media delle vendite di tutto il periodo. Assicurati di gestire
   correttamente il caso in cui non ci siano vendite sopra la media. 
"""
import inserimento
import numpy as np
from datetime import datetime as dt, timedelta as td

vendite = inserimento.inserisci_vendite()
date = [dt.today() - td(days = i) for i in range(len(vendite)-1, -1, -1)]

def totale_vendite():

   totale = np.sum(vendite)
   return totale

def media_vendite():

   media = np.mean(vendite)
   return media

def vendite_sopra_media():

   sopra_media = {}

   for d, v in zip(date, vendite):
      if v > media_vendite():
         sopra_media[d.strftime('%d-%m-%Y')] = v
   
   return sopra_media

def report_vendite():

   report = ""

   report += f"""
--- ANALISI VENDITE ---
TOTALE: {totale_vendite()}
MEDIA: {media_vendite()}

--- VENDITE SOPRA LA MEDIA ---
"""
   sopra_media = vendite_sopra_media()
   if sopra_media:
      for d, v in sopra_media.items():
         report += f"{d}: {v}\n"
   else:
      report += "Non ci sono vendite sopra la media nella lista\n"
   
   report += f"{'-' * 40}\n"
   return report

"""
# --- Test ---       
report_vendite()
"""