def to_pascal_case(s):
    words = s.split()

    result = []

    for word in words:
        result += [word.capitalize()]

    result= "".join(result)

    return result