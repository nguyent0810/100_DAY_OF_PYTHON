############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run
import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n")
your_final_result = 0
comp_final_result = 0
your_cards = []
comp_cards = []
card_symbols = {
    "A": cards[0],
    "2": cards[1],
    "3": cards[2],
    "4": cards[3],
    "5": cards[4],
    "6": cards[5],
    "7": cards[6],
    "8": cards[7],
    "9": cards[8],
    "10": cards[9],
    "J": cards[10],
    "Q": cards[11],
    "K": cards[12]
}

def check_Ace(cards, result):
    if "A" in cards:
        if (result - 1) == 21:
            result = 21
        else:
            result = 0
            card_symbols["A"]  = 1
            for card in cards:
                result += card_symbols[card]
            while result < 17:
                new_card = random.choice(list(card_symbols.keys()))
                cards.append(new_card) 
                result += card_symbols[new_card]
    return result    

if is_play == 'y':
    for i in range(0, 2):
        your_cards.append(random.choice(list(card_symbols.keys()))) 
        comp_cards.append(random.choice(list(card_symbols.keys()))) 
    print(f"Your cards: {your_cards}")
    print(f"Computer's first card: {comp_cards[0]}")

    #Check that computer card is < 17
    for card in comp_cards:
        comp_final_result += card_symbols[card]
    while comp_final_result < 17:
        new_card = random.choice(list(card_symbols.keys()))
        comp_cards.append(new_card) 
        comp_final_result += card_symbols[new_card]
    if comp_final_result > 21:
        comp_final_result = check_Ace(comp_cards, comp_final_result)

    is_continue = True
    for card in your_cards:
        your_final_result += card_symbols[card]      
    while is_continue:
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: \n")
        if get_another_card == 'y':
            new_card = random.choice(list(card_symbols.keys()))
            your_cards.append(new_card) 
            your_final_result += card_symbols[new_card]
            print(f"Your cards: {your_cards}")
        elif get_another_card == 'n':
            print(f"Your final hands: {your_cards}")
            print(f"Computer's final hands: {comp_cards}")         
            if(your_final_result < 17):
                print("You have not reach the minimum value of blackjack. You lose!")
            else:
                if your_final_result > 21:
                    your_final_result = check_Ace(your_cards, your_final_result)


            print(f"Your final result {your_final_result}")
            print(f"Computer final result {comp_final_result}")
            if your_final_result > 21:
                if comp_final_result <= 21:
                    print("You lose")
                else:
                    print("It's a draw")
            elif your_final_result <= 21:
                if comp_final_result > 21:
                    print("You win")
                else:
                    if your_final_result > comp_final_result:
                        print("You win")
                    elif your_final_result < comp_final_result:
                        print("You lose")
                    else:
                        print("It's a draw")
            else:
                print("It's a draw")
            is_continue = False
else:
    print("See you next time!")