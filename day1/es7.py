"""
ESERCIZIO 7

Trova il massimo fra tre numeri inseriti dall'utente
"""

list_of_number = []
for i in range(3):
    number = float(input("Inserisci un numero: "))
    list_of_number.append(number)

massimo = 0
for number in list_of_number:
    if number > massimo:
        massimo = number

print(f"Lista: {list_of_number.sort()}")
print(f"Massimo: {massimo}")