# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:
def encrypteren(tekst):
    gecodeerde_tekst = ""
    for letter in tekst:
        if letter.isalpha():  # Controleer of het een letter is
            # Bepaal of het een hoofdletter of kleine letter is
            basis = ord('A') if letter.isupper() else ord('a')
            # Verschuif de letter met 5 posities in het alfabet en zorg ervoor dat het binnen de grenzen van het alfabet blijft
            gecodeerde_letter = chr((ord(letter) - basis + 5) % 26 + basis)
            gecodeerde_tekst += gecodeerde_letter
        else:
            gecodeerde_tekst += letter  # Behoud spaties en leestekens ongewijzigd
    return gecodeerde_tekst

# Vraag de gebruiker om de tekst die ze willen encrypten
invoer = input("Geef de tekst die wilt encrypten: ")

# Encrypteer de ingevoerde tekst
gecodeerde_tekst = encrypteren(invoer)

# Geef de gecodeerde tekst weer
print("De gecodeerde tekst is:", gecodeerde_tekst)




