import numpy as np

# Seed fisso per rendere ripetibile il processo
np.random.seed(42)

while True:

    # 1. Array di 50 numeri equidistanti tra 0 e 10
    arr = np.linspace(0, 10, 50)
    print(f"\n1. Array linspace:\n{arr}")

    # 2. Array casuale
    rand = np.random.random(50)
    print(f"\n2. Array random:\n{rand}")

    # 3. Somma elemento per elemento
    arr_sum = arr + rand
    print(f"\n3. Somma dei due array precedenti:\n{arr_sum}")

    # 4. Somma totale
    tot = np.sum(arr_sum)
    print(f"\n4. Somma totale: {tot:.2f}")

    # 5. Somma dei valori > 5
    above_5 = np.sum(arr_sum[arr_sum > 5])
    print(f"\n5. Somma valori > 5: {above_5:.2f}")

    # 7. Salva i dati su un file TXT a ogni giro
    scelta = input(
        "\nVuoi sovrascrivere il file o aggiungere dati?\n"     # 9. Chiedi se si vuole sovrascrivere il TXT o no.
        "Scrivi 'w' per sovrascrivere oppure 'a' per aggiungere: "
    ).lower()

    # Controllo input
    while scelta not in ["w", "a"]:
        scelta = input("Inserisci solo 'w' oppure 'a': ").lower()

    with open("260512_lezione_19/risultati.txt", scelta, encoding="utf-8") as file:

        file.write("\n========================\n")
        file.write("NUOVA ESECUZIONE\n")
        file.write("========================\n")

        file.write(f"\nArray linspace:\n{arr}\n")
        file.write(f"\nArray random:\n{rand}\n")
        file.write(f"\nSomma array precedenti:\n{arr_sum}\n")

        file.write(f"\nSomma totale: {tot:.2f}\n")
        file.write(f"Somma valori > 5: {above_5:.2f}\n")

    print("\nDati salvati in risultati.txt")

    # 8. Rendi ripetibile il processo complessivo
    continua = input("\nVuoi eseguire di nuovo il programma? (s/n): ").lower()

    if continua != "s":
        print("\nProgramma terminato.")
        break