# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        volledige_naam = persoon["voornaam"]
        if persoon["tussenvoegsel"]:  # Controleer of er een tussenvoegsel is
            volledige_naam += " " + persoon["tussenvoegsel"]
        volledige_naam += " " + persoon["achternaam"]
        print(volledige_naam)

# Testen van de functie met de gegeven lijst met namen
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
