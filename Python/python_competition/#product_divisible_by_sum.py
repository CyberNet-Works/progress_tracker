#product_divisible_by_sum.py

import math
def is_divisible(numbers):
    return math.prod(numbers) % sum(numbers) == 0 