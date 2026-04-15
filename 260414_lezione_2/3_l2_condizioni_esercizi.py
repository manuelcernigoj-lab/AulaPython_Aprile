
"""
1.  Creare una serie di condizioni una dentro l'altra che a fronte di un input
    per ogni if decidano se farti passare o no ( 3 livelli, fate un paragone con == )
"""
# chiedo il numero all'utente e lo converto in int
condizione = int(input("Scegli un numero intero:"))

# prima condizione
if condizione > 0:
    print("Il tuo numero è maggiore di 0.")
    # seconda condizione
    if condizione < 100:
        print("Il tuo numero è tra 0 e 100.")
        # terza condizione
        if condizione == 50: 
            print("Il numero che hai scelto è proprio 50!")
            
"""
2.  Andare a creare un if con vari elif e un else finale che gestisca un
    menu per la selezione di un crud basilare (aggiungi modifica elimina)
"""

# definizione della lista
lista = ['Giorgio', 'Daniele', 'Mario']

# input per prendere la richiesta
richiesta = int(input("Scegli se vuoi aggiungere [1], eliminare [2] o modificare [3]: "))

# condizione 1, aggiunge un elemento alla fine
if richiesta == 1:
    aggiungi = input("Nome dell'utente da aggiungere?")
    lista.append(aggiungi)
    print(f""" Ho aggiunto {aggiungi} alla lista, la nuova lista è:\n {lista}""")
    
# condizione 2, rimuove un elemento    
elif richiesta == 2:
    rimuovi = input("Quale utente vuoi rimuovere? ")
    lista.remove(rimuovi)
    print(f""" Ho rimosso {rimuovi} dalla lista, la nuova lista è:\n {lista}""")
    
# condizione 3, inserisce un elemento in una posizione definita dall'utente 
elif richiesta == 3:
    inserisci = input("Quale utente vuoi inserire? ")
    posizione = int(input(f"La lista corrente è: {lista}. In che posizione vuoi inserirlo? Digita il numero:"))   
    lista.insert(posizione - 1, inserisci)
    print(f""" Ho inserito {inserisci} in posizione {posizione} della lista, la nuova lista è:\n {lista}""")
else: 
    lista.sort()
    print(lista)

"""
3.  Creare un if con else semplice, dentro l'if inserire una struttura di creazione di dati (nome, password, id dato dal sistema a crescere) 
    e nell'else il controllo automatico la dove è presente l'account nel sistema e solo se si passa dall'else concludere lo script
"""

# dati esistenti nel sistema: id, user e password degli account registrati
id = [1, 2, 3]
user = ["Auri", "Gloria", "Diego"]
pw = [1332, 6455, 9152]

# input per scegliere tra accesso e registrazione
scelta = int(input("Vuoi accedere [1] o registrarti [2]"))

# --- registrazione nuovo utente ---
if scelta == 2:
    nome = input("Inserisci il tuo nome utente:")
    password = input("Inserisci la tua password di 4 cifre:")
    nuovo_id = len(id) + 1                                      # id assegnato automaticamente in base alla lunghezza della lista
    user.append(nome)                                           # aggiunge il nome alla lista degli account
    pw.append(password)                                         # aggiunge la password alla lista
    id.append(nuovo_id)                                         # aggiunge il nuovo id alla lista
    print("Ti sei registrato con successo!")
    print(f"Nome utente: {nome}")
    print(f"Password: {password}")
    print(f"ID: {nuovo_id}")

# --- accesso utente esistente ---
else:
    nome = input("Scegli l'account con cui accedere:")
    password = int(input("Digita la password da 4 cifre:"))
    if nome in user:                                            # controlla se il nome è presente nel sistema
        print("Accesso effettuato!")
    else:
        print("Account non trovato.")
      
"""
4.  Scrivi un programma che chieda all'utente la sua età. Se l'età è
    inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi
    vedere questo film". Altrimenti, dovrebbe stampare "Puoi vedere questo film".
"""
# input dell'età
eta = int(input("Inserisci la tua età:"))

# verifica età
if eta < 18:
    print("Mi dispiace, non puoi vedere questo film")
else:
    print("Puoi vedere questo film")
 
"""    
5.Scrivi un programma che chieda all'utente di inserire due
  numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
  moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire
  l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di dividere
  per zero, il programma dovrebbe stampare "Errore: Divisione per zero". 
  Se l'operazione inserita non è riconosciuta, dovrebbe stampare "Operazione
  non valida".
"""      

# input per ottenere i due numeri su cui eseguire l'oeprazione
num_1 = int(input("Scrivi il primo numero:"))
num_2 = int(input("Scrivi il secondo numero:"))

# input per far scegliere l'operazione da eseguire
op = input("Scegli quale operazione eseguire tra: addizione [+]), sittrazione [-]), moltiplicazione [*]), divisione [/])")

# --- menu operazioni ---
# definito un 'case' e un 'print' per ogni operazione
match op:
    case "+":
        print(num_1 + num_2)
    case "-":
        print(num_1 - num_2)
    case "*":
        print(num_1 * num_2)
    case "/":
        if num_2 == 0:                              # trattamento della divisione per 0
            print("Errore: Divisione per zero")     # se divideno è 0 -> mostra errore
        else:
            print(num_1 / num_2)
    case _:                                         # trattamento operazione non valida
        print("Operazione non valida")