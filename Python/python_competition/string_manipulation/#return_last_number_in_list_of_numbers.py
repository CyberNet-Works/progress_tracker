#return_last_number_in_list_of_numbers.py

def end_letters(numbers):
    result = []

    for x in numbers:
        last_num = [char for char in str(x)]
        result += last_num[-1]

    return result