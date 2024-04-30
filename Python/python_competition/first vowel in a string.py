first vowel in a string

def get_first_vowel_index(str):
    # write your code here
    vowels = "aeioiAEIOU"

    dict1 = {}


    for key, value in enumerate(str):
        dict1[key] = value

    for x, y in dict1.items():
        if y in vowels:
            return x

