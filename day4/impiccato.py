# Importiamo random per pescare un elemento a caso da una lista con random.choice
import random

# Definisco una lista di parole e seleziono una parola casuale con random.choice
word_list = ["python", "ciao", "bussola", "programma"]
word = random.choice(word_list)

"""
Definisco delle variabili per il controllo di flusso/cpnteggio errori

my_guess: stringa che contiene lo stato di avanzamento del guess della parola
n_errors: intero, mi dice quante volte ho sbagliato
n_guess: intero, mi dice quanti guess ho fatto
max_guess: intero, mi dice quante volte posso giocare
"""
my_guess = '_'*len(word)
n_errors = 0
n_guess = 0
max_guess = len(word)*2
print(f"World to guess: {my_guess}")

# Finchè ho dei tentativi e non ho indovinato...
while n_guess <= max_guess and my_guess != word:
    my_char = input("Insert a character: ")
    print(type(my_char))

    # E se inserisco più di una lettera?
    while len(my_char) > 1:
        print(f"Puoi inserire un solo carattere! Ne hai inseriti {len(my_char)}")
        my_char = input("Insert a character: ")

    # Ok, una volta che abbiamo inserito un guess corretto, incrementiamo la conta dei guess
    n_guess += 1

    # Se il carattere che inserisco è nella parola da indovinare...
    if my_char in word:
        print("The character is present! ")

        # Modo 1 per rimpiazzare gli _ con la lettera trovata alla posizione giusta
        idx = [i for i in range(len(word)) if my_char == word[i]]
        for i in idx:
            my_guess = my_guess[:i] + my_char + my_guess[i+1:]

        # Modo 2: lista?
        my_guess_ = list(my_guess)
        for i in idx:
            my_guess_[i] = my_char
        my_guess = ''.join(my_guess_)

    # Se invece non c'è...
    elif my_char not in word:
        print("carattere non presente, riprova")
        n_errors += 1
        print(f"Errors made: {n_errors}")
        print(f"Guesses left: {max_guess-n_guess}")

    # Printo l'avanzamento nell'indovinare la parola
    print(my_guess)

if n_guess == max_guess and my_guess != word:
    print("I'm sorry, you did not guess the word")

