#return_dictoinary_with_double_values
def max_pairs(n):
    result = {}
    for x in range(1, n + 1):
        result[str(x)] = x * 2
    return result