def has_consecutive_letters(s):
	consecutive = False
	string = s
	length = len(string)

	for x in range(length - 1):
		if string[x] == string[x + 1]:
			consecutive = True

	return consecutive