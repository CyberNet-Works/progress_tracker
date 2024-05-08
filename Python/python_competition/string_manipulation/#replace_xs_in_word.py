#replace_xs_in_word
def pronounce_xs(s):
    characters = list(s)

    if characters[-1] == 'x':
        characters[-1] = 'k'

    for i in range(len(characters) - 1):
        if characters[i] == 'x' and characters[i + 1] in 'aeiou':
            characters[i] = 'cks'
        
        if characters[i] == 'x' and characters[i + 1] not in 'aeiou':
            characters[i] = 'k'
        

    return "".join(characters)