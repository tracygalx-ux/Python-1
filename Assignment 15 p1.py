'''
Assignment 15
Challenge: Write the function using recursion.

===================================
Description: Create a function named is_palindrome
that takes a string as input and returns True if it is a palindrome, and False otherwise.
'''


def is_palindrome(text):

    # Base case : if string length is 0 or 1
    if len(text) <= 1:
        return True
    # If first and last characters differ
    if text[0] != text[-1]:
        return False
    # Recursive call on smaller substring
    return is_palindrome(text[1:-1])

word = input("Enter a string:")
if is_palindrome(word):
    print("True")
else:
    print("False")