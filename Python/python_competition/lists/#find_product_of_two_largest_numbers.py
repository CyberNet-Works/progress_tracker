#find_product_of_two_largest_numbers.py
def product_of_largest(numbers):

    numbers = sorted(numbers, reverse = True)

    return numbers[0] * numbers[1]
