# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = { 
    "rijn": ["Nederland", "Duitsland", "Frankrijk"], 
    "maas": ["Nederland", "België", "Duitsland"], 
    "Nijl": ["Egypte", "Soedan", "Oeganda"] 
}
Barraa = "rijn"
fufu = "maas"
sisi = "Nijl"
rivieren = list(rivier_info.keys())

# Print de naam van de 1e rivier
print("De rivier", rivieren[0].capitalize(), "stroomt onder andere door", rivier_info[rivieren[0]][1].capitalize())
print(Barraa)
# Print de naam van de 2e rivier
print("De rivier", rivieren[1].capitalize(), "stroomt onder andere door", rivier_info[rivieren[1]][0].capitalize())
print(fufu)
# Print de naam van de 3e rivier
print("De rivier", rivieren[2].capitalize(), "stroomt onder andere door", rivier_info[rivieren[2]][2].capitalize())
print(sisi)