#return_max_list_of_lists.py
def find_largest(lists):
    result = []

    for lista in lists:
        result.append(max(lista))

    return result

#result = [max(lista) for lista in lists]
