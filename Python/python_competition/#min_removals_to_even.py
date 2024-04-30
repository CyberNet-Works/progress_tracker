#min_removals_to_even.py

def min_removals(numbers):
    if sum(numbers) % 2 == 0:
        return 0
    else:
        return 1