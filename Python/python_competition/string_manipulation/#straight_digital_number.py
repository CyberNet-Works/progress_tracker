#straight_digital_number
def is_straight_digital(n):
    n = list([int(char) for char in str(n)])

    straight = True

    for i in range(len(n) - 2):
        if abs(n[i] - n[i + 1]) != abs(n[i + 1] - n[i + 2]):
            straight = False
    
    return straight
