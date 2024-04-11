# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...
# opdr_1.py

# my_modules/csv.py

from my_modules import csv_operations

def main():
    # Example usage of the CSV module
    file_name = 'data.csv'

    # Writing data to a CSV file
    data = [{'Name': 'Alice', 'Age': 30, 'City': 'New York'},
            {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
            {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}]
    headers = ['Name', 'Age', 'City']
    csv_operations.write_csv(file_name, data, headers)

    # Reading data from a CSV file
    read_data = csv_operations.read_csv(file_name)
    print(read_data)

if __name__ == "__main__":
    main()
