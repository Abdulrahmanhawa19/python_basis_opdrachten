# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

steden = input("Voer minimaal 5 steden in, gescheiden door komma's: ").split(',')

# Verwijder eventuele extra spaties aan het begin en einde van elk element in de lijst
steden = [stad.strip() for stad in steden]

# Sorteer de lijst in omgekeerde volgorde
steden.sort(reverse=True)

# Print de gesorteerde lijst
print("Gesorteerde lijst in omgekeerde volgorde:")
print(steden)

