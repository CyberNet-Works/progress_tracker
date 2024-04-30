#double_every_letter_in_string.py
def double_letters(s):
    result = ""
    for char in s:
        result += char * 2
    return result