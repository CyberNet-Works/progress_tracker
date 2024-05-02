def positive_dominant(lst):

    pos = set()
    neg = set()

    for num in lst:
        if num < 0:
            neg.add(num)
        elif num > 0:
            pos.add(num)

    return len(pos) > len(neg)
        
