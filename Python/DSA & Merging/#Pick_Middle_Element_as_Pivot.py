#Pick_Middle_Element_as_Pivot.py


def quick_sort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    else:
        mid = length // 2
        pivot = lst[mid]

    left = []
    right = []

    for i, element in enumerate(lst):
        if i == mid:
            continue
        elif element <= pivot:
            left.append(element)
        else:
            right.append(element)
    
    return quick_sort(left) + [pivot] + quick_sort(right)




# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)
print(sorted_list)


'''
Challenge:
Pick Middle Element as Pivot
Easy
Problem Description
Write a quick sort program that sorts elements in ascending order. However, choose the middle element as the pivot.

Create a function

Create a function named quick_sort() that takes a list as its argument.
Implement the quick sort algorithm with the middle element as the pivot.
Return the sorted list.
Print the returned list outside the function.
'''