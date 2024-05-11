#numeric seasaw

def numeric_seesaw(n):

    ascendingList = [num for num in range(1, n + 1)]

    return ascendingList[:-1] + ascendingList[::-1]