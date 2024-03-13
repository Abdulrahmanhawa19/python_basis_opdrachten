# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
# Originele lijst
people = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print("Originele lijst:", people)

# Marie wordt uit de lijst verwijderd
people.remove("Marie")
print("Lijst zonder Marie:", people)

# George wordt naast Kees toegevoegd
kees_index = people.index("Kees")
people.insert(kees_index + 1, "George")
print("Lijst met George naast Kees:", people)
