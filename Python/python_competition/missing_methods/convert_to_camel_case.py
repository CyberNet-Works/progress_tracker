def convert_to_camel_case(s):
    words = s.lower().split()

    for i, word in enumerate(words):
        if i != 0:
            words[i] = word[0].upper() + word[1:]

    result = "".join(words)

    return result