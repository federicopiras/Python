"""
ESERCIZIO 6: PARLIAMO DI IF

Verificare se un numero inserito dall'utente è pari o dispari.
"""

number = int(input("Inserisci un numero: "))
resto = number % 2

if resto == 0:
    print(f"Il numero che hai scelto è {number} ed è pari")
else:
    print(f"Il numero che hai scelto è {number} ed è dispari")