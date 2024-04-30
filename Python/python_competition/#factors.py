#factors.py
def get_factors(n):
    factorslist = []

    for x in range(1, n + 1):
        if n % x == 0:
            factorslist.append(x)

    return factorslist