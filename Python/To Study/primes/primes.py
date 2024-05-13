def is_prime(n):
    if n <= 1:
        return False

    for factor in range(2, int(n ** 0.5) + 1):
        if n % factor == 0:
            return False

    return True

#    return False if n <= 1 else all(n % factor != 0 for factor in range(2, int(n ** 0.5) + 1))
