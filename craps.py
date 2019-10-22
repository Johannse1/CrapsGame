# evan johanns
# craps game
#  10/21/19

import random


def create():
    bank_roll = int(input("How much do you have?:"))
    return bank_roll


def roll():
    dice = random.randint(1,7) + random.randint(1,7)
    return dice


def play_game():
    amount_bet = int(input("How much would you like to bet?: "))
    dice1 = roll()
    if dice1 == 7 or 11:
        print("You Win!")
    elif dice1 == 2 or 3 or 12:
        print("You Lost! :( Maybe next time!")
    else:
        point = dice1
        print(f"Your point is {point}")
        return

    dice2 = roll()










