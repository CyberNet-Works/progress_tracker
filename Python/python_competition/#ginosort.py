def ginortS(s):
    string = [char for char in str(s)]
    lower = []
    upper = []
    odddigits = []
    evendigits = []

    for x in string:
        if x.isnumeric() and int(x) % 2 != 0:
            odddigits.append(x)
        elif x.isnumeric() and int(x) % 2 == 0:
            evendigits.append(x)
        elif x.islower():
            lower.append(x)
        elif x.isupper():
            upper.append(x)
            
    result = sorted(lower) + sorted(upper) + sorted(odddigits) + sorted(evendigits)

    final = ""
    for y in result:
        final += y

    return final
