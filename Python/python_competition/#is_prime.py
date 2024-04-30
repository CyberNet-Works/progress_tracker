#is_prime
def is_prime(n):
    prime = True

    for x in range(2, n):
        if n % x == 0:
            prime = False

    return prime