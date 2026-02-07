'''
Assignment 16
Challenge: Optimize the function to handle large input numbers efficiently.

=====================================================
Description: Develop a function called is_prime that takes a positive integer as
input and returns True if it is a prime number, and False otherwise.
'''


def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i = i + 1
    return True
number = int(input("Enter a positive integer: "))
if is_prime(number):
    print("True")
else:
    print("False")