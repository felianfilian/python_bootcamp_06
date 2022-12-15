import pandas


def start():
    nato = pandas.read_csv("nato_phonetic_alphabet.csv")
    phon_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
    word = input("Your word: \n").upper()
    nato_trans = {phon_dict[letter] for letter in word}
    print(nato_trans)
