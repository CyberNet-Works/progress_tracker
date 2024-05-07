#convert_letters_in_strng_to_dictionary_with_letter_key_and_ascii_value.py
def ascii_dictionary(string):
    
    letters = [x for x in string]

    ascii_dict = {}

    for x in range(len(letters) + 1):
        for letter in letters:
            ascii_dict[letter] = ord(letter)
    
    #ascii_dict = {letter: ord(letter) for x in range(len(letters) + 1) for letter in letters}  

    return ascii_dict
