# evan johanns
# craps game
#  10/21/19

import random


def create():
    bank = int(input("How much would you like to enter into the bank?: ")) # asks for how much you have
    return bank


def roll():
    dice = random.randint(1,6) + random.randint(1,6) # rolls dice
    return dice


def play_again():
    choice = input("Would you like to play again?: ") # asks if the player wants to play again
    if choice == 'yes' or choice == 'sure':
            play_game()
    else:
        return
    return


def play_game():
    bank = create()
    bet = int(input("How much would you like to bet?: ")) #starts game and asks for bet
    while bet < 0: # error trapping for invalid bet

        print("Invalid input, try again:")
        bet = int(input())
    dice1 = roll()
    while bank > 0 and bet > 0: # checks for win and lose conditions, otherwise sets first roll as point and continues on
        if dice1 == 7 or dice1 == 11:
            print(f"You Win with a roll of {dice1}!")
            bank = bank + bet
            print(f"Bank = {bank}")
            play_again()

            return
        elif dice1 == 2 or dice1 == 3 or dice1 == 12:
            print(f"You Lost with a roll of {dice1}! :( Maybe next time!")
            bank = bank - bet
            print(f"Bank = {bank}")
            play_again()
        else:
            point = dice1
            print(f"Your point is {point}")
            dice2 = roll()
            while point != dice2 and dice2 != 7: # checks for second win and lose conditions until you have
                print(f"You rolled a {dice2}.")
                dice2 = roll()
            if dice2 == point:
                    print(f"You Win with a roll of {dice2}!")
                    bank = bank + bet
                    print(f"Bank = {bank}")
                    play_again()
                    return
            else:
                    print(f"You Lost a roll of {dice2}! :( Maybe next time!")
                    bank = bank - bet
                    print(f"Bank = {bank}")
                    play_again()
                    return
    if bank <= 0:
        print("Your out of money! Thanks for playing!")
        play_again()

    return


play_game()




