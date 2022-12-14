import pandas

def start():
    data = pandas.read_csv("squirrel_data.csv")
    grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
    black_squirrels = data[data["Primary Fur Color"] == "Black"]
    print(grey_squirrels)
    print(black_squirrels)
