#is_list_subset.py
def is_subset(list1, list2):
    a = set(list1)
    b = set(list2)
    return a.intersection(b) == a