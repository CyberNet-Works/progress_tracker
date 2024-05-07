#List_to_dictionary_with_count_as_value
def word_order(words):
    word_count_dict = {}

    for keyvalue in words:
        
        word_count_dict[keyvalue] = words.count(keyvalue)

    return word_count_dict