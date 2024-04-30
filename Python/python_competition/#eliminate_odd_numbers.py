#eliminate_odd_numbers
def eliminate_odd_numbers(numbers):

    result = []

    for x in numbers:
        if x % 2 == 0:
            result.append(x)
    return result

# result = [x for x in numbers if x % 2 == 0]
#NOT BELOW!
# result = result.append(x) for x in numbers if x % 2 == 0
