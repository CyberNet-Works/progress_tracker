#move all zeros to the end

def move_zeroes_to_end(n):
    n = [char for char in str(n)]
    result = ""

    count = 0
    for x in n:
        if x == '0':
            count += 1

    for x in n:
        if x == '0':
            continue
        else:
            result += (x)

    result = result + (count * '0')

    return result