#count leap years between dates:
from datetime import datetime as d

def count_leap_years(start_year, end_year): 
    leap_count = 0

    for year in range(start_year, end_year + 1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap_count += 1 

    return leap_count