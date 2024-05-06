#check_if_theres_2_difference_in_list
def two_is_difference(numbers):
    result = None
    for x in numbers:
        for y in numbers:
            if x != y:
                if abs(x - y) == 2:
                    result = True

    return result