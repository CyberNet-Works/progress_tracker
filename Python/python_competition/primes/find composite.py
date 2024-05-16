def is_composite(n):
    
# def is_prime(n):
    prime = True
    if n < 1:
        return False
    else:
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                prime = False

    if prime == False:
        return True
    else:
        return False