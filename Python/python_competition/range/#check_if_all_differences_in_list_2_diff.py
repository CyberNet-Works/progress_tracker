#check_if_all_differences_in_list_2_difference.py
def two_is_difference(numbers):
#    check_list = []

    for i in range(len(numbers) - 1):
#       check_list.append(abs(numbers[i] - numbers[i + 1]))
        if (abs(numbers[i] - numbers[i + 1])) != 2:
            return False
        else:
            return True