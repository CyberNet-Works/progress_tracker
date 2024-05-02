import math


def max_value(s):


    nums = [int(char) for char in s.split() if char != ' ']


    return max(sum(nums), math.prod(nums))