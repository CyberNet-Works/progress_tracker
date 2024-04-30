def is_pronic(n):
    result = False

    for x in range(0, n + 1):
        if x * (x + 1) == n:
            result = True

    return result