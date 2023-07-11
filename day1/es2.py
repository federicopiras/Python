"""
ESERCIZIO 2

1. Creare una tupla che contenga le nostre informazioni(nome, cognome, età, città)
2. Stampare i dati singolarmente
3. Creare un dizionario che contenga i dati di una automobile (marca, nome modello, numero porte, colore) 
4. Stampare i dati
5. Cambiare il colore dell'auto
6. Aggiungi una coppia chiave-valore cilindrata
"""

# Punti 1 e 2
my_info = ("Federico", "Piras", 27, "Rimini")
print("Il mio nome è: ", my_info[0])
print("Il mio cognome è: ", my_info[1])
print(f"La mia età è: {my_info[2]} anni")
print(f"Vivo a: {my_info[-1]}")

# .. oppure
for element in my_info:
    print(element)

# Punti 3 e 4
my_dict = {
    "marca": "Nissan",
    "modello": "Qashqai",
    "n_porte": 5,
    "colore": "grigio"
}

# # print singoli valori
# print(my_dict["marca"])
# print(my_dict["modello"])
# print(my_dict["n_porte"])
# print(my_dict["colore"])

# .. o in modo più efficiente:
for key in my_dict.keys():
    print(f"{key.capitalize()}: {my_dict[key]}")


# Punti 5 e 6
# modifico il valore associato alla chiave colore e aggiungo la nuova chiave cilindrata
my_dict["colore"] = "nero"
my_dict["cilindrata"] = 3000
# print coppie chiave-valore
for key in my_dict.keys():
    print(f"{key.capitalize()}: {my_dict[key]}")
