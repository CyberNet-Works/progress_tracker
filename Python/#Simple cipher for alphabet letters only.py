#Simple cipher for alphabet letters only
#Returns lowercase unicode value, adjusted from 96 to 1
#Non-alpha characters added w/out translation.

def replace_with_position(s):
    return ' '.join(str(ord(letter) - 96) if letter.isalpha() else letter for letter in s.lower())
