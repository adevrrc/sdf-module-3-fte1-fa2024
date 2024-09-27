"""
Description: A script to demonstrate python modules; math and random.
Author: Damien Altenburg
Date: 2024-9-27
Usage: python python_modules.py
"""
from math import isqrt, pow
from random import randint

teams = ["jets", "flames", "oilers", "canucks", "senators", "canadians"]

print(isqrt(64))
print(pow(2, 3))

player_dice = []

for number in range(5):
    die_roll = randint(1, 6)
    player_dice.append(die_roll)

print(player_dice)
