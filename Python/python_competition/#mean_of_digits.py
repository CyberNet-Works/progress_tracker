#mean_of_digits
def mean_of_digits(n):
    str_converted_number = [char for char in str(n)]
    result = 0

    for num in str_converted_number:
        result += int(num)

    return result / len(str_converted_number)