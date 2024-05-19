#convert numbers string stream to list and sum
def memorial_cost(prices):
    prices_list = prices.split()
    integer_price_list = []

    # for element in prices_list:
    #     element = int(element)
    #     integer_price_list.append(element)
    integer_price_list = [int(element) for element in prices_list]

    return sum(integer_price_list)