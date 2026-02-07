'''
Assignment 13
Challenge: Use a loop structure to compare characters from both ends of the string to determine whether
it is a palindrome.

===================================
Description: Write a program that prompts the user to enter a string and then checks whether
it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the
same forward and backward.
'''

# Ask user to enter a string
text = input("Enter a string: ")

# Assume it is a palindrome
is_palindrome = True

# Set starting and ending index
left = 0
right = len(text)-1

# Compare characters from both ends
while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

#Results
if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")