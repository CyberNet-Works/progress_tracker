def valid_palindrome(s):
    word = list(s)

    for i, char in enumerate(word):
        edited_word = word[:i] + word[i+1:]

        if edited_word == edited_word[::-1]:
            return True 

    return False