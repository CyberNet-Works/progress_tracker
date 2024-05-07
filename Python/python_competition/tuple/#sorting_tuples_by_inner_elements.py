#sorting_tuples_by_inner_elements
def sort_tuples(tuples):
    sorted_tuples = []

    sorted_tuples = sorted(tuples, key=lambda x: x[1])

    return sorted_tuples