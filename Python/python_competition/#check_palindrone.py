#check_palindrone.py
def is_palindrome(n):
    # write your code here
    n = [char for char in str(n)]
    return n == n[::-1]