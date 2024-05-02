def to_from_list(n):
    if isinstance(n, list):
        return int(''.join(map(str, n)))
    elif isinstance(n, int):
        return [int(digit) for digit in str(n)]