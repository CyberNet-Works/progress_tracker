#find_missing_consecutive_integers
def consecutive_sequence(list1,list2):
    
    union = sorted(list(set(list1) | set(list2)))

    for i in range(len(union) - 1):
        start = min(union)
        if union[i] + 1 != union[i + 1]:
            return 'Not consecutive'

    return union