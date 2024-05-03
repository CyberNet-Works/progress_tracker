def single_occurrence(s):
    string = s

    for index in range(len(string)):
        if string[index] == string[index + 1] and string.count(string[index]) == 1:
            continue
        else:
            return string[index]