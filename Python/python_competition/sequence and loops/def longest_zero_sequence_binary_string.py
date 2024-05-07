def longest_zero_sequence(binary_string):
    longest = 0
    current = 0

    for x in binary_string:
        if x == '0':
            current += 1
            longest = current
        else:
            current = 0

    return longest 
