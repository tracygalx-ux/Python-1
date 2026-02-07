'''
Challenge: Implement error handling to ensure that the length and width
entered by the user are positive numbers.

=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula:
 Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''

#input

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

#processing

area = length * width

#Output

print("The area of the rectangle is ", area)

#challenge

if length > 0 and width > 0:
    area = length * width
    print("The area of the rectangle is ", area)
else:
    print("Error: Length and width must be positive numbers.")
