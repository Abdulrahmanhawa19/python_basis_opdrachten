# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
pizzas.sort()
print("Lijst gesorteerd op alfabet:", pizzas)
pizzas.append('yo-favorito')
print("Nieuwe lijst met toegevoegde pizza:", pizzas)
pizzas.remove('olivio')
print("Lijst na het verwijderen van 'olivio':", pizzas)
print("Eerste 3 pizza's:", pizzas[:9])
middle_index = len(pizzas) // 2
print("Middelste pizza:", pizzas[middle_index])
print("Laatste 3 pizza's:", pizzas[-9:])