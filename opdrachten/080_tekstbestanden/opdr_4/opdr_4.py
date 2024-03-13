# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Lijst met vragen
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Open het tekstbestand om gegevens op te slaan
with open("feestgangers.txt", "w") as bestand:
    # Loop door elke vraag en vraag de gebruiker om invoer
    for vraag in vragen:
        antwoord = input(f"{vragen.index(vraag) + 1}. {vraag}\n")
        bestand.write(f"{vraag.split('Wat ')[1].split(' ')[0].lower()}: {antwoord}\n")  # Schrijf het antwoord naar het tekstbestand

print("Bedankt voor het invullen!")
print("See you at the party.")
