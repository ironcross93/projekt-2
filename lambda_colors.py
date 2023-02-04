import csv
import json

# Utwórz pusty słownik, w którym będą przechowywane dane z plików CSV
data = {}

# Pobierz dane z pierwszego pliku CSV i dodaj je do słownika
with open('example.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        color = row['color']
        hex_value = row['value']
        data[color] = hex_value

# Pobierz dane z drugiego pliku CSV i dodaj je do słownika
with open('example1.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        color = row['color']
        hex_value = row['value']
        data[color] = hex_value

# Pobierz dane z trzeciego pliku CSV i dodaj je do słownika
with open('example2.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        color = row['color']
        hex_value = row['value']
        data[color] = hex_value

# Konwertuj słownik na plik JSON i zapisz go do pliku
with open('colors.json', 'w') as json_file:
    json.dump(data, json_file)
