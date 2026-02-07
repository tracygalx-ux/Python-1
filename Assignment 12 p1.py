'''
Assignment 12
Challenge: Use nested loop structures to print the pattern efficiently and neatly.
Allow the user to specify the character used for the pattern.

=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern
and then prints a pattern of asterisks (*) in the form of a right triangle.
'''


# Ask user for number of rows
rows_input = input("Enter number of rows: ")

# Validate input
while True:
    if rows_input.isdigit():
        rows = int(rows_input)
        if rows > 0:
            break
    rows_input = input("Please enter a positive integer: ")

# Ask user for character
character = input("Enter a character for the pattern: ")
print("Pattern: ")

# Nested loops to print triangle
for i in range(1, rows + 1):
    for s in range(rows -i):
        print("", end="")
    for j in range(i):
        print(character, end="")
    print()

