#weekly_salary_for_regular_rate_20_and_25_overtime.py
def calculate_salary(hours):

    total_salary = 0
    regular_rate = 20
    overtime = 25

    if hours <= 40:
        total_salary = regular_rate * hours

    if hours > 40:
        total_salary = (regular_rate * 40) + (25 * (hours - 40))
    
    return total_salary
