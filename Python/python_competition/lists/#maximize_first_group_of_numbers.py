#maximize_first_group_of_numbers.py
def maximize_first_number(numbers):
    left =  sorted([int(char) for char in str(numbers[0])], reverse = True)
    right = ([int(char) for char in str(numbers[1])])
    
    lresult = ""
    rresult = ""

    for x in left:
        lresult += str(x)

    for x in right:
        rresult += str(x)

    return [int(lresult), int(rresult)]