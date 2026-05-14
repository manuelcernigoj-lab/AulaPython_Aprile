"""
Sistema interattivo per la gestione di matrici 2D con NumPy.
Struttura modulare: ogni operazione è una funzione richiamabile singolarmente.
 
Parti:
    - Parte 1 : operazioni base (creazione, sotto-matrice, trasposizione, somma)
    - Parte 2 : moltiplicazione element-wise, media, determinante (EXTRA)
    - Parte 3 : inversa, funzione matematica, filtro per condizione
"""
#   --- IMPORT & SETUP ---
# ----------------------------
import numpy as np
import os
from datetime import datetime as dt
# ----------------------------

def salva_risultato(operazione: str, risultato):
    time = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("260513_lezione_20/risultati.txt", "a") as f:
        f.write(f"\n[{time}] — {operazione}\n")
        f.write(f"{risultato}\n")
        f.write("-" * 40 + "\n")
    
    print("Risultato salvato su 'risultati.txt'")

class Matrix:
    
    def __init__(self, righe: int, colonne: int):
        self.mat = np.random.randint(0, 101, size = (righe, colonne))
    
    def submatrix(self):
        r, c = self.mat.shape
        # Indici del blocco centrale
        r_start, r_end = r // 4, 3 * r // 4
        c_start, c_end = c // 4, 3 * c // 4

        # Cntrollo: evita sottomatrice vuota
        if r_end <= r_start or c_end <= c_start:
            print("ERRORE: matrice troppo piccola per estrarre un blocco centrale.")
            return None

        return self.mat[r_start:r_end, c_start:c_end]

    def transpose(self):
        return self.mat.T
    
    def mat_sum(self):
        return np.sum(self.mat)
    
    def elementwise_mult(self):
        self.mat2 = np.random.randint(0, 101, size = self.mat.shape)
        return self.mat * self.mat2
    
    def mat_mean(self):
        return np.mean(self.mat)
    
    def mat_det(self):
        r, c = self.mat.shape
        if r != c:
            print(f"ERRORE: Matrice {r} x {c}: il determinante esiste solo per matrici quadrate.")
            return None
        
        return np.linalg.det(self.mat)
    
    def mat_inv(self):
        r, c = self.mat.shape
        if r != c:
            print("ERRORE: serve una matrice quadrata.")
            return None
    
        det = np.linalg.det(self.mat)
        if np.isclose(det, 0):
            # isclose controlla se det è "quasi zero"
            # utile perché i float hanno errori di arrotondamento 
            # (es. 0.000000000001 invece di 0)
            print("ERRORE: determinante = 0, matrice non invertibile.")
            return None
    
        return np.linalg.inv(self.mat)
    
    def apply_func(self, func_name: str):
        funzioni = {
        "sin":  np.sin,
        "cos":  np.cos,
        "exp":  np.exp
        }
        if func_name not in funzioni:
            print(f"ERRORE: funzione '{func_name}' non riconosciuta.")
            return None
    
        return funzioni[func_name](self.mat)

    def filter_elements(self, soglia: float):
        # Restituisce solo i valori che superano la soglia (come array 1D)
        return self.mat[self.mat > soglia]


def menu():
    mat = None          # matrice non ancora creata

    while True:
        print("""
------------------------------------
|         MENU MATRICE NUMPY       |
|----------------------------------|
|  1. Crea nuova matrice           |
|  2. Sottomatrice centrale        |
|  3. Trasposta                    |
|  4. Somma elementi               |
|  5. Moltiplicazione element-wise |
|  6. Media elementi               |
|  7. Determinante                 |
|  8. Matrice inversa              |
|  9. Applica funzione matematica  |
| 10. Filtra elementi              |
|  0. Esci                         |
------------------------------------""")
        
        scelta = int(input("  Scegli opzione: ").strip())

        # --- Caso speciale: matrice non ancora creata ---
        if scelta != 1 and scelta != 0 and mat is None:
            print("ERRORE: Prima crea una matrice (opzione 1).")
            continue

        match scelta:
            case 1:
                r = int(input("  Righe: "))
                c = int(input("  Colonne: "))
                mat = Matrix(r, c)
                print(f"\n  Matrice creata ({r}x{c}):\n{mat.mat}")
                salva_risultato("Nuova matrice", mat.mat)
            case 2:
                sub = mat.submatrix()
                if sub is not None:
                    print(f"\n  Sottomatrice centrale:\n{sub}")
                    salva_risultato("Sottomatrice centrale", sub)
            case 3:
                t = mat.transpose()
                print(f"\n  Trasposta:\n{t}")
                salva_risultato("Trasposta", t)
            case 4:
                s = mat.mat_sum()
                print(f"\n  Somma elementi: {s}")
                salva_risultato("Somma elementi", s)
            case 5:
                res = mat.elementwise_mult()
                print(f"\n  Matrice 2 (casuale):\n{mat.mat2}")
                print(f"\n  Risultato element-wise:\n{res}")
                salva_risultato("Moltiplicazione element-wise", res)
            case 6:
                m = mat.mat_mean()
                print(f"\n  Media elementi: {m:.4f}")
                salva_risultato("Media elementi", m)
            case 7:
                det = mat.mat_det()
                if det is not None:
                    print(f"\n  Determinante: {det:.4f}")
                    salva_risultato("Determinante", det)
            case 8:
                inv = mat.mat_inverse()
                if inv is not None:
                    print(f"\n  Matrice inversa:\n{inv}")
                    salva_risultato("Matrice inversa", inv)
            case 9:
                print("  Funzioni disponibili: sin, cos, exp, sqrt, log")
                fname = input("  Scegli funzione: ").strip().lower()
                res = mat.apply_func(fname)
                if res is not None:
                    print(f"\n  Risultato {fname}:\n{res}")
                    salva_risultato(f"Funzione {fname}", res)
            case 10:
                soglia = float(input("  Valore soglia (mostra elementi >): "))
                res = mat.filter_elements(soglia)
                print(f"\n  Elementi > {soglia}: {res}")
                salva_risultato(f"Filtro > {soglia}", res)
            case 0:
                print("  Uscita. Arrivederci!")
                break
            case _:
                print("ERRORE: Opzione non valida.")


if __name__ == "__main__":
    menu()