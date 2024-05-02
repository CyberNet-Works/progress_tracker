def sum_nth_numbers(numbers, n):
	result = 0
	for x in range(n -1, len(numbers), n):
		result += numbers[x]

	return result