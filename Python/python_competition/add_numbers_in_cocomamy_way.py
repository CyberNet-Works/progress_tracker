def add_numbers(num1, num2):
    num3 = num1 + num2

    result = ""
    result += str(num1)
    result += str(num2)
    result += str(num3)
    
    if num1 == 0 and num2 == 0:
        return 0
    else:
        return result