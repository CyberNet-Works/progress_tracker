#reverse_order_of_words

def reverse_words(s):

    words = s.split()
    result = []

    for i in range(len(words)):
        result.insert(0, words[i])

    return " ".join(result)