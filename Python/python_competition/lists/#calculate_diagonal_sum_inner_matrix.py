#calculate_diagonal_sum_inner_matrix.py

def calculate_matrix_trace(matrix):
    sum_matrix = 0

    for inner_list in matrix:
        if inner_list == matrix[0]:
            sum_matrix += inner_list[0]
        if inner_list == matrix[1]:
            sum_matrix += inner_list[1]
        if inner_list == matrix[2]:
            sum_matrix += inner_list[2]

    return sum_matrix