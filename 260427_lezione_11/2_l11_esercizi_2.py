"""
Andiamo a creare un sistema ripetibile che simuli un teatro:

Classe Base: Posto
    - Attributi privati:
        - _numero (intero): il numero del posto.
        - _fila (stringa): la fila in cui si trova il posto.
        - _occupato (booleano): stato del posto, se è occupato (True) o libero (False).
    - Metodi:
        - __init__(numero, fila): inizializza il posto impostando _occupato a False.
        - prenota(): prenota il posto se non è già occupato; in caso contrario, 
          segnala che il posto è già occupato.
        - libera(): libera il posto se è occupato; altrimenti segnala che il posto non 
          era prenotato.
        - Getter: per recuperare il numero, la fila e lo stato (occupato/libero).
Classi Derivate
- PostoVIP:
    - Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come 
      “Accesso al lounge”, “Servizio in posto”).
    - Metodi:
        - Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, 
          l'attivazione dei servizi extra.
- PostoStandard:
    - Attributi aggiuntivi: costo (un valore numerico che rappresenta il costo della 
      prenotazione, ad esempio per prenotazione online).
    - Metodi:
        - Può sovrascrivere prenota() per includere la visualizzazione del costo o altre 
          particolarità della prenotazione.
Classe Teatro
    - Attributi:
        - _posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
    - Metodi:
        - aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
        - prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero 
          e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
        - stampa_posti_occupati(): stampa tutti i posti che risultano occupati.

→ l'esercizio deve essere ripetibile (while)
"""

class Posto:
    
    # --- init ---
    def __init__(self,
                 _numero: int,
                 _fila: str,
                 _occupato: bool = False):
        self._numero = _numero
        self._fila = _fila
        self._occupato = _occupato

    # --- definizione dei Getter ---
    @property
    def numero(self):
        return self._numero
    @property
    def fila(self):
        return self._fila
    @property
    def occupato(self):
        return self._occupato
    
    # --- prenotazione ---
    def prenota(self):
        if self._occupato == False:
           print(f"Posto {self._fila}{self._numero} occupato.")
        else:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato.")
    
    # --- libera posto ---
    def libera(self):
        if self._occupato == False:
           print(f"Posto {self._fila}{self._numero} non era prenotato.")
        else:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} liberato.")
    
    # --- tipo posto ---
    def tipo(self):
        return "Posto"


class PostoVIP(Posto):
    
    def __init__(self, 
                 _numero: int, 
                 _fila: str, 
                 _occupato: bool = False,
                 _servizi_extra: list = [],
                 _costo: float = 0.0):
        super().__init__(_numero,
                         _fila,
                         _occupato)
        self._servizi_extra = _servizi_extra
        self._costo = _costo

    # --- prenotazione → override ---
    def prenota(self):
        if self._occupato == False:
           print(f"Posto VIP {self._fila}{self._numero} occupato.")
        else:
            self._occupato = True
            servizi = ", ".join(self._servizi_extra)
            print(f"Posto VIP {self._fila}{self._numero} prenotato.\nServizi: {servizi}\nCosto: €{self._costo:.2f}")            

    # --- tipo posto ---
    def tipo(self):
        return "VIP"

class PostoStandard(Posto):
    
    def __init__(self, 
                 _numero: int, 
                 _fila: str, 
                 _occupato: bool = False,
                 _costo: float = 0.0):
        super().__init__(_numero,
                         _fila,
                         _occupato)
        self._costo = _costo
    
    # --- prenotazione → override ---
    def prenota(self):
        if self._occupato == False:
           print(f"Posto Standard {self._fila}{self._numero} occupato.")
        else:
            self._occupato = True
            print(f"Posto Standard {self._fila}{self._numero} prenotato.\nCosto: €{self._costo:.2f}")

    # --- tipo posto ---
    def tipo(self):
        return "Standard"

class Teatro():
    
    def __init__(self):
        self._posti = []

    # --- aggiungi posto ---
    def aggiungi_posto(self,
                       posto: Posto):
        self._posti.append(posto)
    
    # --- prenota posto ---
    def prenota_posto(self,
                      numero: int,
                      fila: str):
        for posto in self._posti:
            if posto.numero == numero and posto.fila == fila:
                posto.prenota()
                return
            else:
                print(f"Posto {fila}{numero} non trovato")

    # --- libera posto ---
    def libera_posto(self,
                      numero: int,
                      fila: str):
        for posto in self._posti:
            if posto.numero == numero and posto.fila == fila:
                posto.libera()
                return
            else:
                print(f"Posto {fila}{numero} non trovato")
    
    # --- visualizza posti occupati ---
    def stampa_posti_occupati(self):
        occupati = [o for o in self._posti if o.occupato]
        if not occupati:
            print("\nNessun posto occupato.")
        else:
            for o in occupati:
                print(f"[{o.tioo()}] Fila {o.fila} - Posto {o.numero}")


# --- setup teatro ---
teatro = Teatro()

# Aggiungi posti VIP (fila A)
for n in range(1, 4):
    teatro.aggiungi_posto(
        PostoVIP(n,
                 "A",
                 ["Accesso al lounge", "Servizio in posto"],
                 costo = 20.50)
    )

# Aggiungi posti Standard (fila B e C)
for fila in ["B", "C"]:
    for n in range(1, 6):
        teatro.aggiungi_posto(PostoStandard(n,
                                            fila,
                                            costo = 8.50))

# --- MENU ---

MENU = """
--------------------------------
         TEATRO - MENU         
--------------------------------
   1. Prenota posto            
   2. Libera posto             
   3. Posti occupati           
   0. Esci                     
--------------------------------
"""

while True:
    print(MENU)
    scelta = int(input("Scelta: "))

    match scelta:
        case 1:
            fila   = input("  Fila (A/B/C): ").strip().upper()
            numero = int(input("  Numero posto: ").strip())
            teatro.prenota_posto(numero, fila)
        case 2:
            fila   = input("  Fila (A/B/C): ").strip().upper()
            numero = int(input("  Numero posto: ").strip())
            teatro.libera_posto(numero, fila)
        case 3:
            print("\n  Posti occupati:")
            teatro.stampa_posti_occupati()
        case 0:
            print("  Arrivederci!")
            break
        case _:
            print("  Scelta non valida.")



"""
def prenota(self):
        if self._occupato == False:
           print(f"Posto {self._fila}{self._numero} occupato.")
        else:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato.")
            print("Vuoi aggiungere dei servizi VIP? y / n")
            scelta = str(input()).lower()
            match scelta:
                case "n":
                    print("Hai scelto di non aggiungere servizi VIP")
                case "y":
                    print("Seleziona il servizio:")
                    servizio = int(input("1. Popcorn | 2. Bibita"))
                    match servizio:
                        case 1:
                            print("Aggiunto servizio: Popcorn")
                        case 2:
                            print("Aggiunto servizio: Bibita")
                        case _:
                            print(f"Scelta non valida: {servizio}")
                            return
                case _:
                    print(f"Scelta non valida: {scelta}")
                    return
"""