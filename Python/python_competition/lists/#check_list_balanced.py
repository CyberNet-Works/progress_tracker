#check_list_balanced.py
def is_balanced(lst):
    mid = len(lst) // 2

    return len(lst[:mid]) == len(lst[mid:])