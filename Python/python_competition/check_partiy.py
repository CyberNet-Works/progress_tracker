def check_parity(number):
    digits = [int(char) for char in str(number)]

    return number % 2 == sum(digits) % 2 