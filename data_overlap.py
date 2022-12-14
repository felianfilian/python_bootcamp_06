
def start():
    print("data overlap")
    with open("./data_overlap/file01.txt") as num01:
        data01 = num01.read().splitlines()
    with open("./data_overlap/file02.txt") as num02:
        data02 = num02.read().splitlines()
    new_list = [int(n) for n in data01 if n in data02]
    print(new_list)



