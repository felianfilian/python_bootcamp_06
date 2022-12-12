import csv

def start():
    ages = []
    with open("csv_data.csv") as data_file:
        data = csv.reader(data_file)
        for row in data:
            print(row[1])