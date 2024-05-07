#check for repeating digit
def is_repdigit(num):
    rep = [char for char in str(num)]

    for i in range(len(rep) - 1):
        if rep[i] != rep[i + 1]:
            return False
    
    return True