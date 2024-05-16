def fibonacci_less_than(n):
    sequence = [0, 1]

    if n == 1:
        return [0]
    else:

        while sequence[-1] < n:

            next_sequence = sequence[-1] + sequence[-2]
            if next_sequence < n:
                sequence.append(next_sequence)
            else:
                break

    return sequence