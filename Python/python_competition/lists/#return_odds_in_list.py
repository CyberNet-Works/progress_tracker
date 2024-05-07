#return_odds_in_list
def odd_numbers(numbers):

    odds = []

    for x in numbers:
        if x % 2 != 0:
            odds += [x]

    return odds