#fill_in_missing_elements_with_zeros.py
def complete_square(matrix):
    
    max_len = matrix[0]

    for i in range(len(matrix) - 1):
        if len(matrix[i]) > len(max_len):
            max_len = (matrix[i])

    for i in range(len(matrix)):
        if len(matrix[i]) < len(max_len):
            dif = len(max_len) - len(matrix[i])
            matrix[i] += [0] * dif

    return matrix
            