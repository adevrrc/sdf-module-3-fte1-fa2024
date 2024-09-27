"""
Description: A script to demonstrate file input.
Author: Damien Altenburg
Date: 2024-9-27
Usage: python file_input.py
"""
file_path: str = "./data/data.txt"

people_to_hack = open(file_path, 'r')

data: str = people_to_hack.read()

people_to_hack.close()

#print(data)

people_to_hack = open(file_path, 'r')

#print(people_to_hack.readline())

for line in people_to_hack:
    print(line.rstrip())

people_to_hack.close()
