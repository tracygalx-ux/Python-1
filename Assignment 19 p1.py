'''
Assignment 19
Challenge: Implement the sorting algorithm without using any built-in sorting functions.

====================================
Description: Develop a function called sort_list that takes a list of numbers as input
and returns a new list containing the
same elements sorted in ascending order.
'''


def sort_list(numbers):
    new_list = numbers[:]

    for i in range(len(new_list)):
        for j in range(len(new_list)-1):
            if new_list[j] > new_list[j+1]:

                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
    return new_list
numbers = [5,2,9,1,6]
print(sort_list(numbers))
