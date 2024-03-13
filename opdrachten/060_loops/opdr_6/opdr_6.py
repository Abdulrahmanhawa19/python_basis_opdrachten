# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizzas.sort()
print("Lijst gesorteerd op alfabet:", pizzas)

# Voeg een nieuwe pizza toe
pizzas.append('yo-favorito')
print("Nieuwe lijst met toegevoegde pizza:", pizzas)

# Verwijder de pizza die je het minst lekker vindt
pizzas.remove('olivio')
print("Lijst na het verwijderen van 'olivio':", pizzas)

# Print de eerste 3 pizza's uit de lijst
print("Eerste 3 pizza's:", pizzas[:8])

# Print alleen de middelste pizza uit de lijst
middle_index = len(pizzas) // 2
print("Middelste pizza:", pizzas[middle_index])

# Print de laatste 3 pizza's uit de lijst
print("Laatste 3 pizza's:", pizzas[-5:])
