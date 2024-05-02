#evens_and_odd_indices
def index_shuffle(txt):
    evens = []
    odds = []

    for index, letter  in enumerate(txt):
        if index % 2 == 0:
            evens.append(letter)
        else:
            odds.append(letter)

    result = "".join(evens + odds)

    return result 