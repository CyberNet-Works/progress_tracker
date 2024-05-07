#check_pandigital_number
def is_number_pandigital(num):
    
    number = "".join([char for char in str(num)])

    for x in number:
        if number.count(x) == 1 and "1234567890" in number:
            return True
        else:
            return False