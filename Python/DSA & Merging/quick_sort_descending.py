#quick_sort_descending.py
def quick_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        pivot = lst.pop()

    left = []
    right = []

    for element in lst:
        if element >= pivot:
            left.append(element)
        else:
            right.append(element)

    result = quick_sort(left) + [pivot] + quick_sort(right)
    return result

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)
print(sorted_list)