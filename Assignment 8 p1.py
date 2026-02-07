'''
Assignment 8
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each
subject.

=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.
'''


# Ask the user to enter marks for three subjects
mark1_input = input("Enter marks for subject 1: ")
mark2_input = input("Enter marks for subject 2: ")
mark3_input = input("Enter marks for subject 3: ")

# Check if all inputs are numeric
if mark1_input.isdigit() and mark2_input.isdigit() and mark3_input.isdigit():
    mark1 = int(mark1_input)
    mark2 = int(mark2_input)
    mark3 = int(mark3_input)

# Check if marks are between 0 and 100
    if 0 <=mark1 <= 100 and 0<=mark2<=100 and 0<=mark3<=100:
        average = (mark1+mark2+mark3)/3

        # Determine the grade
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"
        print("Average Grade: ", average)
        print("Grade: ", grade)

    else:
        print("Error: Marks must be between 0 and 100")
else:
    print("Error: Please enter valid numeric marks.")