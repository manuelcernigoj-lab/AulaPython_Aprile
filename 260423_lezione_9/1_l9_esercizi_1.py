"""
Estendere una classe base UnitaMilitare per creare diverse unità specializzate, 
ciascuna con compiti e metodi specifici.
Inoltre, implementare una classe ControlloMilitare che eredita da tutte le altre 
classi per gestire e tenere traccia delle diverse unità. Utilizzando tutti i metodi speciali.

    1. Classe UnitaMilitare:
        o Attributi:
            • nome (stringa): nome dell'unità.
            • numero_soldati (intero): numero di soldati nell'unità.
        o Metodi:
            • muovi(): stampa un messaggio sul movimento dell'unità.
            • attacca(): stampa un messaggio sull'attacco.
            • ritira(): gestisce il ritiro strategico.
    2. Classi Derivate:
        o Fanteria:
            • costruisci_trincea(): costruisce difese temporanee.
        o Artiglieria:
            • calibra i pezzi di artiglieria per la precisione.
        o Cavalleria:
            • esplora l'area per raccogliere informazioni sul nemico.
        o SupportoLogistico:
            • gestisce il rifornimento e la manutenzione.
        o Ricognizione :
            • conduci_ricognizione(): conduce missioni di sorveglianza.
    3. Classe ControlloMilitare:
        o Eredita da tutte le classi precedenti.
        o Attributi aggiuntivi:
            • unita_registrate: dizionario/due liste per tenere traccia delle unità create.
        o Metodi:
            • registra_unita(unita): aggiunge un unità al registro.
            • mostra_unita(): elenca tutte le unità registrate.
            • dettagli_unita(nome): mostra dettagli specifici di un ' unità.
"""
import random

# SuperClasse UnitaMiIitare: 
class UnitaMilitare:
    
    def __init__(self,                          # costruttore per UnitaMilitare
                 nome: str,                     # nome dell'UnitaMilitare
                 numero_soldati: int):          # numero_soldati dell'UnitaMilitare
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def muovi(self):                            # 
        print("\n--- MOVIMENTO ---")
        print(f"➡️  {self.numero_soldati} soldati dell'unità {self.nome} stanno marciando!")
    
    def attacca(self):                          # 
        print("\n--- ATTACCO ---")
        print(f"⚔️  {self.numero_soldati} soldati dell'unità {self.nome} attaccano le unità nemiche!")
    
    def ritira(self):                           # 
        print("\n--- RITIRATA ---")
        print(f"⬅️  {self.numero_soldati} soldati dell'unità {self.nome} si ritirano!")

    # Metodi speciali sulla classe base
    def __str__(self):
        intestazione = (
            f"{'─' * 30}\n"
            f"Classe:   {self.__class__.__name__}\n"
            f"Unità:    {self.nome}\n"
            f"Soldati:  {self.numero_soldati}\n"
            f"{'─' * 30}"
        )
        statistiche = "\n".join(
            f"{attr.replace('_', ' ').capitalize():<22} {valore}"
            for attr, valore in vars(self).items()
            if attr not in ("nome", "numero_soldati")
        )
        return f"{intestazione}\n{statistiche}"

    def __eq__(self, other):
        if not isinstance(other, UnitaMilitare):
            return NotImplemented
        return self.nome == other.nome

# SottoClasse Fanteria: 
class Fanteria(UnitaMilitare):
    
    def __init__(self,
                 nome: str,
                 numero_soldati: int,
                 attacco: int = 72,
                 difesa: int = 65,
                 punti_salute: int = 800,
                 precisione: int = 85):
        super().__init__(nome,
                         numero_soldati)
        self.attacco = attacco
        self.difesa = difesa
        self.punti_salute = punti_salute
        self.precisione = precisione
    
    def costruisci_trincea(self):                   # costruisce difese temporanee.
        print("\n--- TRINCERAMENTO ---")
        buff = random.choices([5, 10, 15, 30], [0.25, 0.4, 0.25, 0.1])[0]
        self.difesa += buff
        print(f"🪏  I fanti dell'unità {self.nome} costruiscono una trincea!")
        print(f"✅ Completato: 🛡️  Difesa + {buff:.0f} punti")
        print("📊 Statistiche aggiornate:")
        print(self)
    
# SottoClasse Artiglieria: 
class Artiglieria(UnitaMilitare):
    
    def __init__(self,
                 nome: str,
                 numero_soldati: int,
                 attacco: int = 95,
                 difesa: int = 25,
                 punti_salute: int = 500,
                 precisione: int = 60):
        super().__init__(nome,
                         numero_soldati)
        self.attacco = attacco
        self.difesa = difesa
        self.punti_salute = punti_salute
        self.precisione = precisione
    
    def calibra_artiglieria(self):                   # calibra i pezzi di artiglieria per la precisione.
        print("\n--- CALIBRAZIONE ARTIGLIERIA ---")
        print(f"⚙️  Artiglieri dell'unità {self.nome} calibrano l'artiglieria!")
        buff = random.choices([5, 10, 20, 40], [0.25, 0.4, 0.25, 0.1])[0]
        self.precisione += buff
        print(f"✅ Completato: 👁️  Precisione + {buff:.0f}%")
        print("📊 Statistiche aggiornate:")
        print(self)
        
    
# SottoClasse Cavalleria: 
class Cavalleria(UnitaMilitare):
    
    def __init__(self,
                 nome: str,
                 numero_soldati: int,
                 attacco: int = 80,
                 difesa: int = 45,
                 punti_salute: int = 700,
                 precisione: int = 55):
        super().__init__(nome,
                         numero_soldati)
        self.attacco = attacco
        self.difesa = difesa
        self.punti_salute = punti_salute
        self.precisione = precisione
    
    def esplorazione(self):                   # esplora Varea per raccogliere informazioni sul nemico.
        print("\n--- ESPLORAZIONE ---")
        print(f"🐎  {self.numero_soldati} Cavalieri dell'unità {self.nome} stanno perlustrando l'area!")
        print("Completato!\nInformazioni raccolte: ")
        unita_nemiche = random.uniform(10, 1000)
        print(f"Il nemico ha schierato {unita_nemiche:.0f} unità!")

# SottoClasse SupportoLogistico: 
class SupportoLogistico(UnitaMilitare):
    
    def __init__(self,
                 nome: str,
                 numero_soldati: int,
                 quantita_munizioni: int = 900,
                 quantita_provviste: int = 850,
                 integrita_armamenti: int = 100):
        super().__init__(nome,
                         numero_soldati)
        self.quantita_munizioni = quantita_munizioni
        self.quantita_provviste = quantita_provviste
        self.integrita_armamenti = integrita_armamenti
    
    def rifornimento(self):                   # 
        print("\n--- RIFORNIMENTO ---")
        rif = int(input("Cosa vuoi rifornire: 1. Munizioni 💣    2. Provviste 🥩"))
        if rif == 1:
            print("💣  Il Supporto Logistico ha richiesto Munizioni al campo base")
            buff = random.choices([5, 10, 25, 50], [0.25, 0.4, 0.25, 0.1])[0]
            self.quantita_munizioni += 50 * buff
            print("📦 Inventario aggiornato:")
            print(self)
            print(f"\n✅ Bonus: 🗡️ Attacco di tutte le unità + {buff:.0f} punti")
        else: 
            print("🥩  Il Supporto Logistico ha richiesto Provviste al campo base")
            buff = random.choices([50, 100, 250, 500], [0.25, 0.4, 0.25, 0.1])[0]
            self.quantita_provviste += buff
            print(f"\n✅ Bonus: ❤️ HP di tutte le unità + {buff:.0f} punti")
    
    def manutenzione(self):                   # 
        print("\n--- MANUTENZIONE ---")
        print(f"⚒️  Il Supporto Logistico sta eseguendo manutenzione sugli armamenti!")
        buff = random.choices([5, 10, 25, 50], [0.25, 0.4, 0.25, 0.1])[0]
        self.integrita_armamenti += buff
        print(f"Completato: 📶 Integrità armamenti + {buff:.0f}%")
        print("📦 Inventario aggiornato:")
        print(self)
    
# SottoClasse Ricognizione: 
class Ricognizione(UnitaMilitare):
    
    def __init__(self,
                 nome: str,
                 numero_soldati: int):
        super().__init__(nome,
                         numero_soldati)
            
    def conduci_ricognizione(self):
        print("\n--- RICOGNIZIONE ---")
        print(f"🔍 I ricognitori stanno sorvegliando l'area!")
        movimenti_nemici = random.binomialvariate(1, 0.5)
        if movimenti_nemici == 0:
            print("⚠️  Messaggio: Il nemico sta retrocedendo!")
        else:
            print("⚠️  Messaggio: Il nemico sta avanzando!")

# SottoClasse ControlloMilitare: 
class ControlloMilitare(Fanteria,
                        Artiglieria,
                        Cavalleria,
                        SupportoLogistico,
                        Ricognizione):
    
    def __init__(self,
                 nome: str = "Quartier Generale",
                 numero_soldati: int = 0):
        # Inizializza solo gli attributi della classe base
        UnitaMilitare.__init__(self, nome, numero_soldati)
        # Attributi extra di SupportoLogistico
        self.quantita_munizioni = 0
        self.quantita_provviste = 0
        self.integrita_armamenti = 1.0
        # Attributi extra di Ricognizione
        self.conoscenza_territorio = 0.0
       

    # Registro: dizionario  nome → istanza
        self.unita_registrate: dict[str, UnitaMilitare] = {}
    
    # --- Gestione registro ---
    def registra_unita(self,
                       unita: UnitaMilitare):
        # Aggiunge un'unità al registro. Sovrascrive se il nome esiste già.
        if not isinstance(unita, UnitaMilitare):
            print(f"{unita} non è un'istanza di UnitaMilitare.")
        self.unita_registrate[unita.nome] = unita
        print(f"✅  Unità '{unita.nome}' registrata con successo.")
    
    def mostra_unita(self):
        # Elenca tutte le unità registrate.
        print("\n--- UNITÀ REGISTRATE ---")
        if not self.unita_registrate:
            print("  (nessuna unità registrata)")
        for i, unita in enumerate(self.unita_registrate.values(), start=1):
            print(f"{unita}")

    def dettagli_unita(self, 
                       nome: str):
        # Mostra i dettagli completi di un'unità specifica.
        unita = self.unita_registrate.get(nome)
        if unita is None:
            print(f"⚠️  Unità '{nome}' non trovata nel registro.")
            return
        print(f"\n--- Dettagli {unita.nome} ---")
        print(str(unita))
        
        

    # --- Metodi speciali ---
    def __str__(self):
        return (f"\nControllo Militare '{self.nome}'\n"
                f"Unità registrate: {len(self.unita_registrate)}\n")

    def __len__(self):
        """Restituisce il numero di unità registrate."""
        return len(self.unita_registrate)
        
# Creazione unità
qg      = ControlloMilitare(nome="Quartier Generale", numero_soldati=10)
alpha   = Fanteria("Alpha", 150)
bravo   = Artiglieria("Bravo", 40)
charlie = Cavalleria("Charlie", 80)
delta   = SupportoLogistico("Delta", 30, quantita_munizioni=500, quantita_provviste=300)
echo    = Ricognizione("Echo", 20)

# Registrazione
for u in [alpha, bravo, charlie, delta, echo]:
    qg.registra_unita(u)

# Test mostra_unita
qg.mostra_unita()

# Test dettagli_unita (una semplice e una con attributi extra)
qg.dettagli_unita("Alpha")
qg.dettagli_unita("Delta")

# Test __str__
print(str(qg))

# Test __len__
print(f"Unità totali: {len(qg)}")

# Test __eq__
alpha2 = Fanteria("Alpha", 999)
print(f"Alpha == Alpha2 (stesso nome, soldati diversi): {alpha == alpha2}")
print(f"Alpha == Bravo: {alpha == bravo}")

# Test azioni
alpha.costruisci_trincea()
bravo.calibra_artiglieria()
charlie.esplorazione()
delta.manutenzione()
echo.conduci_ricognizione()

# Test metodi base ereditati da UnitaMilitare
alpha.muovi()
bravo.attacca()
charlie.ritira()