'''
Assignment 17
Challenge: Optimize the function to handle large input lists efficiently.

==============================
Description: Develop a function called find_common_elements that takes
two lists as input and returns a new list containing elements that are common
to both input lists.
'''


def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2 = [1,2,3,4,5,6,]
print(find_common_elements(list1, list2))


