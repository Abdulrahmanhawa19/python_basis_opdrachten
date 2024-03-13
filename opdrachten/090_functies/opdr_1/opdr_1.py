# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(bestandsnaam, tekst):
    # Open het bestand in de schrijfmodus en voeg de tekst toe aan het bestand
    with open(bestandsnaam, "a") as bestand:
        bestand.write(tekst + "\n")

# Voorbeeldgebruik van de functie
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)

