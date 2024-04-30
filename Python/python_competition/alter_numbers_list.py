def alter_numbers(numbers):
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x / 2)
        else:
            result.append(x - 1)

    return result