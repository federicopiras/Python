"""
Esercizio 5

PARTE 1
Dichiara un numero uguale a 10.
Se il numero è maggiore di 0 stampa il numero è positivo
Se il numero è negativo elif

PARTE 2
Rifallo con input
"""

# Parte 1
number = 10
if number > 0:
    print("il numero è positivo")
elif number < 0:
    print("il numero è negativo")

# Parte 2
number_ = int(input("Inserisci un numero: "))
if number_ > 0:
    print("il numero è positivo")
elif number_ < 0:
    print("il numero è negativo")