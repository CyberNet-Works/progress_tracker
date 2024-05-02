def loves_me_not(n):

    a = "Loves me"
    b = "Loves me not"

    count = 0
    results = []

    for x in range(n):
        results.append(a)
        count += 1

        if count == n:
            break

        results.append(b)
        count += 1

        if count == n:
            break

    return results