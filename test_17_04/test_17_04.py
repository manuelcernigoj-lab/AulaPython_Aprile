# --- Database accounts ---
accounts = {}       # { username: password }

# --- Memoria ---
numeri_inseriti = []
operazioni = []
risultati = []
op_limit = 4

def login():
    """Restituisce lo username se il login ha successo, None altrimenti."""
    username = input("Username: ")
    password = input("Password: ")
    if username in accounts and accounts[username] == password:
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
    """Loop finché non si ottiene un login valido. Restituisce lo username."""
    while True:
        print("""Benvenuto se hai già un account fai Login, altrimenti Registrati:
          1. Login  2. Registrati  3.Esci""")
        scelta = int(input("Scelta: "))

        match scelta:
            case 1:
                utente = login()
                if utente:
                    return utente
            case 2:
                registra()
            case 3:
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida")

# --- Menu funzione ---

def stampa_riepilogo_sessione():
    print("LIMITE OPERAZIONI RAGGIUNTO")
    print(f"Hai eseguito {op_limit} operazioni. Riepilogo sessione:")
    for op in (operazioni):
        print(f"{op.capitalize()}")
    print("Logout...")

def menu_funzione():

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
    op = int(input("Scleta: "))

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

    print("""Scegli cosa vuoi stampare:
          1. Numeri inseriti    2. Risultati""")
    stamp = int(input("Scleta: "))

    match stamp:
        case 1:
            print(f"Ecco i numeri che hai inserito:\n {numeri_inseriti}")
        case 2:
            print(f"Ecco i risultati delle tue operazioni:\n{operazioni}\n{risultati}")
        case _:
            print("Scelta non valida")

# --- Menu operazioni ---

## --- Addizione ---
def addizione():

    addendi = []
    numeri_inseriti.append("Addizione")
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
    numeri_inseriti.append("Sottrazione")
    print("Digita il primo addendo: ")
    sub = int(input("Addendo: "))
    sottraendi.append(sub)
    numeri_inseriti.append(sub)
    print("Digita il secondo addendo: ")
    sub = int(input("Addendo: "))
    sottraendi.append(sub)
    numeri_inseriti.append(sub)

    while True:
        print("""Vuoi inserire un altro addendo?:
              1. Si   2. No""")
        scelta1 = int(input("Scelta: "))

        match scelta1:
            case 1:
                print("Digita l'addendo da aggiungere: ")
                sub = int(input("Addendo: "))
                sottraendi.append(sub)
                numeri_inseriti.append(sub)
            case 2:
                risultato1 = sottraendi[0] - sum(sottraendi[1:])
                operazioni.append("sottrazione")
                risultati.append(risultato1)
                print(f"Calcolo eseguito! Il risultato è: {risultato1}")
                break            
            case _:
                print("Scelta non valida")

## --- Moltiplicazione ---
def moltiplicazione():
    numeri_inseriti.append("Moltiplicazione")
    print("Digita il primo numero: ")
    mult1 = int(input("Primo numero: "))
    numeri_inseriti.append(mult1)
    print("Digita il secondo numero: ")
    mult2 = int(input("Secondo numero: "))
    numeri_inseriti.append(mult2)
    risultato2 = mult1*mult2
    operazioni.append("moltiplicazione")
    risultati.append(risultato2)
    print(f"Calcolo eseguito! Il risultato è: {risultato2}")

## --- Divisione ---
def divisione():
    numeri_inseriti.append("Divisione")
    print("Digita il primo numeratore: ")
    div1 = int(input("Numeratore: "))
    numeri_inseriti.append(div1)
    print("Digita il denominatore: ")
    div2 = int(input("Denominatore: "))
    numeri_inseriti.append(div2)
    if div2 != 0:
        risultato3 = div1/div2
        operazioni.append("divisione")
        risultati.append(risultato3)
        print(f"Calcolo eseguito! Il risultato è: {risultato3}")
    else:
        print(f"Calcolo non eseguito! non puoi dividere per {div2}")

## --- Potenza ---
def potenza():
    numeri_inseriti.append("Potenza")
    print("Digita il primo numero: ")
    pot1 = int(input("Primo numero: "))
    numeri_inseriti.append(pot1)
    print("Digita il secondo numero: ")
    pot2 = int(input("Secondo numero: "))
    numeri_inseriti.append(pot2)
    risultato4 = pot1**pot2
    operazioni.append("potenza")
    risultati.append(risultato4)
    print(f"Calcolo eseguito! Il risultato è: {risultato4}")

utente = menu_principale()
if utente:
    menu_funzione()