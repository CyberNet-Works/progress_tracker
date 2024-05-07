#primes_to_a_given_number
def is_prime(n):
    prime = True
    for x in range(2, n):
        if n % x == 0:
            prime = False
    return prime

def primes_below(n):
    primes = []
    for x in range(2, n + 1):
        if is_prime(x):
            primes.append(x)

    return primes
