# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...
# opdr_1.py

# my_modules/csv.py

import csv

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
# opdr_1.py

from my_modules import csv

data = [
    ['Name', 'Age', 'Country'],
    ['John', 30, 'USA'],
    ['Emily', 25, 'UK'],
    ['David', 35, 'Canada']
]

csv.write_to_csv('output.csv', data)
print("Data has been written to output.csv")
