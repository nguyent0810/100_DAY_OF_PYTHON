import random 
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficult_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ")
total_attemps = 0
number = random.randint(1, 100)
is_continue = True
if difficult_chosen == "easy":
    total_attemps = 10
else:
    total_attemps = 5

while is_continue:
    print(f"You have {total_attemps} attempts remaining to guess the number")
    total_attemps -= 1
    user_guess = int(input("Make a guess: "))
    if total_attemps > 0:
        if user_guess > number:
            print("Too high.")
            print("Guess again.")
        elif user_guess < number:
            print("Too low.")
            print("Guess again")
        else:
            print(f"You got it. The answer was {number}.")
            is_continue = False
    else:
        is_continue = False
        print("You're run out of guesses, you lose.")