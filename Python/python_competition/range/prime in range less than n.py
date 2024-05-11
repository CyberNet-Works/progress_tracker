def isPrime(candidate):
    isprime = True
    for x in range(2, (candidate // 2) + 1):
        if candidate % x == 0:
            isprime = False

    return isprime


def count_primes(n):
    count = 0
    for num in range(2, n):
        if isPrime(num):
            count += 1

    return count