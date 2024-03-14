# Opdracht 4 condities
# Naam student:
# Groep:
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]
gekozen_toppings = []
while True:
    print("Beschikbare toppings:", beschikbare_toppings)
    keuze = input("Maak een keuze uit onze toppings (typ 'stop' om te stoppen): ").strip().lower()
    if keuze == 'stop':
        break
    gevonden = False
    for topping, prijs in toppings:
        if keuze == topping.lower():
            gevonden = True
            gekozen_toppings.append((topping, prijs))
            print(f"U heeft {topping} besteld. Dat kost {prijs}")
            break
    
    if not gevonden:
        print("Uw keuze zit niet in ons assortiment")
if gekozen_toppings:
    totale_prijs = sum(prijs for _, prijs in gekozen_toppings)
    print("Uw bestelling:")
    for topping, prijs in gekozen_toppings:
        print(f"- {topping}: €{prijs}")
    print(f"Totale kosten: €{totale_prijs}")
else:
    print("U heeft geen toppings besteld.")

