"""
Crea una classe chiamata Punto. 
Questa classe dovrebbe avere:
- Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
- Un metodo muovi che prenda in input un valore per dx e un valore per dy e 
  modifichi le coordinate del punto di questi valori.
- Un metodo distanza_da_origine che restituisca la distanza del punto 
  dall'origine (0,0) del piano.
"""

class Punto:
    
    # definizione attributi x e y
    def __init__(self, x, y):                           # costruttore
        self.x = x
        self.y = y

    # definizione metodo .muovi() e attributi dx e dy
    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    # definizione metodo .distanza_da_origine()
    def distanza_da_origine(self):                      
        dist = (self.x**2 + self.y**2)**0.5             # calcolo distanza con Teorema di Pitagora
        return dist

# instanziazione della classe Punto
p = Punto(3, 4)
print(f"Posizione Iniziale: ({p.x}, {p.y})")

# modifica posizione con il metodo .muovi()
p.muovi(1, 2)
print(f"Dopo muovi: ({p.x}, {p.y})")

# calcolo distanza con il metodo .distanza_da_origine()
dist = p.distanza_da_origine()
print(f"Distanza dall'origine: {round(dist, 2)}")