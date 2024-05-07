def capital_indexes(str):
    words = list(str)
    capital_indexes = []
    
    for index, word in enumerate(words):
        if word[0].isupper():
            capital_indexes.append(index)
    return capital_indexes
        