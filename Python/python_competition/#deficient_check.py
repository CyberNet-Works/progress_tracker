#deficient_check
def is_deficient(n):
    factors = []
    for x in range(1, n):
        if n % x == 0:
            factors.append(x)

    return sum(factors) < n