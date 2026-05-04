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


class Analisi:

   def calcola_statistiche(self):
      self.vendite = inserimento.Inserimento.lista_vendite()
      self.date = [dt.today() - td(days = i) for i in range(len(self.vendite)-1, -1, -1)]

      self.totale = np.sum(self.vendite)
      self.media = np.mean(self.vendite)

      print(f"""
--- ANALISI VENDITE ---
TOTALE: {self.totale}
MEDIA: {self.media}
""")

   def giorni_sopra_media(self):
      sopra_media = {}

      for d, v in zip(self.date, self.vendite):
         if v > self.media:
            sopra_media[d.strftime('%d-%m-%Y')] = v
   
      print("--- VENDITE SOPRA LA MEDIA ---")
      if sopra_media:
         for d, v in sopra_media.items():
            print(f"{d}: {v}")
      else:
         print(f"Non ci sono vendite sopra la media nella lista")

# --- Test ---
a = Analisi()          
a.calcola_statistiche()
a.giorni_sopra_media()


