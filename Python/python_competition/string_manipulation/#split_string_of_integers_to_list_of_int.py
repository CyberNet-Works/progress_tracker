#split_string_of_integers_to_list_of_integers.py
def memorial_cost(prices):

    integers = [int(x) for x in prices.split()]

    return sum(integers)
