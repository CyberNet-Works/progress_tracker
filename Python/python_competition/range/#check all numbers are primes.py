#check all numbers are primes
def isPrime(number):
    prime = True

    for num in range(2, number):
        if number % num == 0:
            prime = False

    return prime

def all_primes(numbers):

    return all(isPrime(number) for number in numbers)
    # for number in numbers:
    #     if not isPrime(number):
    #         return False

    return True