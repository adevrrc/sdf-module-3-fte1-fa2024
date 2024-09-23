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

