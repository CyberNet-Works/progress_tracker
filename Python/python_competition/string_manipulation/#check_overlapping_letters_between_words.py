#check_overlapping_letters_between_words
def check_overlap(sentence):
    chars = [char for char in sentence]

    for index in range(len(chars) - 2):
        if chars[index + 1] == ' ':
            if chars[index] != chars[index + 2]:
                return False
    
    return True