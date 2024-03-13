# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

def raad_een_nummertje():
    geheime_getal = random.randint(1, 100)
    aantal_pogingen = 0

    print("Raad mijn geheime getal")

    while True:
        poging = int(input())

        aantal_pogingen += 1

        if poging < geheime_getal:
            print("hoger")
        elif poging > geheime_getal:
            print("lager")
        else:
            print(f"Je hebt het getal geraden! Het is {geheime_getal}!")
            print(f"Je hebt het in {aantal_pogingen} keer gedaan.")
            break

raad_een_nummertje()

