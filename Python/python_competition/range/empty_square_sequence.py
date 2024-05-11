def empty_square_sequence(n):
    sequence = []

    for num in range(1, n + 1):

            sequence.append(((num + 1) ** 2) - (num ** 2))

    return sequence