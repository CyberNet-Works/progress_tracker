#factorial.py
def factorial(n):
    # write your code here
    result = 1

    for factorial in range(1, n + 1):
        result *= factorial

    return result

#    return 1 if n == 0 else n * factorial(n - 1)