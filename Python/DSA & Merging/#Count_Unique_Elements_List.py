#Count_Unique_Elements_List.py  

# Replace ___ with your code

def count_unqiue_elements(lst):

    # get counting list
    max_element = max(lst)
    counting_list = [0] * (max_element + 1)

    for num in lst:
        counting_list[num] += 1

    # count unqiue elements using counting_list
    unqiue_count = 0
    unique_output = []
    
    for index, value in enumerate(counting_list):
        unique_output.extend([index] * value)
        result = len(set(unique_output))
   
    return result


# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = count_unqiue_elements(data_list)
print(sorted_list)
'''
Challenge:
Count Unique Elements in a List
Easy
Problem Description
Create a program to find the number of unique elements in a list.

Create a function named count_unqiue_elements() to count the number of unique elements in a list.
The count_unique_elements() function should accept a single argument, a list. It will return the count of unique elements.
Print the result from outside the function.
For instance, [10, 20, 10, 20, 20, 20, 30] contains three unique elements: 10, 20 and 30.

Assumption: The input list will only contain non-negative integers.

Hint: Once we create the counting list, it becomes much easier to solve this problem.

Example
Test Input

4 2 2 1 3 2 4 4 1 5
Expected Output

5

'''

