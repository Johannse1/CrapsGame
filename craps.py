# evan johanns
# craps game
#  10/21/19

import random


def roll():
        dice = random.randint(1,7) + random.randint(1,7)
        return dice

def sim_games(n):
        wins = losses = 0
        for i in range(n):
            if game():
                wins = wins + 1
            if not game():
                losses = losses + 1
        return wins, losses

    #simulate one game

 def game():

            dice = roll()
            if dice == 2 or dice == 3 or dice == 12:
                return False
            elif dice == 7 or dice == 11:
                return True
            else:
                dice1 = roll()
                while dice1 != 7 or dice1 != dice:
                    if dice1 == 7:
                        return False
                    elif dice1 == dice:
                        return True
                    else:
                        dice1 = roll()
