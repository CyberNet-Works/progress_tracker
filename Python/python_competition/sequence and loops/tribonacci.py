def tribonacci(n):
    sequence = [0, 1, 1]

    for i in range(3, n):
        next_trib = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        if next_trib <= n:
            sequence += [next_trib]
        else:
            break 

    sum_sequence = sum(sequence)
    return sum_sequence