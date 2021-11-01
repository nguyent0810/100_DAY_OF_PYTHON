#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def random_generator(number, list_choice):
    rd_string = ""
    for l in range(0, number):
        rd_string += random.choice(list_choice)
    return rd_string
rd_letters = random_generator(nr_letters, letters)
rd_symbols = random_generator(nr_symbols, symbols)
rd_numbers = random_generator(nr_numbers, numbers)

eazy_pass = rd_letters + rd_symbols + rd_numbers

print(f"The eazy password is {eazy_pass}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
sample_pass = random.sample(eazy_pass,len(eazy_pass))
# hard_pass = ""
# for c in sample_pass:
#     hard_pass += c
# random.shuffle(sample_pass)
hard_pass = ''.join(sample_pass)
print(f"The hard password is {hard_pass}")