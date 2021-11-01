import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)

print("You chose: \n")
print(choices[user_choice])
print("Computer chose: \n")
print(choices[comp_choice])
if user_choice == comp_choice:
    print("It's a draw!")
elif (user_choice == 0 and comp_choice == 1) or (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 0):
    print("You lose!")
else:
    print("You win!")
