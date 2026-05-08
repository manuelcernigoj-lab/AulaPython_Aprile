# --- Modulo Main: Gestore, menu e avvio ---

import csv
import os
from ricette import Ricetta

# --- Gestore ---
class GestoreRicette:

    def __init__(self):
        self.ricette = []           # lista di oggetti Ricetta
        self.file_path = None       # inizializzazione del path
        self.carica()               # carica subito da file

    # --- I/O ---
    def carica(self):
        # --- Percorso cartella Ricette (relativo allo script) ---
        # IMPORTANTE: os.path.dirname(__file__) restituisce la cartella dove si trova lo script corrente
        #             così il path funziona indipendentememte dalla posizione da cui si lancia lo script
        cartella = os.path.join(os.path.dirname(__file__), "Ricette")

        # --- Lista file presenti ---
        try:
            files = os.listdir(cartella)    # lista dei file presenti (ricette)
        except FileNotFoundError:
            os.makedirs(cartella)           # crea automaticamente la cartella
            files = []                      # cartella appena creata → sicuramente vuota, niente da listare

        if not files:
            print("Nessun file trovato nella cartella.")
            nome_file = input("Nome nuovo file (es. ricette_maggio.csv o ricette_maggio.txt): ").strip()
            self.file_path = os.path.join(cartella, nome_file)
            print(f"Nuovo file '{nome_file}' verrà creato al primo salvataggio.")
            return

        # --- Mostra file disponibili ---
        print("\nBenvenuto nel sistema: GESTIONE RICETTE")
        print("-" * 40)
        print("\nFile disponibili:")
        for i, f in enumerate(files, start=1):
            print(f"  {i}. {f}")
        print("  0. Crea nuovo file")

        # --- Scelta utente ---
        while True:
            scelta = input("\nScegli numero file (0 per nuovo): ").strip()

            if scelta == "0":
                nome_file = input("Nome nuovo file (es. ricette_maggio.csv o ricette_maggio.txt): ").strip()
                self.file_path = os.path.join(cartella, nome_file)
                print(f"Nuovo file '{nome_file}' verrà creato al primo salvataggio.")
                return
            
        # --- Validazione scelta ---
            try:
                indice = int(scelta) - 1
                nome_file = files[indice]
                break                           # scelta valida → esci dal loop
            except (ValueError, IndexError):
                print("Scelta non valida, riprova.")
                continue                        # torna all'inizio del while

        # self.file_path salvato come attributo perché salva() ne avrà bisogno 
        self.file_path = os.path.join(cartella, nome_file)
        estensione = nome_file.split(".")[-1]

        # --- Lettura CSV ---
        if estensione == "csv":
            try:
                with open(self.file_path, "r", newline = "", encoding = "utf-8") as f:
                    reader = csv.DictReader(f)
                    for riga in reader:
                        self.ricette.append(Ricetta.from_dict(riga))
                print(f"Caricate {len(self.ricette)} ricette da '{nome_file}'.")
            except FileNotFoundError:
                print("File non trovato. Partenza con lista vuota.")

        # --- Lettura TXT ---
        elif estensione == "txt":
            try:
                with open(self.file_path, "r", encoding = "utf-8") as f:
                    next(f)     # ← salta intestazione
                    for riga in f:
                        riga = riga.strip()
                        if not riga:        # salta righe vuote
                            continue
                        parti = riga.split("|")     # separatore arbitrario
                        d = {
                            "id":               parti[0],
                            "nome_paziente":    parti[1],
                            "cognome_paziente": parti[2],
                            "farmaco":          parti[3],
                            "dose":             parti[4]
                        }
                        self.ricette.append(Ricetta.from_dict(d))
                print(f"Caricate {len(self.ricette)} ricette da '{nome_file}'.")
            except FileNotFoundError:
                print("File non trovato. Partenza con lista vuota.")

        else:
            print(f"Formato '.{estensione}' non supportato. Partenza con lista vuota.")
        

    def salva(self):
        
        # recupera estensione del file
        estensione = self.file_path.split(".")[-1]

        # apri file con csv.DictWriter, scrivi i campi + tutte le righe
        if estensione == "csv":
            with open(self.file_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "nome_paziente", "cognome_paziente", "farmaco", "dose"])
                writer.writeheader()
                for r in self.ricette:
                    writer.writerow(r.to_dict())

        # apri file con come txt, scrivi i campi + tutte le righe usa '|' come separatore arbitrario
        elif estensione == "txt":
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write("id|nome_paziente|cognome_paziente|farmaco|dose\n")  # ← intestazione
                for r in self.ricette:
                    f.write(f"{r.id}|{r.nome_paziente}|{r.cognome_paziente}|{r.farmaco}|{r.dose}\n")

        print("Salvataggio completato.")

    # --- CRUD ---

    def visualizza(self):
        # se lista vuota stampa avviso, altrimenti stampa ogni ricetta
        if not self.ricette:
            print("Nessuna ricetta presente.")
            return
        print("\n--- Ricette ---")
        for r in self.ricette:
            print(r)

    def aggiungi(self):
        # chiedi input, genera nuovo id, crea Ricetta, appendi, salva
        print("\n--- Nuova ricetta ---")
        nome     = input("Nome paziente: ").strip()
        cognome  = input("Cognome paziente: ").strip()
        farmaco  = input("Farmaco: ").strip()
        dose     = input("Dose: ").strip()

        nuova = Ricetta(
            id               = self._nuovo_id(),
            nome_paziente    = nome,
            cognome_paziente = cognome,
            farmaco          = farmaco,
            dose             = dose
        )
        self.ricette.append(nuova)
        self.salva()
        print(f"Ricetta aggiunta con ID {nuova.id}.")

    def modifica(self):
        # chiedi id, cerca con filter(), aggiorna campi, salva
        self.visualizza()
        if not self.ricette:
            return

        try:
            id_cerca = int(input("\nID ricetta da modificare: ").strip())
        except ValueError:
            print("ID non valido.")
            return

        ricetta = None
        for r in self.ricette:
            if r.id == id_cerca:
                ricetta = r
                break        # si ferma al primo trovato
        
        if not ricetta:
            print(f"Nessuna ricetta con ID {id_cerca}.")
            return

        print("Lascia vuoto per mantenere il valore attuale.")
        nome    = input(f"Nome ({ricetta.nome_paziente}): ").strip()
        cognome = input(f"Cognome ({ricetta.cognome_paziente}): ").strip()
        farmaco = input(f"Farmaco ({ricetta.farmaco}): ").strip()
        dose = input(f"Dose ({ricetta.dose}): ").strip()

        if nome:    ricetta.nome_paziente    = nome
        if cognome: ricetta.cognome_paziente = cognome
        if farmaco: ricetta.farmaco          = farmaco
        if dose:    ricetta.dose             = dose

        self.salva()
        print("Ricetta modificata.")

    def elimina(self):
        # chiedi id, rimuovi con list comprehension, salva
        self.visualizza()
        if not self.ricette:
            return

        try:
            id_cerca = int(input("\nID ricetta da eliminare: ").strip())
        except ValueError:
            print("ID non valido.")
            return

        originale = len(self.ricette)
        self.ricette = [r for r in self.ricette if r.id != id_cerca]

        if len(self.ricette) < originale:
            self.salva()
            print(f"Ricetta {id_cerca} eliminata.")
        else:
            print(f"Nessuna ricetta con ID {id_cerca}.")

    # --- Gestione degli ID ---
    def _nuovo_id(self):
        # ritorna max(id esistenti) + 1  oppure 1 se lista vuota
        if not self.ricette:
            return 1
        return max(r.id for r in self.ricette) + 1

# --- Menu ---

MENU = """
--------------------------------
|        Gestione Ricette       |
--------------------------------
|  1. Visualizza ricette        |
|  2. Aggiungi ricetta          |
|  3. Modifica ricetta          |
|  4. Elimina ricetta           |
|  5. Salva ed esci             |
--------------------------------
"""

def menu():
    # stampa opzioni 1-5, ritorna la scelta dell'utente
    print(MENU)
    return input("Scelta: ").strip()


# --- Avvio ---
if __name__ == "__main__":
    gestore = GestoreRicette()

    while True:
        scelta = menu()

        match scelta:
            case "1":
                gestore.visualizza()
            case "2":
                gestore.aggiungi()
            case "3":
                gestore.modifica()
            case "4":
                gestore.elimina()
            case "5":
                print("Arrivederci.")
                break
            case _:
                print("Scelta non valida.")