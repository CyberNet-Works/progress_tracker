def replace_item(lst, old_item, new_item):
    result = [new_item if x == old_item else x for x in lst]

    return result

def replace_item(lst, old_item, new_item):
    for index, value in enumerate(lst):
        if value == old_item:
            lst[index] = new_item
    return lst
