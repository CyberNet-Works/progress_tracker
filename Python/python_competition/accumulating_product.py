def accumulating_product(numbers):
    # write your code here
    result = 1
    results = []

    for x in numbers:
        result *= x
        results.append(result)

    return results