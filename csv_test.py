import pandas

def start():
    data = pandas.read_csv("squirrel_data.csv")
    grey_squirrels = data[data["Primary Fur Color"] == "Grey"]
    print(grey_squirrels)
