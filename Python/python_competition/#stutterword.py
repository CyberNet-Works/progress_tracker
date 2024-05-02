#stutterword
def stutter(word):
    first_letters = word[0:2] + "... "

    stutter_word = first_letters * 2 + word  + "??"

    return stutter_word