#return_keys_and_values_in_separate_lists_tuple
def dict_to_lists(dict):
    keys = [x for x in dict.keys()]
    values = [x for x in dict.values()]

    result = keys, values

    return result