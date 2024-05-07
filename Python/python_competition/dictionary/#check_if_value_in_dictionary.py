#check_if_value_in_dictionary
def value_exist(dict1, val):
    values = [x for x in dict1.values()]

    result = val in values

    return result