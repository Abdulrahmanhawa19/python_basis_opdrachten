# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

# Maak een lege lijst om de getallen in op te slaan
getallen = []

# Vul de lijst met getallen van 1 t/m 10
for i in range(1, 11):
    getallen.append(i)

# Print alleen de getallen die groter zijn dan 4
for getal in getallen:
    if getal > 4:
        print(getal)
