#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as data:
    letter = data.read()
names = open("./Input/Names/invited_names.txt")
print(names)
list_names = names.readlines()
new_list_names = []
for name in list_names:
    name = name.replace("\n","")
    new_list_names.append(name)
for name in new_list_names:
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as data:
        new_letter = letter.replace("[name]", name)
        data.write(new_letter)