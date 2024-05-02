#shortest_word.property
def shortest_word(sentence):
    words = sentence.split()

    shortest_word = min(words, key=len)
    
    return shortest_word