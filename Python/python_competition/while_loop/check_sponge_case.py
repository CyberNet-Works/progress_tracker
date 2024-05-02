def is_spongecase(s):
    string = s
    index = 0

    while index < len(s) - 2:
        if string[index].isupper() and string[index + 1].islower() or string[index].islower() and string[index + 1].isupper():
            spongecase = True
        else:
            spongecase = False
            break
        index += 1

    return spongecase