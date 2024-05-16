def isPrime(limit):
    primes = [num for num in range(2, limit) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return primes

#List all Primes up to limit

def primes_between(lower_limit, upper_limit):
    primes = [num for num in range(lower_limit, upper_limit + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1]
    return primes

# Write a function to check if a given integer is a prime number.
# Implement a function to generate the nth prime number.
# Create a program to find all prime numbers up to a given limit.
# Write a function to count the number of prime numbers within a given range.
# Implement a program to find the sum of all prime numbers up to a given limit.
# Create a function to find the product of all prime numbers up to a given limit.
# Write a program to find the largest prime factor of a given number.
# Implement a function to find the smallest prime factor of a given number.
# Create a program to find the prime factorization of a given number.
# Write a function to generate twin primes within a given range.
# Implement a program to find the nth Mersenne prime.
# Create a function to check if a given number is a safe prime.
# Write a program to find the prime gaps within a given range.
# Implement a function to generate palindromic primes within a given range.
# Create a program to find the prime quadruplets within a given range.
# Write a function to check if a given number is a Fermat prime.
# Implement a program to find the sum of the reciprocals of prime numbers up to a given limit.
# Create a function to find the prime digit sum of a given number.
# Write a program to find the Lucas-Lehmer sequence for a given Mersenne prime.
# Implement a function to check if a given number is a Sophie Germain prime.
