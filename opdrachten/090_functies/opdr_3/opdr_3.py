# Opdracht 1 functies
# Naam student:
# Groep:


import math

def kubus_vol(zijde):
    volume = zijde ** 3
    return volume

def bol_vol(r):
    volume = (4/3) * math.pi * r**3
    return volume

# Voorbeeldgebruik van de functies
zijde_kubus = 5
radius_bol = 4

volume_kubus = kubus_vol(zijde_kubus)
volume_bol = bol_vol(radius_bol)

print(f"De inhoud van deze kubus is: {volume_kubus}")
print(f"De inhoud van deze bol is: {volume_bol}")
