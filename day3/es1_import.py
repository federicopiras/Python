def is_palindromo(my_stringa):

    if type(my_stringa) != str:
        print(f"Devi inserire una stringa, hai inserito una cosa di tipo {type(my_stringa)}")

    elif my_stringa.replace(" ", "") == my_stringa[::-1].replace(" ", ""):
        print("La stringa è palindroma")

    else:
        print("La stringa non è palindroma")


class Persona:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print(f"Ciao {self.nome} {self.cognome} !")