import pandas


def start():
    nato = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_dic = nato.to_dict()
    word = input("Your word: \n")
    print(word)
    print(nato_dic)
