import pandas


def start():
    nato_trans = ""
    nato = pandas.read_csv("nato_phonetic_alphabet.csv")
    phon_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

    def generate_phon():
        word = input("Your word: \n").upper()
        try:
            nato_trans = {phon_dict[letter] for letter in word}
        except KeyError:
            print("please use valid letters")
            generate_phon()
        else:
            print(nato_trans)

    generate_phon()
