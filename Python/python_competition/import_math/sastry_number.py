import math
def is_sastry(n):
	num = int(str(n) + str(n + 1))
	sqrt = math.isqrt(num)

	return sqrt * sqrt == num