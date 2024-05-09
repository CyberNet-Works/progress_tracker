def add_binary_strings(bin_str1, bin_str2):
    a = int(bin_str1, 2)
    b = int(bin_str2, 2)

    result = bin(a + b)[2:]

    return result