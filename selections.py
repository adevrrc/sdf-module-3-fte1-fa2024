"""
Description: A script to demonstrate selections.
Author:
Date:
Usage: python selections.py
"""

age: int = 35
name: str = "Damien"

if age == 25:
    # Block starts here
    print(f"You are {age}")
    # Block end here

print("This is not part of the if statement.")

if age < 25:
    print("You are young.")
else:
    print("You are old")

print("This is not part of the if statement.")

age = 30

if age == 30:
    print("You have been alive for three decades.")
elif age == 40:
    print("You have been alive for four decades.")
elif name == "Damien":
    print("Hello Damien")
else:
    print("None of the other conditions were met.")

match age:
    case 30:
        print("You are thirty.")
    case 40:
        print("You are forty.")
    case 50:
        print("You are fifty.")
    case _:
        print("No match.")

name = "David"
age = 18

if age >= 25 or name == "Damien":
    print("You are a pretty cool guy.")

if not name.isalpha():
    print("The name is not valid.")

age = 19

if age <= 18:
    age_description = "young"
else:
    age_description = "old"

#age_description: str = "young" if age <= 18 else "old"

print(f"{name} you are {"young" if age <= 18 else "old"}.")

names = ["Damien", "James", "Kirk", "Rob"]

name = "James"

# Membership operator (in, not in)
if name in names:
    print("You are in the band.")
else:
    print("You are not allowed to be backstage.")

if name not in names:
    print("You are not part of the group.")
