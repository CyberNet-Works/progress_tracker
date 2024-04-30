#repeat_vowels_in_a_string.py
def repeat_vowels(string):
    vowels = "AEIOUaeiou"

    result = ""

    for x in string:
        if x in vowels:
            result += x * 2
        else:
            result += x
    return result