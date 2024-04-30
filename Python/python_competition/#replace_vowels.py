#replace_vowels.py
def replace_vowels(string, char):
    vowels = "AEIOUaeiou"

    result = ""

    for x in string:
        if x in vowels:
            result += char
        else:
            result += x

    return result

#    return ''.join(char if x in vowels else x for x in string)