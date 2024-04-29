#Linear_Search_Algorithm.py


def linear_search(lst, target):
    result = None

    if target in lst:
        for i, x in enumerate(lst):
            if x == target:
                result = i

    return result

lst = [9, 10, 5, 8, 7, 4, 11, 6, 15, 3]

# take integer input to search in the list
target_value = int(input())

result = linear_search(lst, target_value)
print(result)

'''
Linear Search Algorithm
Easy
Problem Description
Can you create a program to perform a linear search on your own?

Create a function named linear_search() that takes two arguments: a list and an integer, target.
Return the index of target if found in the list. If target is not present, return None.
Print the result (either the index or None if the target value is not found) outside the function.
Note: We will use a predefined list, [9, 10, 5, 8, 7, 4, 11, 6, 15, 3], for this challenge. The target value to search for will be taken from the user input.

Example
Test Input

5
Expected Output

2
'''