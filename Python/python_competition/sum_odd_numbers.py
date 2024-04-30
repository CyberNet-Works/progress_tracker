def sum_of_odds(numbers):
    result = 0
    for x in numbers:
        if x % 2 != 0:
            result += x

    return result
