"""
Description: A script to demonstrate the while loop.
Author:
Date:
Usage: python while_loop.py
"""
new_password = "new_password"
confirm_password = "confirm_password"

while new_password != confirm_password:
    new_password = input("Enter the new password: ")

    confirm_password = input("Confirm password: ")

    print("Confirmation not successful. Try again." if \
          new_password != confirm_password else \
          "Password Updated!")
