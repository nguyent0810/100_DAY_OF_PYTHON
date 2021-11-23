import pandas
student_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(student_dict)


#Loop through rows of a data frame
nato_alphabet_dict = {row.letter:row.code for (index, row) in student_data_frame.iterrows()}

user_name = input("Enter a word: ").upper()
list_word = [item for item in user_name]

#result = [code for (letter, code) in nato_alphabet_dict.items() if letter in list_word]
result = [nato_alphabet_dict[item] for item in list_word if item in nato_alphabet_dict.keys()]
print(result) 
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

