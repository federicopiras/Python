"""
ESERCIZIO 8

Verificare se un elemento inserito dall'utente è inserito in una lista
"""

lista = [1, 2, 3, 4, 5, 6, -8, 2398, 4.2]
lista = [float(element) for element in lista]

number = float(input("Inserisci un numero: "))
if number not in lista:
    print("il numero non è nella lista")
else:
    print("Il numero è nella lista")

print(f"Numero: {number}")
print(f"Lista: {sorted(lista)}")