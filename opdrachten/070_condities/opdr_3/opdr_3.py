# Opdracht 3 condities
# Naam student:
# Groep:
normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}
Crew_korting = {"crew": 50}  
leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))
Crew_input = input("Ben je een crew (ja/nee): ").lower() 
if Crew_input == "ja":  
    korting = Crew_korting["crew"]
    print(f"Als crewlid krijg je {korting}% korting.")
else: 
    for groep, leeftijdsgrens in leeftijd.items():
        if leeftijd_input >= leeftijdsgrens[0] and leeftijd_input <= leeftijdsgrens[1]:
            print(f"U behoort tot de groep {groep}")
            korting = kortings_percentages[groep]
            print(f"U krijgt {korting}% korting")
            break

toegangsprijs_met_korting = normale_toegangsprijs * (100 - korting) / 100
print(f"U betaalt daarom {toegangsprijs_met_korting:.2f} euro.")


