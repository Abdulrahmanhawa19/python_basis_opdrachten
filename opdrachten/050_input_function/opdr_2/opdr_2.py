# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Originele lijst
people = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print("Originele lijst:", people)
people.remove("Marie")
print("Lijst zonder Marie:", people)
kees_index = people.index("Kees")
people.insert(kees_index + 1, "George")
print("Lijst met George naast Kees:", people)
