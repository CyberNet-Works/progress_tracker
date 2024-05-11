#check if given month/year is friday the 13th
from datetime import datetime
def is_friday_13(month, year):
    date_object = datetime(year, month, 13)
    
    return date_object.weekday() == 4