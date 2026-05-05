"""
--- Esercizio 3 ---
Creare una classe base MembroSquadra e una Squadra che conterrà le diverse 
classi figlie che rappresentano ruoli specifici all' interno della squadra 
di calcio, come Giocatore, Allenatore, e Assistente. 
Utilizzando tutti i metodi speciali.

Classe MembroSquadra:

  • Attributi:
    o nome (stringa)
    o età (intero)
  • Metodi:
    o descrivi() (stampa una descrizione generale del membro della squadra)
    o Classi Derivate:

Giocatore:
  • Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
  • Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
Allenatore :
  • Attributi aggiuntivi come anni_di_esperienza
  • Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
Assistente :
  • Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
  • Metodi specifici del ruolo, come supporta_team() che può descrivere varie 
    forme di supporto al team 

Crea due squadre e falle giocare contro.
"""

import random

# SuperClasse MembroSquadra: Rappresenta un membro generico della squadra di calcio.
class MembroSquadra:
    
    def __init__(self,                          # costruttore per MembroSquadra
                 nome: str,                     # nome dell'allenatore
                 eta: int):                     # eta del MembroSquadra
        self.nome = nome
        self.eta = eta
        
    def descrivi(self):                         # stampa una descrizione generale del membro della squadra
        print("\n--- SCHEDA MEMBRO ---")
        print(f"Membro squadra: {self.nome}, età: {self.eta} anni.")     

# SottoClasse Giocatore: Giocatore con ruolo e numero di maglia.
class Giocatore(MembroSquadra):
    
    def __init__(self,
                 nome: str,
                 eta: int,
                 ruolo: str,
                 numero_maglia: int):
        super().__init__(nome,
                         eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        self.stanchezza: int = 0
    
    def gioca_partita(self):
        
        print("\n--- CONVOCAZIONE PARTITA ---")
        # Tenta di giocare. Restituisce True se riesce, False se è stanco.
        if self.stanchezza == 0:        
            self.stanchezza += 1        
            print(f"  ⚽ {self.nome} ({self.ruolo}) gioca la partita!")
            return True
        else:
            print(f"  😓 {self.nome} è stanco e non può giocare.")
            return False
    
    def riposo(self):
        print("\n--- RIPOSO ---")
        if self.stanchezza == 0:
            print(f"  💤 {self.nome} non ha bisogno di riposarsi.")
        else:
            self.stanchezza -= 1
            print(f"  💪🏻 {self.nome} si è riposato ed è pronto.")
    
    def descrivi(self):
        print("\n--- SCHEDA GIOCATORE ---")
        print(f"Giocatore: {self.nome}\nRuolo: {self.ruolo}\nMaglia: #{self.numero_maglia}\nEtà: {self.eta}")

# SottoClasse Allenatore: Allenatore della squadra.
class Allenatore(MembroSquadra):
    
    def __init__(self,
                 nome: str,
                 eta: int,
                 anni_di_esperienza: int,
                 schema_di_gioco: str):
        super().__init__(nome,
                         eta)
        self.anni_di_esperienza = anni_di_esperienza
        self.schema_di_gioco = schema_di_gioco
 
    def dirige_allenamento(self):
        print("\n--- INIZIO ALLENAMENTO ---")
        print(f"  📋 {self.nome} allena la squadra sullo schema {self.schema_di_gioco}.")
 
    def descrivi(self):
        print("\n--- SCHEDA ALLENATORE ---")
        print(f"Allenatore: {self.nome}\nSchema preferito: {self.schema_di_gioco}\nEsperienza: {self.anni_di_esperienza} anni")
    
# SottoClasse Assistente: Membro dello staff con specializzazione.
class Assistente(MembroSquadra):
    
    def __init__(self,
                 nome: str,
                 eta: int,
                 specializzazione: str):
        super().__init__(nome,
                         eta)
        self.specializzazione = specializzazione
 
    def supporta_team(self):
        print("\n--- LA SQUADRA HA BISOGNO DI SUPPORTO ---")
        print(f"  🩺 {self.nome} ({self.specializzazione}) supporta la squadra.")
 
    def descrivi(self):
        print("\n--- SCHEDA ASSISTENTE ---")
        print(f"Assistente: {self.nome}\nSpecializzazione: {self.specializzazione}\nEtà: {self.eta}")

# Classe Squadra: Contiene giocatori, un allenatore e assistenti.
class Squadra:
     
    def __init__(self,
                 nome: str):
        self.nome = nome
        self.giocatori: list[Giocatore] = []
        self.allenatore: Allenatore | None = None
        self.assistenti: list[Assistente] = []
        self.punteggio: int = 0
    
     # --- gestione membri ---
    def aggiungi_giocatore(self,
                           g: Giocatore):
        self.giocatori.append(g)
 
    def aggiungi_allenatore(self,
                            a: Allenatore):
        self.allenatore = a
 
    def aggiungi_assistente(self,
                            a: Assistente):
        self.assistenti.append(a)
    
    def allenati(self):
        if self.allenatore:
            self.allenatore.dirige_allenamento()
        for g in self.giocatori:
            g.riposo()
    
    # --- metodi di gioco ---

    # Sceglie un giocatore casuale e gli fa tentare un'azione.
    def tentativo_gol(self):
        attaccanti = [g for g in self.giocatori if g.ruolo == "attaccante"]
        candidati = attaccanti if attaccanti else self.giocatori
        giocatore = random.choice(candidati)
        ha_giocato = giocatore.gioca_partita()
        if ha_giocato and random.random() < 0.45:   # 45% di conversione in gol
            print(f"    🥅 GOL di {giocatore.nome}!")
            self.punteggio += 1
            return True
        return False
    
    def presenta_rosa(self):
        totale = len(self.giocatori) + (1 if self.allenatore else 0) + len(self.assistenti)
        print(f"\n{'='*50}")
        print(f"  ROSA: {self.nome}  (tot. membri: {totale})")
        print(f"{'='*50}")
        if self.allenatore:
            self.allenatore.descrivi()
        for g in self.giocatori:
            g.descrivi()
        for a in self.assistenti:
            a.descrivi()

# --- partita ---

# Simula una partita tra due squadre. Ogni turno entrambe le squadre tentano un'azione offensiva.
def gioca_partita(squadra_a: Squadra,
                  squadra_b: Squadra,
                  turni: int = 6):
    
    squadra_a.punteggio = 0
    squadra_b.punteggio = 0
 
    print(f"\n{'='*50}")
    print(f"  😮‍💨 FISCHIO D'INIZIO: {squadra_a.nome} vs {squadra_b.nome}")
    print(f"{'='*50}\n")
 
    for turno in range(1, turni + 1):
        print(f"--- Turno {turno} ---")
        squadra_a.tentativo_gol()
        squadra_b.tentativo_gol()
        print(f"  Parziale: {squadra_a.nome} {squadra_a.punteggio} - {squadra_b.punteggio} {squadra_b.nome}\n")
 
    print(f"{'='*50}")
    print(f"  RISULTATO FINALE")
    print(f"  {squadra_a.nome} {squadra_a.punteggio} - {squadra_b.punteggio} {squadra_b.nome}")
    if squadra_a.punteggio > squadra_b.punteggio:
        print(f"  🏆 Vince {squadra_a.nome}!")
    elif squadra_b.punteggio > squadra_a.punteggio:
        print(f"  🏆 Vince {squadra_b.nome}!")
    else:
        print("  🤝 Pareggio!")
    print(f"{'='*50}\n")

# --- TESTS ---

# --- Costruzione Squadra A ---
inter = Squadra("Inter")
inter.aggiungi_allenatore(Allenatore("Inzaghi", 48, 10, "3-5-2"))
inter.aggiungi_giocatore(Giocatore("Lautaro", 26, "attaccante", 10))
inter.aggiungi_giocatore(Giocatore("Thuram",  27, "attaccante",  9))
inter.aggiungi_giocatore(Giocatore("Bastoni", 25, "difensore",  95))
inter.aggiungi_assistente(Assistente("Ferrara", 38, "fisioterapista"))
 
# --- Costruzione Squadra B ---
milan = Squadra("Milan")
milan.aggiungi_allenatore(Allenatore("Fonseca", 51, 15, "4-3-3"))
milan.aggiungi_giocatore(Giocatore("Leao",     25, "attaccante", 10))
milan.aggiungi_giocatore(Giocatore("Morata",   32, "attaccante",  7))
milan.aggiungi_giocatore(Giocatore("Tomori",   26, "difensore",  23))
milan.aggiungi_assistente(Assistente("Rossi", 42, "analista di gioco"))
 
# --- Presentazione rose ---
inter.presenta_rosa()
milan.presenta_rosa()
 
# --- Allenamenti pre-partita ---
inter.allenati()
milan.allenati()
 
# --- Partita ---
gioca_partita(inter, milan, turni=6)
 
# --- Demo ---
print("\n--- Demo ---")
lautaro = inter.giocatori[0]
print(f"Giocatore: {lautaro.nome}, ruolo: {lautaro.ruolo}, maglia: {lautaro.numero_maglia}")
print(f"Lautaro è nell'Inter? {lautaro in inter.giocatori}")
totale = len(inter.giocatori) + (1 if inter.allenatore else 0) + len(inter.assistenti)
print(f"Numero totale membri Inter: {totale}")
 