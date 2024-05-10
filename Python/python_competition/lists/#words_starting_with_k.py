#words_starting_with_k
def extract_k_words(words):
    k_words = []

    for word in words:
        if word[0] == "K":
            k_words.append(word)



    return k_words