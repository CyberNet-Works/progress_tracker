def first_n_vowels(string, n):
    vowels = 'aeiouAEIOU'


    string = list(string)

    result = []
    count = 0

    for char in string:
        if char in vowels:
            result += [char]
            count += 1
            if count == n:
                break

    return result if len(result) > 0 else "Not found"
