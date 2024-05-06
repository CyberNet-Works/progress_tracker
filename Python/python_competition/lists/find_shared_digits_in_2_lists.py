def shared_digits(num1, num2):
    list1 = [int(x) for x in str(num1)]
    list2 = [int(x) for x in str(num2)]

    result_set = set(list1).intersection(set(list2))
    converted_result = [f"{item}" for item in result_set]

    return converted_result