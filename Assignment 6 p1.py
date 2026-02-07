'''
Assignment 6
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error
handling for invalid currency inputs.

==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
'''

# Ask user to choose currency pair
print("Choose a currency conversion")
print("1. USD to EUR")
print("2. USD to PEN")

choice = input("Enter your choice (1-2): ")

# Check if choice is valid
if choice.isdigit():
    choice = int(choice)
    if 1 <= choice <= 2 :
        amount_input =input("Enter amount in USD:")

        #Check if amount is numeric (allow decimals)
        if amount_input.isdigit():
            amount = float(amount_input)
            if amount >= 0:
                if choice ==1:
                    converted = amount * 0.92
                    print("Converted amount in EUR:", converted)
                elif choice ==2:
                    converted = amount * 3.75
                    print("Converted amount in PEN:", converted)
            else:
                print("Error:Amount must be non-negative integer")
        else:
            print("Error: Please enter a valid number for amount.")
    else:
        print("Error: invalid choice, choose from 1-2")
else:
    print("Error: Please enter a number for choice")
