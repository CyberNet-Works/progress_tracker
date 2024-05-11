def binary_toggle(n):
    n = bin(n)[2:]

    # swaps = ""

    # for x in n:
    #     if x == '0':
    #         swaps += '1'
    #     else:
    #         swaps += '0'

    swaps = ''.join(['1' if x == '0' else '0' for x in n])

    converted_swap = int(swaps, 2)

    return converted_swap

