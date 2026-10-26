# Day 01 - Python If-Else Statements
# Project: Rollercoaster Eligibility Checker

print("Welcome to the rollercoaster!\n")

# Ask the user for their height in centimeters
height = int(input("What is your height in cm?\n"))

# Check whether the user meets the minimum height
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("You need to grow taller to ride the rollercoaster!")
