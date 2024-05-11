#Calc duration of days between two dates
from datetime import datetime
def days_spent_together(date1, date2):
    
    formatted_date1 = datetime.strptime(date1, '%Y-%m-%d')
    formatted_date2 = datetime.strptime(date2, '%Y-%m-%d')

    duration = formatted_date2 - formatted_date1

    return duration.days