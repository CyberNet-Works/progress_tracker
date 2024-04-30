def excuse_threes(n):
    result = []

    for x in range(1, n + 1):
        if x % 3 != 0:
            result += [x]

    return result