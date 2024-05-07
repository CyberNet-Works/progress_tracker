#group_similar_items_from_list_to_dictionary

def group_items(lst):
    result_dict = {}

    for idx, value in enumerate(lst):
        if value not in result_dict:
            result_dict[value] = []
        result_dict[value].append(idx)

    return result_dict
