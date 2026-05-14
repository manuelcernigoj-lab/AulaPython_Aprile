import pandas as pd
import numpy as np

"""
Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario. 
"""

# DataFrame esempio, inclusi valori mancanti e duplicati
data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', 'Mario'],
    'Età': [25, 30, 16, np.nan, 85, 25, 29],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma'],
    'Salario': [1800.50, 1659.34, 856.78, 467.90, 2500.75, np.nan, 3469.65]
}
# 1.Caricare i dati in un DataFrame autogenerandoli casualmente .
df = pd.DataFrame(data)
print(f"\nDataFrame originale:\n{df}")

# 2. Visualizzare le prime e le ultime cinque righe del DataFrame.
print(f"\nPrime cinque righe del DataFrame:\n{df.head()}")
print(f"\nUltime cinque righe del DataFrame:\n{df.tail()}")

# 3. Visualizzare il tipo di dati di ciascuna colonna.
print(f"\nDataTypes di ciascuna colonna:\n{df.dtypes}")

# 4. Calcolare statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard).
print(f"\nStatistiche descrittive di base sulle colonne numeriche:\n{df.describe(include = 'number')}")

# 5. Identificare e rimuovere eventuali duplicati.
df_clean = df.drop_duplicates()
print(f"\nDataFrame pulito dopo rimozione duplicati:\n{df_clean}")

# 6. Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.
df_clean.fillna({'Età': df_clean['Età'].median(),
                 'Salario': df_clean['Salario'].median()},
                 inplace=True)
print(f"\nDataFrame pulito dopo fillna():\n{df_clean}")

# 7. Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le persone 
#    come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18 anni: Giovane, 
#    19-65 anni: Adulto, oltre 65 anni: Senior).
df_clean["Categoria Età"] = np.select([
    df_clean["Età"] <= 18,
    df_clean["Età"] > 65
    ],
    ["Giovane",
    "Senior"], 
    default="Adulto")
# np.select(condizioni, valori, default) → assegna un valore per ogni riga
# in base alla prima condizione vera; se nessuna è vera, usa default
print(f"\nDataFrame con nuova colonna 'Categoria Età':\n{df_clean}")

# 8. Salvare il DataFrame pulito in un nuovo file CSV.
df_clean.to_csv("260514_lezione_21/df_clean.csv")