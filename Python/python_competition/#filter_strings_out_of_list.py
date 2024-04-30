#filter_strings_out_of_list.py
def filter_strings(lst):
    result = [int(item) for item in str(lst) if item.isnumeric()]

    return result