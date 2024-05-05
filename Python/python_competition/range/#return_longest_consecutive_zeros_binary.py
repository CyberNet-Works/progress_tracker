#return_longest_consecutive_zeros_binary_string.py
def longest_zero_sequence(binary_string):
    count = 0
    length = len(binary_string)
    data = []

    for i in range(0, length):
        if binary_string[i] == '0':
            count += 1
        else:
            data.append(count)
            count = 0

    return max(data)
            
            
