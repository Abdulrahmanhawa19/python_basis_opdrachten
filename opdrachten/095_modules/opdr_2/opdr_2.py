# Opdracht 1 modules
# Naam student:
# Groep:

# my_modules/csv.py

import csv

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

def filter(data, field_name, filter_str):
    filtered_data = [row for row in data if filter_str.lower() in str(row[field_name]).lower()]
    return filtered_data
# opdr_1.py

from my_modules import csv

data = [
    {'voornaam': 'Jan', 'achternaam': 'Van Der Vliet', 'plaats': 'Amsterdam'},
    {'voornaam': 'Piet', 'achternaam': 'De Vries', 'plaats': 'Rotterdam'},
    {'voornaam': 'Griet', 'achternaam': 'Van Der Pol', 'plaats': 'Den Haag'},
    {'voornaam': 'Jan Jaap', 'achternaam': 'Siewers', 'plaats': 'Utrecht'}
]

csv.write_to_csv('output.csv', data)
print("Data has been written to output.csv")

def print_filtered(filtered_data):
    for row in filtered_data:
        print(row['voornaam'], row['achternaam'])

print("\nFiltering by voornaam starting with 'Ja':")
filtered_data = csv.filter(data, 'voornaam', 'Ja')
print_filtered(filtered_data)

print("\nFiltering by voornaam starting with 'Pie':")
filtered_data = csv.filter(data, 'voornaam', 'Pie')
print_filtered(filtered_data)

print("\nFiltering by plaats starting with 'd':")
filtered_data = csv.filter(data, 'plaats', 'd')
print_filtered(filtered_data)
