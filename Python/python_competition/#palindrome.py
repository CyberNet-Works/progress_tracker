#palindrome.py
def is_palindrome(n):
    result = [char for char in str(n)]

    return result == result[::-1]