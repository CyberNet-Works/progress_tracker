#reverse_binary_string
def reverse_binary(n):
    binary = bin(n)[2:]

    reversed_binary = ''.join([char for char in binary][::-1])

    converted_binary = int(reversed_binary, 2)

    return converted_binary