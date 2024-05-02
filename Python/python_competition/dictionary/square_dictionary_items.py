#convert list to dictionary with square values 
def numbers_to_dict(numbers):
	data = {}

	for x in numbers:
		data[str(x)] = x ** 2

	return data