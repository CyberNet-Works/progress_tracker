#partition_pivot_around_last_list_element.py
def moving_partition(lst):
    last_element = lst.pop()
    left = []
    right = []

    for element in lst:
        if element < last_element:
            left.append(element)
        else:
            right.append(element)

    return left + [last_element] + right