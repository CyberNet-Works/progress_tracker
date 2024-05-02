def filter_integers(lst):
	return [int(item) for item in str(lst) if item.isnumeric()]