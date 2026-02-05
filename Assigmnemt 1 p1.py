'''
Assignment 1
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate,
or time period, and provide appropriate error messages.

=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
'''

# We will be handling the input section below
principal = float(input("Please enter the principal amount: "))
interest_rate = float(input("Please enter the interest rate: "))
time = float(input("Please enter the time period: "))

#This is the processing phase below
simple_interest = (principal * interest_rate * time) / 100

# The output section is below

print("The simple interest is", simple_interest)




