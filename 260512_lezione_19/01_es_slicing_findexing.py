import numpy as np

"""
1. Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri 
   interi casuali compresi tra 1 e 100.
2. Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
3. Inverti le righe della matrice estratta (cioè, la prima riga 
   diventa l'ultima, la seconda diventa la penultima, e così via).
4. Estrai la diagonale principale della matrice invertita e crea un 
   array 1D contenente questi elementi.
5. Sostituisci tutti gli elementi della matrice invertita che sono 
   multipli di 3 con il valore -1.
6. Stampa la matrice originale, la sotto-matrice centrale estratta, la 
   matrice invertita, la diagonale principale e la matrice invertita 
   modificata.
"""

# 1.
m_6x6 = np.random.randint(1, 101, size = (6, 6))
print(f"Matrice 6 x 6 con numeri tra 1 e 100:\n{m_6x6}")

# 2.
m_4x4 = m_6x6[1:5, 1:5]
print(f"\nSotto-matrice centrale 4 x 4 della precedente:\n{m_4x4}")

# 3.
indices = np.array([5, 4, 3, 2, 1, 0])      # indici corrispondenti alle righe invertite
m_6x6_inv = m_6x6[indices]      # creazione matrice invertita
print(f"\nMatrice 6 x 6 iniziale con righe in ordine inverso:\n{m_6x6_inv}")

# 4.
# creazione delle liste contenenti gli indici delle righe e delle colonne
r = np.array([0, 1, 2, 3, 4, 5])
c = np.array([0, 1, 2, 3, 4, 5])
arr = m_6x6_inv[r, c]      # estrazione diagonale e salvataggio in variabile arr
print(f"\nArray 6 x 1 corrispondente alla diagonale principale della matrice 6 x 6:\n{arr}")

# 5.
m_6x6_r = m_6x6_inv.copy()
m_6x6_r[m_6x6_inv % 3 == 0] = -1
print(f"\nMatrice 6 x 6 invertita con multipli di 3 rimpiazzati a '-1':\n{m_6x6_r}")