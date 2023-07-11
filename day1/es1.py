"""
ESERCIZIO 1

1. Creare una lista di numeri interi (almeno 5 numeri)
2. Usare la funzione append() per aggiungere un elemento
3. Usare la funzione insert() per inserire un elemento in una posizioine specifica (due argomenti)
4. Usare remove
5. Usare sort
"""

# 1. Creare una lista di numeri interi (almeno 5 numeri)
my_list = [1, 3, 18, 2, 9, 17, 4]
print("----------------")
print("----------------")
print("Punto 1: creo una lista")
print(f"La mia lista iniziale:\n{my_list}")

# 2. Usare la funzione append() per aggiungere un elementoù
my_list.append(46)
print("----------------")
print("----------------")
print("Punto 2: aggiungo un elemento in ultima posizione")
print(f"La mia lista con l'elemento aggiunto:\n{my_list}")


# 3. Usare la funzione insert() per inserire un elemento in una posizione specifica (due argomenti)
my_list.insert(3, 402)
print("----------------")
print("----------------")
print("Punto 3: aggiungo un elemento in posizione specifica")
print(f"La mia lista con l'elemento aggiunto in posizione specifica:\n{my_list}")


# 4. Usare remove
my_list.remove(402)
print("----------------")
print("----------------")
print("Punto 4: rimuovo l'elemento appena aggiunto")
print(f"La mia lista con l'elemento rimosso:\n{my_list}")

# 5. Usare sort
my_list.sort()
print("----------------")
print("----------------")
print("Punto 5: ordino la lista")
print(f"La mia lista ordinata:\n{my_list}")