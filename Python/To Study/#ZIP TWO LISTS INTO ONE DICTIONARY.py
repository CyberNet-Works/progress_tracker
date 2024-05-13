#ZIP TWO LISTS INTO ONE DICTIONARY
def lists_to_dict(list1, list2):

    combined_dict = {key: value for key, value in zip(list1, list2)} 

    return combined_dict

    #combined_dict = {key: value for key, value in zip(keys, values)} <-Zip more efficient more readable, less prone to index errors

    #combined_dict = {keys[i]: values[i] for i in range(len(keys))}
