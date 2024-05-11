#calc_date_difference_in_days

from datetime import datetime, timedelta

def calculate_days(date1, date2):
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')

    difference = date2 - date1

    return difference.days
