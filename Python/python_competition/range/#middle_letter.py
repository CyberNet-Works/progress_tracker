#Middle_letter.py
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".


def mid(str):
    letters = [char for char in str if char.isalpha()]
    length = len(letters)
    middle_letter = ""
    
    if length % 2 == 0:
        middle_letter = ""
    else:
        middle_letter = letters[length // 2]
    
    return middle_letter

mid("this is a string")
