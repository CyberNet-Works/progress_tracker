#check_two_digit_number_has_even_and_odd
def check_number(n):
    result = [char for char in str(n)]
    a = int(result[0]) % 2
    b = int(result[1]) % 2

    return (a == 0 and b == 1) or (b == 0 and a == 1)