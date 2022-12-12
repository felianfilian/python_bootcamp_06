

def start():
    file = open("mail_names.txt", mode="r")
    names = file.read().splitlines()
    print(names)

