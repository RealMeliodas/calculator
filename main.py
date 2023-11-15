#!/usr/bin/env python3
def main():
    print("Benvenuti sulla mia Calcolatrice")

if __name__ == "__main__":
    main()
# Funzioni per ogni operazioni basiche algebriche
def somma (a,b):
    return a+b
def sottrazione (a,b):
    return a-b
def moltiplicazione (a,b):
    return a*b
def divisione (a,b):
    return a/b

# Messaggio iniziale
message = """  
Calcolatrice: 
------------------
1) Somma
2) Sottrazione
3) Moltiplicazione
4) Divisione
-------------------
0) Esci
"""

# Ciclo while per non far interrompere il programma
while True:
    print(message)

    scelta = input("Inserisci il numero dell'operazione che vuoi effettuare: ")

    # Vari cicli if per le varie operazioni che l'utente può effettuare
    if scelta == "1":
        a = float(input("\nInserisci il Primo Numero: "))
        b = float(input("Inserisci il Secondo Numero: "))
        print("Il risultato è: ", somma(a,b))
    elif scelta == "2":
        a = float(input("\nInserisci il Primo Numero: "))
        b = float(input("Inserisci il Secondo Numero: "))
        print("Il risultato è: ", sottrazione(a,b))
    elif scelta == "3":
        a = float(input("\nInserisci il Primo Numero: "))
        b = float(input("Inserisci il Secondo Numero: "))
        print("Il risultato è: ", moltiplicazione(a,b))
    elif scelta == "4":
        a = float(input("\nInserisci il Primo Numero: "))
        b = float(input("Inserisci il Secondo Numero: "))
        print("Il risultato è: ", divisione(a,b))
    elif scelta == "0":
        print("\nChiusura in corso...")
        break
    elif scelta not in [1, 2, 3, 4]:
        print("\nScelta non valida")

    # Nuova variabile e nuovo ciclo if per far sì che l'utente possa decidere se stoppare il programma o no
    nuova_scelta = input("\nVuoi continuare ad utilizzare la calcolatrice? Premi S/N.  ")
    if nuova_scelta == "Si" or nuova_scelta == "si" or nuova_scelta == "S" or nuova_scelta == "s":
        print("\nTorno al menù.")
        continue
    else:
        print("\nAddio")
        break