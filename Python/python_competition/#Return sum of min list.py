#Return sum of min list
def sum_of_min_values(lst):
    min_list = []

    for x in lst:
        min_list += [min(x)]


    return sum(min_list)

#    min_list = [min(x) for x in lst]
