# Creation de devinez nombre
import random

MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)

def ask_number(MIN_NUMBER, MAX_NUMBER) :
    number_int = 0
    while number_int == 0:
        number_str = input(f"Quel est le nombre magique (entre {MIN_NUMBER} et {MAX_NUMBER}) ? ")
        try:
            number_int = int(number_str)
        except ValueError:
            print("Erreur : Entrez un nombre")
        else:
            if number_int < MIN_NUMBER or number_int > MAX_NUMBER:
                print(f"ERREUR : Entrez un nombre compris entre {MIN_NUMBER} et {MAX_NUMBER}")
                number_int = 0
    return number_int


number = 0

while number != MAGIC_NUMBER:
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER :
        print("Bravo, vous avez gagné ! ")
    elif number > MAGIC_NUMBER:
        print(f"Le nombre est plus petit que {number}")
    else:
        print(f"Le nombre est plus grand que {number}")