# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
try:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
except:
    print("The file is not exist" )
#TODO 1. Create a dictionary in this format:
else:
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()   
    try: 
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error:
        print(f"Your input {error} is invalid. Only allow alphabet input. Please try again")
        generate_phonetic()
    else:
        print(output_list)
        is_valid_input = True

generate_phonetic()
