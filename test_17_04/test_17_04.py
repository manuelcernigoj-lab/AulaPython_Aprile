# --- Database accounts ---

accounts = {}       # { username: password }


# --- Memoria ---

numeri_inseriti = []
operazioni = []
risultati = []
op_limit = 4


# --- Funzioni account ---
 
def login():
    """Restituisce lo username se il login ha successo, None altrimenti."""
    username = input("Username: ")
    if username not in accounts:        # username non presente nel database
        print("Username non trovato!\nSe non sei registrato, registrati prima di effettuare il Login")
        return None
    password = input("Password: ")
    if accounts[username] == password:
        print(f"Benvenuto, {username}!")
        return username
    print("Credenziali errate!")
    return None
 
def registra():
    username = input("Username: ")
    if username in accounts:
        print("Utente già esistente.")
        return
    password = input("Password: ")
    accounts[username] = password
    print("Registrazione avvenuta. Ora puoi effettuare il login.")


# --- Menu Principale ---

def menu_principale():
    # Loop finché non si ottiene un login valido. Restituisce lo username.
    while True:
        print("""Benvenuto se hai già un account fai Login, altrimenti Registrati:
          1. Login  2. Registrati  3. Esci""")
        scelta = int(input("Scelta: "))
 
        match scelta:
            case 1:
                utente = login()
                if utente:
                    return utente           # login riuscito: esci dal loop
            case 2:
                registra()
            case 3:
                print("Arrivederci!")
                exit()
            case _:
                print("Scelta non valida")

# --- Menu funzione ---

def stampa_riepilogo_sessione():
    print("LIMITE OPERAZIONI RAGGIUNTO")
    print(f"Hai eseguito {op_limit} operazioni. Riepilogo sessione:")
    for op in (operazioni):
        print(f"{op.capitalize()}")
    print("Logout...")

def menu_funzione(username):

    op_count = 0          # contatore operazioni per questa sessione di login
    while True:
        print("""Che funzione vuoi usare:
              1. Calcolatrice   2. Stampa dati""")
        func = int(input("Scleta: "))

        match func:
            case 1:
                print("Hai scelto Calcloatrice")
                menu_calcolatrice()
                op_count += 1
                if op_count >= op_limit:
                    stampa_riepilogo_sessione()
                    return          # torna al menu principale → re-login
            case 2:
                print("Hai scelto Stampa dati")
                menu_stampa()
            case _:
                print("Scelta non valida")


# --- Menu Calcolatrice ---

def menu_calcolatrice():
    print("""Che operazione vuoi eseguire:
          1. Addizione  2. Sottrazione  3. Moltiplicazione  4. Divisione    5. Potenza""")
    op = int(input("Scelta: "))
 
    match op:
        case 1:
            print("Hai scelto Addizione!")
            addizione()
        case 2:
            print("Hai scelto Sottrazione!")
            sottrazione()
        case 3:
            print("Hai scelto Moltiplicazione!")
            moltiplicazione()
        case 4:
            print("Hai scelto Divisione!")
            divisione()
        case 5:
            print("Hai scelto Potenza!")
            potenza()
        case _:
            print("Scelta non valida")


# --- Menu Stampa Dati ---

def menu_stampa():
    # Se non ci sono operazioni in memoria, avvisa l'utente ed esci
    if not operazioni:
        print("Non hai ancora eseguito operazioni.")
        return
 
    print("""Scegli cosa vuoi stampare:
          1. Numeri inseriti    2. Risultati""")
    stamp = int(input("Scelta: "))
 
    match stamp:
        case 1:
            print(f"Ecco i numeri che hai inserito:\n {numeri_inseriti}")
        case 2:
            print(f"Ecco i risultati delle tue operazioni:\n{operazioni}\n{risultati}")
        case _:
            print("Scelta non valida")

# ----- OPERAZIONI -----


## --- Addizione ---

def addizione():
    addendi = []
    numeri_inseriti.append("Addizione")             # segna l'inizio del gruppo in memoria
    print("Digita il primo addendo: ")
    add = int(input("Addendo: "))
    addendi.append(add)
    numeri_inseriti.append(add)
    print("Digita il secondo addendo: ")
    add = int(input("Addendo: "))
    addendi.append(add)
    numeri_inseriti.append(add)
 
    while True:
        print("""Vuoi inserire un altro addendo?:
              1. Si   2. No""")
        scelta1 = int(input("Scelta: "))
 
        match scelta1:
            case 1:
                print("Digita l'addendo da aggiungere: ")
                add = int(input("Addendo: "))
                addendi.append(add)
                numeri_inseriti.append(add)
            case 2:
                risultato = sum(addendi)
                operazioni.append("addizione")
                risultati.append(risultato)
                print(f"Calcolo eseguito! Il risultato è: {risultato}")
                break
            case _:
                print("Scelta non valida")

## --- Sottrazione ---

def sottrazione():
    sottraendi = []
    numeri_inseriti.append("Sottrazione")           # segna l'inizio del gruppo in memoria
    print("Digita il minuendo: ")
    sub = int(input("Minuendo: "))
    sottraendi.append(sub)
    numeri_inseriti.append(sub)
    print("Digita il sottraendo: ")
    sub = int(input("Sottraendo: "))
    sottraendi.append(sub)
    numeri_inseriti.append(sub)
 
    while True:
        print("""Vuoi inserire un altro sottraendo?:
              1. Si   2. No""")
        scelta1 = int(input("Scelta: "))
 
        match scelta1:
            case 1:
                print("Digita il sottraendo da aggiungere: ")
                sub = int(input("Sottraendo: "))
                sottraendi.append(sub)
                numeri_inseriti.append(sub)
            case 2:
                # Sottrae tutti i termini successivi al primo
                risultato1 = sottraendi[0] - sum(sottraendi[1:])
                operazioni.append("sottrazione")
                risultati.append(risultato1)
                print(f"Calcolo eseguito! Il risultato è: {risultato1}")
                break
            case _:
                print("Scelta non valida")

## --- Moltiplicazione ---

def moltiplicazione():
    numeri_inseriti.append("Moltiplicazione")       # segna l'inizio del gruppo in memoria
    print("Digita il primo numero: ")
    mult1 = int(input("Primo numero: "))
    numeri_inseriti.append(mult1)
    print("Digita il secondo numero: ")
    mult2 = int(input("Secondo numero: "))
    numeri_inseriti.append(mult2)
    risultato2 = mult1 * mult2
    operazioni.append("moltiplicazione")
    risultati.append(risultato2)
    print(f"Calcolo eseguito! Il risultato è: {risultato2}")

## --- Divisione ---

def divisione():
    numeri_inseriti.append("Divisione")             # segna l'inizio del gruppo in memoria
    print("Digita il numeratore: ")
    div1 = int(input("Numeratore: "))
    numeri_inseriti.append(div1)
    print("Digita il denominatore: ")
    div2 = int(input("Denominatore: "))
    numeri_inseriti.append(div2)
    if div2 != 0:
        risultato3 = div1 / div2
        operazioni.append("divisione")
        risultati.append(risultato3)
        print(f"Calcolo eseguito! Il risultato è: {risultato3}")
    else:
        # Divisione per zero non consentita: operazione annullata
        print(f"Calcolo non eseguito! Non puoi dividere per {div2}")

## --- Potenza ---

def potenza():
    numeri_inseriti.append("Potenza")               # segna l'inizio del gruppo in memoria
    print("Digita la base: ")
    pot1 = int(input("Base: "))
    numeri_inseriti.append(pot1)
    print("Digita l'esponente: ")
    pot2 = int(input("Esponente: "))
    numeri_inseriti.append(pot2)
    risultato4 = pot1 ** pot2
    operazioni.append("potenza")
    risultati.append(risultato4)
    print(f"Calcolo eseguito! Il risultato è: {risultato4}")


# --- Avvio programma ---
 
while True:
    # Ottieni un utente autenticato, poi avvia il menu funzione
    utente = menu_principale()
    if utente:
        menu_funzione(utente)   #  passa username per riepilogo e re-login