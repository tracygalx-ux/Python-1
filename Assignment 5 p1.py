'''
Assignment 5
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
'''


# Ask the user for time in hours
time_input = input("Enter a time duration in hours: ")

# Check if input is numeric
if time_input.isdigit():
    time = int(time_input)

    # Check if number is non- negative
    if time >= 0:
        minutes = time * 60
        seconds = time * 3600

        print("Time in minutes:", minutes)
        print("Time in seconds:", seconds)

else:
        print("Error: Time must be non-negative integer")


