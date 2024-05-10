#check_if_list_is_special
#special if even indexes are even and odd indexes are odd:
def is_special(lst):

    left = []
    right = []

    left_special = True
    right_special = True

    for index, num in enumerate(lst):
        if index % 2 == 0:
            left.append(num)
        elif index % 2 != 0:
            right.append(num)

    x = True
    for x in left:
        if x % 2 != 0:
            left_special = False

    y = True
    for y in right:
        if y % 2 == 0:
            right_special = False


    
    return left_special == right_special == True