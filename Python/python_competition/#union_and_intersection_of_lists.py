#union_and_intersection_of_lists.py
def list_union_intersection(list1,list2):
    union = sorted(set(list1).union(set(list2)))
    intersection = sorted(set(list1).intersection(set(list2)))

    return (union, intersection)
