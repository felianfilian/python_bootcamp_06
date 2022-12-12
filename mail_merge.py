

def start():
    file = open("mail_names.txt", mode="r")
    names = file.readlines()
    print(names)
    file_02 = open("./output/letter.txt", mode="r")
    letter = file_02.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter.replace("[name]", strip_name)
        print(new_letter)
        # print(F"hello {names[name]}")

