def harmonic_sum(n):
    series = 1

    for i in range(2, n + 1):
        series += (1 / i)

    return round(series,2)