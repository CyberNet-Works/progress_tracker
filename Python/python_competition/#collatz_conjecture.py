#collatz_conjecture.py
def collatz_conjecture2(n):
 
    if n <= 1:
        return [n]
    
    result = []
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
            result += [n]
        else:
            result += [(n * 3) + 1]

    return result


def collatz_conjecture(n):
    if n <= 1:
        return [n]

    result = [n]
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
        result.append(n)

    return result
