# import csv
import pandas

def start():
#     ages = []
#     with open("csv_data.csv") as data_file:
#         data = csv.reader(data_file)
#         for row in data:
#             print(row[1])
    data = pandas.read_csv("csv_data.csv")
    print(data)
    print(data["name"])
