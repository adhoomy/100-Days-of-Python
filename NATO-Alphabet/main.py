import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def encode():
    word = input("Enter a word: ").upper()
    try:
        encoded_word = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        encode()
    else:
        print(encoded_word)


encode()
