def first_vowel_index(s):
	string1 = s
	
	for index in range(len(string1)):
		if string1[index].lower() in "aeiou":
			return index