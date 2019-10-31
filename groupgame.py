# group: Evan Johanns, Luis Martinez
# Dice Game
# 10/31/19

import random


def roll():
    num = random.randint(1,6)
    return


def play_game():
    p1_points = 0
    p2_points = 0
    while p1_points < 6 or p2_points < 6:
        player_one = roll()
        player_two = roll()
        print(f"player ones roll: {player_one}")
        input("press enter to roll again:")
    if player_one > player_two:
        p1_points + 1


