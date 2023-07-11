### SE VUOI COMMENTARE TUTTO USA CMD+shift+7

# # Funzione print
# print("Hello world!!")

# # variabile
# nome = "Federico"
# age = 27
# print("il mio nome è", nome, "e ho", age, "anni")

# # variabile e f-string
# name = input("Inserisci nome: ")
# print(f"Ciao {name}, benvenuto in python")

# # variabile e + per concatenare stinghe
# name = input("Inserisci nome: ")
# print("Ciao " + name + ", benvenuto in python")

# # variabile
# name = input("Inserisci il tuo nome: ")
# greeting_string = f"Ciao {name}, benvenuto in Python!!"
# print(greeting_string)

# 3 variabili e le stampo con un print
name = "Federico"
surname = "Piras"
age = 27
sentence = "Ciao, sono " + name + " " + surname +  " e ho " + str(age) + " anni"
print(sentence)
print(sentence.split())
# print(f"Ciao, sono {name} {surname} e ho {age} anni")

# # 3 variabili di input
# name = input("Inserisci nome: ")
# surname = input("Inserisci cognome: ")
# age = input("Inserisci anni: ")
# sentence = "Ciao, sono " + name + " " + surname +  " e ho " + age + " anni"
# print(sentence)

# # Prova stringa con index
# name = "Federico"
# for i in range(len(name)):
#     print(f"La lettera all'indice {i} è {name[i]}")