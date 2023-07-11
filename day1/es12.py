"""
ESERCIZIO 12

FIZZBUZZ

Stampare i numeri da 1 a 100, sostituendo
i multipli di 3 con "Fizz",
i multipli di 5 con "Buzz"
i multipli di entrambi con "FizzBuzz"

"""

for i in range(101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)