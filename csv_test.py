# import csv
import pandas

def start():
#     ages = []
#     with open("csv_data.csv") as data_file:
#         data = csv.reader(data_file)
#         for row in data:
#             print(row[1])
#     data = pandas.read_csv("csv_data.csv")
#     age_list = data["age"].to_list()
#     the_age = data[data.age == 33]
#     print(the_age.name)
    data_dic = {
        "player": ["mario", "luigi", "bowser"],
        "score": [120, 76, 158]
    }
    data = pandas.DataFrame(data_dic)
