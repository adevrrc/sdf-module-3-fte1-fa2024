"""
Description: A script to demonstrate boolean expressions.
Author:
Date:
Usage: python boolean_expressions.py
"""
print(True)
print(False)

is_deron_here: bool = True
print(is_deron_here)

name: str = "Damien"
print(name.isalpha())
print(name.isdigit())

age: int = 25

print(age == 25)
print(age == 35)
print(age != 35)
print(age < 14)
print(age <= 25)
print(age > 14)
print(age >= 100)

are_you_old: bool = age >= 100
