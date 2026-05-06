"""
1. Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
2. Verifica il tipo di dato dell'array e stampa il risultato.
3. Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
4. Stampa la forma dell'array.
(EXTRA) Esporta in txt o csv
"""

import numpy as np

ints = np.arange(10, 50)            # creazione ndarray
print(ints.dtype)                   # print dtype
print(ints)                         # print ndarray
floats = ints.astype(np.float64)    # int → float conversion
print(floats.dtype)                 # print new dtype 
print(floats.shape)                 # print

# export ints in formato .txt
np.savetxt(
    "260506_lezione_16/ints.txt",   # percorso e nome del file di output
    ints,                           # array da salvare
    fmt="%d"                        # formato: intero (d = digit)
)

# export floats in formato .csv
np.savetxt(
    "260506_lezione_16/floats.csv",  # percorso e nome del file di output
    floats,                          # array da salvare
    delimiter=",",                   # separatore tra valori (standard CSV)
    fmt="%.1f"                       # formato: decimale con una cifra
)