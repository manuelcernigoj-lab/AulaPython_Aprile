import numpy as np
import pandas as pd

"""
Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.
"""

# --- Dataset vendite ---
data = {
    "Prodotto":       ["Laptop", "Mouse", "Tastiera", "Monitor", "Cuffie",
                       "Laptop", "Tastiera", "Mouse", "Monitor", "Webcam",
                       "Cuffie", "Webcam", "Laptop", "Mouse", "Tastiera"],
    "Città":          ["Milano", "Roma", "Torino", "Milano", "Napoli",
                       "Roma", "Milano", "Napoli", "Torino", "Roma",
                       "Milano", "Torino", "Napoli", "Milano", "Roma"],
    "Quantità":       [3, 10, 7, 2, 5, 4, 6, 8, 1, 3, 9, 2, 2, 15, 4],
    "Prezzo_Unitario":[1200, 25, 75, 350, 80, 1200, 75, 25, 350, 60,
                        80, 60, 1200, 25, 75],
}

# 1. Caricare i dati in un DataFrame.
df = pd.DataFrame(data)
print(f"\nDataFrame originale:\n{df}")

# 2. Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario.
df["Totale Vendite"] = df["Quantità"] * df["Prezzo_Unitario"]
print(f"\nAggiunta nuova colonna 'Totale Vendite':\n{df}")

# 3. Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.
prod_tot_v = df.groupby("Prodotto", as_index = False)["Totale Vendite"].sum()
print(f"\nTotale vendite per prodotto:\n{prod_tot_v}")

# 4. Trovare il prodotto più venduto in termini di Quantità.
top_seller = df.loc[df["Quantità"].idxmax(), ["Prodotto", "Quantità"]]
# .idxmax() restituisce l'indice della riga col valore massimo in "Quantità"
# .loc[indice, colonne] seleziona quelle colonne sulla riga trovata
print(f"\nProdotto più venduto:\n{top_seller.T}")

# 5. Identificare la città con il maggior volume di vendite totali.
top_city = df.loc[df["Quantità"].idxmax(), ["Città", "Quantità"]]
print(f"\nCittà con vendite più alte:\n{top_city.T}")

# 6. Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 1000 euro).
high_seller = df[df["Totale Vendite"] > 500]
print(f"\nDataFrame filtrato per 'Totale Vendite' > 500€:\n{high_seller}")

# 7.Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
df.sort_values("Totale Vendite", ascending = False, inplace = True)
print(f"\nDataFrame originale ordinato per 'Totale Vendite' discendente:\n{df}")

# 8. Visualizzare il numero di vendite per ogni città.
city_sales = df.groupby("Città", as_index = False)["Quantità"].sum()
print(f"\nQuantità di articoli venduti per Città:\n{city_sales}")
