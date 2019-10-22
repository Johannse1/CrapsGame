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


def playGame():
    amount_bet = int(input("How much would you like to bet?: "))



