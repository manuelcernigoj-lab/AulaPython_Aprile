""" 
1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
2. Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
3. Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
4. Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
5. Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
6. Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) 
   assegnando loro il valore 99.
7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
BONUS scrivere su .csv

Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare 
sottoarray specifici da un array più grande.
"""

import numpy as np

# 1. Array di 20 interi casuali [10, 50]
nums = np.random.randint(10, 51, 20)        # uso randint(start, stop(escluso), step)
print("Array originale:       ", nums)

# 2. Estrazione primi 10 elementi dell'array
first10 = nums[:10]
print("Primi 10:              ", first10)

# 3. Estrazione ultimi 5 elementi dell'array
last5 = nums[-5:]       # gli indici negativi partono da -1
print("Ultimi 5:              ", last5)

# 4. Estrazione elementi dall'indice 5 all'indice 15 (escluso)
nums5_14 = nums[5:15]
print("Indice 5-15 (escluso): ", nums5_14)

# 5. Estrazione ogni terzo elemento dell'array
every3 = nums[::3]      # utilizzo solo step = 3
print("Ogni terzo elemento:   ", every3)

# 6. Modifica elementi indice 5 → 10 (escluso) assegnando 99.
nums_m = nums.copy()
nums_m[5:10] = 99         # assegnazione tramite slice
print("Array dopo modifica:   ", nums_m)


# --- BONUS ---

# salvataggio su .txt
np.savetxt("260506_lezione_16/slicing_results.txt",     # path 
           nums,                                        # ndarray
           # separa i valori sulla stessa riga — ma se hai un array 1D, ogni elemento va su una riga propria
           delimiter = ",",                             # delimitatore
           fmt = "%d")                                  # formattazione
#salvataggio su .csv

import csv

# creazione lista righe
rows = [
    ("Array originale (post-modifica)", nums),
    ("Primi 10",                        first10),
    ("Ultimi 5",                        last5),
    ("Indice 5-15",                     nums5_14),
    ("Ogni terzo elemento",             every3),
]

# salvataggio su .csv
with open("260506_lezione_16/slicing_results.csv",      # path
          "w",                                          # metodo
          newline=""                                    # evita righe vuote extra
          ) as f:                                       # alias
    writer = csv.writer(f)                              # metodo writer salvato in variabile
    writer.writerow(["label", "valori"])                # writer di intestazione
    for label, arr in rows:                             # iteratore per spacchettare le tuple in label e array
        writer.writerow([label, arr.tolist()])          # writer riga per riga