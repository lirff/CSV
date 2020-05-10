import csv

with open('Test_csv.csv') as csvfile:
    country_reader = csv.DictReader(csvfile, delimiter=';')
    for row in country_reader:
        print(row)