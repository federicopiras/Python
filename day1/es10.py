"""
ESERCIZIO 10

contare quante volte una vocale appare dentro una specifica stringa
"""

parola = "banana"
lettera_da_contare = "a"
contatore = 0

for lettera in parola:
    if lettera == lettera_da_contare:
        contatore += 1

print(f"La lettera {lettera_da_contare} appare {contatore} volte nella parola {parola}")