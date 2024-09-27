"""
Description: A script to demonstrate the for loop.
Author:
Date:
Usage: python for_loop.py
"""

THRESHOLD = 23
temperatures = [19, 23, 24, 18, 24, 29, 35, 35, 23, 27, 12, 16]
number_of_temperatures_below_threshold = 0

for temperature in temperatures:
    if temperature < THRESHOLD:
        number_of_temperatures_below_threshold += 1

print(number_of_temperatures_below_threshold)

uppercase_letter_count = 0
lowercase_letter_count = 0
whitespace_character_count = 0

phrase = input("Enter a phrase: ")

for character in phrase:
    if character.isupper():
        uppercase_letter_count += 1
    elif character.islower():
        lowercase_letter_count += 1
    elif character.isspace():
        whitespace_character_count += 1

print(f"Uppercase: {uppercase_letter_count}")
print(f"Lowercase: {lowercase_letter_count}")
print(f"Spaces: {whitespace_character_count}")

hockey_teams = {
    "winnipeg": "jets",
    "calgary": "flames",
    "edmonton": "oilers"
}

for number in range(0, 100, 5):
    print(number)
