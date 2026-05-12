import numpy as np

# 1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
arr = np.linspace(0, 1, 12)
print(f"1. Array di 12 numeri equidistanti tra 0 e 1:\n{arr}")

# 2. Cambia la forma dell'array a una matrice 3x4.
m_3x4 = arr.reshape(3,4)
print(f"\n2. Array precedente trasformato in matrice 3x4:\n{m_3x4}")

# 3. Genera una matrice 3x4 di numeri casuali tra 0 e 1.
np.random.seed(42)
rand_3x4 = np.random.random(size = (3,4))
print(f"\n3. Matrice di numeri casuali tra 0 e 1:\n{rand_3x4}")

# 4. Calcola e stampa la somma degli elementi di entrambe le matrici.
m_3x4_sum = round(np.sum(m_3x4), 2)
rand_3x4_sum = round(np.sum(rand_3x4), 2)
print("\n4. Somma dei numeri delle matrici precendeti:")
print(f"Matrice n equidistanti: {m_3x4_sum}\nMatrice n random: {rand_3x4_sum}")
