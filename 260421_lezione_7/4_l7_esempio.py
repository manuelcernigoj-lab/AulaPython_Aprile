class Automobile:

    numero_ruote = 4                        # ATTRIBUTO DI CLASSE (accedibile dalla classe)

    def __init__(self, marca, modello):     # COSTRUTTORE
        self.marca = marca                  # ATTRIBUTO DI ISTANZA (accedibile dall'oggetto)
        self.modello = modello              # ATTRIBUTO DI ISTANZA (accedibile dall'oggetto)
    
    def stampa_info(self):
        print(f"L'automobile è una {self.marca} {self.modello}")

# instanziazione della classe Automobile
auto1 = Automobile("Nissan", "Juke")        
auto2 = Automobile("Fiat", "Panda")
auto3 = Automobile("Renault", "Zoe")

# gli attributi delle classi si possono modificare come si modificherebbe una variabile
auto1.marca = "Mercedes"
auto1.modello = "Classe A"

# chiamata al metodo per stampare le informazioni dell'auto
auto1.stampa_info()                         
auto2.stampa_info()
auto3.stampa_info()


auto1.numero_ruote = 6
print(f"numero ruote: {auto1.numero_ruote}")
print(f"numero ruote: {auto2.numero_ruote}")

Automobile.numero_ruote = 3
print(f"numero ruote auto1: {auto1.numero_ruote}")
print(f"numero ruote auto2: {auto2.numero_ruote}")