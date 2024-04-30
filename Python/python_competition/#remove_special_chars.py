#remove_special_chars.py
def remove_special_chars(s):
    result = ""

    for char in s:
        if char.isalpha() or char.isnumeric() or char.isspace():
            result += char
        else:
            continue

    return result
