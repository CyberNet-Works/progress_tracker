def highest_index(numbers):
    max_number = max(numbers)

    index = [i for i in range(len(numbers)) if numbers[i] == max_number]
    return index[-1]

    
    # index = []

    # for i in range(len(numbers)):
    #     if numbers[i] == max_number:
    #         index.append(i)
