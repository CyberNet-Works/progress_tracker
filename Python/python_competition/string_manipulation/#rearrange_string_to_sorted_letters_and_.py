#rearrange_string_to_sorted_letters_and_sum_numbers

def rearrange_string(s):
    split_s = [char for char in str(s)]

    letters = []
    numbers = 0

    for x in split_s:
        if x.isalpha():
            letters += [x]
        elif x.isnumeric():
            numbers += int(x)

    
    return "".join(sorted(letters)) + str(numbers) 