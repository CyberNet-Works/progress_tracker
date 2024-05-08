#extract_numbers

def extract_numbers(s):

    result = ''.join([char for char in list(s) if char in '1234567890'])

    if not result:
        return None
    else:
        return result