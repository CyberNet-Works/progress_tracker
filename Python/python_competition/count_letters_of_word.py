def count_letters(word):
    result = {}
    
    for key, value in enumerate(word):
        result[value] = word.count(value)
    
    return result
