

def start():
    file = open("mail_names.txt", mode="r")
    names = file.read().splitlines()
    print(names)
    file_02 = open("./output/letter.txt", mode="r")
    for name in range(len(names)):
        letter = file_02.read()
        letter.replace("[name]", names[name])
        print(letter)
        # print(F"hello {names[name]}")

