def remove_character(str,i):
    # write your code here
    words = [char for char in str]
    words.pop(i)

    result = "" 

    for char in words:
        result += "".join(char)

    return result