def check_result(marks):
    if marks > 100 or marks < 0:
        return "Invalid"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"