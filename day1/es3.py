"""
ESERCIZIO 3: insiemi

Creare due insiemi e farne:
1. L'unione
2. L'intersezione
3. La differenza
4. La differenza simmetrica
"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("==========")
print("Unione")
print(set1.union(set2))

print("==========")
print("Intersezione")
print(set1.intersection(set2))

print("==========")
print("Differenza")
print(set1.difference(set2))

print("==========")
print("Differenza simmetrica")
print(set1.symmetric_difference(set2))

# Discard -> se l'elemento non è presente, non fa nulla
print("==========")
print("Discard")
print(f"set1: {set1}")
set1.discard(3)
print(set1)
set1.discard(3)
print(set1)

# Remove -> se l'elemento non è presente da errore 
print("==========")
print("Remove")
# lo rimuovo la prima volta
set1.remove(2)
print(set1)
# provo a rimuoverlo la seconda volta
try:
    set1.remove(2)
except:
    print("L'elemento non è presente e non posso rimuoverlo")
