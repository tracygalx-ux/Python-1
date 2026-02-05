#Challenge



try:
    principal = float(input("Please enter the principal amount: "))
    interest_rate = float(input("Please enter the interest rate: "))
    time = float(input("Please enter the time period: "))

    simple_interest = (principal * interest_rate * time) / 100
    print("The simple interest is", simple_interest)

except ValueError:
    print("Error: Please enter numeric values only.")