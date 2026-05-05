"""
traccia: Gestore file per visita medica con accettazione postuma.
ciao utente, devi fare una visita medica? 3 scelte, a che ora alle 11 
→ aggiungi alla lista, se andro a leggere il file controlla se la visita è inserita
"""
    
FILE_PATH = "260430_lezione_14/esercizio_io/visite.csv"
ORARIO_VISITA = "09:00"

UTENTI = {
    "manuel": {"password": "1234", "nome": "Manuel",  "cognome": "Cernigoj",  "cf": "CRNMNL92B16L319I"},
    "anna":  {"password": "5678", "nome": "Anna",   "cognome": "Verdi",  "cf": "VRDNNA90B41H501X"},
}

# ---------------------------------------------------------------------

class Visita:           # Classe base per una visita medica.

    tipo = "Generica"

    # ---------------------------------------------------------------------
    def __init__(self, utente, giorno: str, orario: str):
        self.utente  = utente
        self.giorno  = giorno
        self.orario  = orario
    # ---------------------------------------------------------------------
    def descrizione(self) -> str:   # Restituisce una descrizione testuale della visita.
        return (f"{self.tipo} — {self.utente.nome} {self.utente.cognome} "
                f"(CF: {self.utente.cf}) — {self.giorno} alle {self.orario}")

    def to_csv(self) -> str:        # Restituisce la riga da salvare nel file CSV.
        return f"{self.tipo},{self.utente.nome},{self.utente.cognome},{self.utente.cf},{self.giorno},{self.orario}"
    # ---------------------------------------------------------------------

# ---------------------------------------------------------------------
class ECG(Visita):
    tipo = "ECG"

class TAC(Visita):
    tipo = "TAC"

class Oculistica(Visita):
    tipo = "Oculistica"
# ---------------------------------------------------------------------

# Mappa scelta utente → sottoclasse
TIPI_VISITA = {
    "1": ECG,
    "2": TAC,
    "3": Oculistica,
}

# ---------------------------------------------------------------------

class GestoreFile:          # Gestisce lettura e scrittura sul file CSV delle visite.

    def __init__(self,
                 path: str):
        self.path = path

    # ---------------------------------------------------------------------
    def leggi(self) -> list[str]:
        # Legge tutte le righe non vuote dal file.
        with open(self.path, "r") as f:
            return [riga.strip() for riga in f.readlines() if riga.strip()]

    def scrivi(self, riga: str) -> None:
        # Aggiunge una riga al file (append).
        with open(self.path, "a") as f:
            f.write(riga + "\n")

    def orario_occupato(self, giorno: str, orario: str) -> bool:
        # Controlla se esiste già una visita nello stesso giorno e orario.
        return any(f"{giorno},{orario}" in riga for riga in self.leggi())
    # ---------------------------------------------------------------------

class Utente:           # Rappresenta un utente autenticato.

    def __init__(self, __username: str, __nome: str, __cognome: str, __cf: str):
        self.__username = __username
        self.__nome     = __nome
        self.__cognome  = __cognome
        self.__cf       = __cf
    
    # ---------------------------------------------------------------------
    @property
    def username(self):
        return self.__username
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome
    @property
    def cf(self):
        return self.__cf
    # ---------------------------------------------------------------------
    @staticmethod
    def login() -> "Utente":
        #Chiede credenziali e restituisce un Utente se il login ha successo.
        print("\n--- Login ---")
        username = input("Username: ").strip().lower()
        password = input("Password: ").strip()

        if username in UTENTI and UTENTI[username]["password"] == password:
            dati = UTENTI[username]
            print(f"\nBenvenuto, {dati['nome']} {dati['cognome']}!")
            return Utente(username, dati["nome"], dati["cognome"], dati["cf"])
        else:
            print("Credenziali errate. Riprova.")
            return Utente.login()          # Richiede finché non è corretto
    # ---------------------------------------------------------------------

class GestoreVisite:            # Gestisce la logica di prenotazione e controllo visite.

    def __init__(self,
                 utente: Utente,
                 gestore_file: GestoreFile):
        self.utente        = utente
        self.gestore_file  = gestore_file

    # ---------------------------------------------------------------------
    def _chiedi_giorno(self) -> str:        # Chiede e valida il giorno nel formato dd/mm/yyyy.
        while True:
            giorno = input("Giorno (dd/mm/yyyy): ").strip()
            parti  = giorno.split("/")

            # Controlla formato: 3 parti, lunghezze corrette, tutti numerici
            if (len(parti) == 3
                    and len(parti[0]) == 2
                    and len(parti[1]) == 2
                    and len(parti[2]) == 4
                    and all(p.isdigit() for p in parti)):
                return giorno
            else:
                print("Formato non valido. Usa dd/mm/yyyy (es. 05/05/2025).")

    def _chiedi_orario(self) -> str:        # Chiede e valida l'orario nel formato hh:mm. 
        while True:
            orario = input("Orario (hh:mm): ").strip()
            parti  = orario.split(":")

            # Controlla formato: 2 parti, lunghezze corrette, tutti numerici
            if (len(parti) == 2
                    and len(parti[0]) == 2
                    and len(parti[1]) == 2
                    and all(p.isdigit() for p in parti)):
                return orario
            else:
                print("Formato non valido. Usa hh:mm (es. 09:30).")
    
    def _chiedi_tipo_visita(self) -> type:      # Mostra il menu dei tipi di visita e restituisce la sottoclasse scelta.
        print("\nTipo di visita:")
        print("  1. ECG")
        print("  2. TAC")
        print("  3. Oculistica")
        while True:
            scelta = input("Scegli (1/2/3): ").strip()
            if scelta in TIPI_VISITA:
                return TIPI_VISITA[scelta]
            print("Scelta non valida. Inserisci 1, 2 o 3.")

    def prenota(self) -> None:          # Aggiunge una visita per l'utente corrente. 
        TipoVisita = self._chiedi_tipo_visita()
        giorno = self._chiedi_giorno()
        orario = self._chiedi_orario()

        # Controlla se l'orario è già occupato (indipendentemente dall'utente)
        if self.gestore_file.orario_occupato(giorno, orario):
            print(f"ERRORE: L'orario {orario} del {giorno} è già occupato. Scegli un altro slot.")
            return
        
        # Crea l'istanza della sottoclasse scelta
        visita = TipoVisita(self.utente, giorno, orario)
        self.gestore_file.scrivi(visita.to_csv())
        print(f"{visita.descrizione()}")

        """ # Formato riga CSV: nome,cognome,cf,giorno,orario
        riga = f"{self.utente.nome},{self.utente.cognome},{self.utente.cf},{giorno},{orario}"
        self.gestore_file.scrivi(riga)
        print(f"Visita prenotata: {self.utente.nome} {self.utente.cognome} — {giorno} alle {orario}.") """

    def controlla(self) -> None:           # Mostra tutte le visite prenotate dall'utente corrente.
        # Controlla se l'utente ha una visita all'orario dato.
        visite = [r for r in self.gestore_file.leggi() if self.utente.cf in r]

        if visite:
            print(f"\nVisite per {self.utente.nome} {self.utente.cognome}:")
            for v in visite:
                parti = v.split(",")
                # formato CSV: tipo,nome,cognome,cf,giorno,orario
                print(f"  → {parti[0]} — {parti[4]} alle {parti[5]}")
        else:
            print("Nessuna visita trovata per il tuo profilo.")

    def menu(self) -> None:             # Loop principale del menu dopo il login.
        while True:
            print("\n--- Menu Visite ---")
            print("1. Prenota visita")
            print("2. Controlla prenotazione")
            print("3. Esci")

            scelta = input("\nScegli (1/2/3): ").strip()

            match scelta:
                case "1":
                    self.prenota()
                case "2":
                    self.controlla()
                case "3":
                    print("Arrivederci!")
                    break
                case _:
                    print("Scelta non valida. Inserisci 1, 2 o 3.")
    # ---------------------------------------------------------------------

def main():
    gestore_file   = GestoreFile(FILE_PATH)
    utente         = Utente.login()
    gestore_visite = GestoreVisite(utente, gestore_file)
    gestore_visite.menu()


if __name__ == "__main__":
    main()