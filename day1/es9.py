"""
ESERCIZIO 9

Verificare se una chiave è presente in un dizionario
"""

my_dict = {
    "nome": "Federico",
    "cognome": "Piras"
}

dict_keys = list(my_dict.keys())

key_to_check = input("Che chiave stai cercando? ")

if key_to_check not in dict_keys:
    print("La chiave che cerchi non è nel dizionario.")
    print(f"Chiave inserita: {key_to_check}")
    print(f"Chiavi disponibili: {dict_keys}")
else:
    print(f"La chiave è presente! Il valore associato è {my_dict[key_to_check]}")