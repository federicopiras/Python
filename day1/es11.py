"""
ESERCIZIO 11

Stampare i caratteri unici presenti in due stringhe
"""

parola1 = "ciao"
parola2 = "buongiorno"

lettere_comuni = set(parola1).intersection(set(parola2))

for lettera in lettere_comuni:
    print(lettera)