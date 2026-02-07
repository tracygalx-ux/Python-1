'''
Assignment 9
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.

=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
'''

# Ask the user to enter a character
char_input = input("Enter a single character: ")

# check if the user entered exactly one character and that is a letter
if len(char_input)==1 and char_input.isalpha():
    char = char_input.lower()

    # check if the character is a vowel
    if char in "aeiou":
        print("It is a vowel")
    else:
        print("It is a consonant")

else:

    if len(char_input) != 1:
        print("Error: Please enter a single character")
    else:
        print("Error: The input is not a letter")
