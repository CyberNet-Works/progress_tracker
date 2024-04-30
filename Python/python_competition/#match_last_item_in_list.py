#match_last_item_in_list.py
def match_last_item(lst):
    result = ""

    for x in lst[0:-1]:
        result += x

    return result == lst[-1]