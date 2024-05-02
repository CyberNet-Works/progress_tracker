def sum_of_digits(start, end):

	results = []

	for num in range(start, end + 1):
		results += [num]

	sumdigits = sum([int(char) for char in str(results) if char.isdigit()])

	
	return sumdigits