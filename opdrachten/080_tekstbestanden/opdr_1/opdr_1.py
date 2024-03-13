# Opdracht 1 while-loops
# Naam student:
# Groep:

# Vragen stellen aan de gebruiker
vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

# Resultaten opslaan in een tekstbestand
with open("enquete_resultaten.txt", "w") as file:
    file.write("Resultaten van de enquete:\n")
    file.write("1. Wat vind je van de huidige regering? " + vraag1 + "\n")
    file.write("2. Wat vind je van de Python-lessen tot nu toe? " + vraag2 + "\n")
    file.write("3. Wat vind jij de mooiste stad van Nederland? " + vraag3 + "\n")

print("Bedankt voor het invullen van de enquete. De resultaten zijn opgeslagen in enquete_resultaten.txt.")
