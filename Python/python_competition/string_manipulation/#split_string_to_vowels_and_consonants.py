#split_string_to_vowels_and_consonants.py

def split_string(s):
    left = []
    right = []

    for char in s:
        if char.lower() in "aeiou":
            left.append(char)
        elif char.lower() in "bcdfghjklmnpqrstvwxyz":
            right.append(char)
    left = "".join(left)
    right = "".join(right)
    
    return (left, right)