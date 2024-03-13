# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

resultaten = []

# Gebruik een for-loop en range om door de reeks van getallen te itereren
for i in range(3, 82, 3):
    # Neem elk getal in het kwadraat en deel het door 3
    resultaat = (i ** 2) / 3.0
    resultaten.append(resultaat)

# Print de lijst met resultaten op het scherm
print(resultaten)
