#quick_sort.py
def quick_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        pivot = lst.pop()

    left = []
    right = []

    for element in lst:
        if element > pivot:
            right.append(element)
        else:
            left.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)
print(sorted_list)


'''
#quick_sort.py
def quick_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        pivot = lst.pop()

    left = []
    right = []

    for element in lst:
        if element > pivot:
            right.append(element)
        else:
            left.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)
print(sorted_list)
'''