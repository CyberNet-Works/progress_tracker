#sum_evens_in_list_of_lists_matrix.py
def sum_of_evens(matrix):
    result = 0

    for i in range(len(matrix)):
        for x in matrix[i]:
            if x % 2 == 0:
                result += x

    return result