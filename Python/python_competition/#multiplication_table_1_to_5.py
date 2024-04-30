#multiplication_table_1_to_5.py

def multiplication_table(n):
    result = []
    
    for i in range(1, 6):
        result.append(i * n)

    return result