# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
import math

def bereken_schuine_zijde(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    print("Geef de lengte van de eerste zijde")
    zijde1 = float(input())
    print("Geef de lengte van de tweede zijde")
    zijde2 = float(input())

    schuine_zijde = bereken_schuine_zijde(zijde1, zijde2)
    print("\nDe lengte van de schuine zijde is:", schuine_zijde)

if __name__ == "__main__":
    main()


