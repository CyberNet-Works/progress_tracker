def to_spongecase(text):
    result = ""
    letter_count = 0

    for i, char in enumerate(text):
        if char != " ":
            if letter_count % 2 == 0:
                result += char.lower()
            else:
                result += char.upper()
            letter_count += 1
        else:
            result += " "

    return result