#WEIRD NUMBERS
def is_weird(n):
    if n % 2 == 0 and n not in range(6, 20):
        return "Not Weird"
    else:
        return "Weird"


    # if n % 2 == 0:
    #     if n not in range(6, 20):
    #         return "Not Weird"
    #     else:
    #         return 'Weird'
    # else:
    #     return "Weird"


    
# weird:
# odd
# even in range 6:20

# not weird:
# even in 2:5
# even greater than 20
