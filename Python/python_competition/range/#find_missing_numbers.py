#find_missing_numbers.py
def find_missing_number(numbers):
    numbers = sorted(numbers)

    number = numbers[0] - 1

    for i in range(0, len(numbers) - 1):
        if numbers[i + 1] != numbers[i] + 1:
            number = numbers[i] + 1
    
    return number