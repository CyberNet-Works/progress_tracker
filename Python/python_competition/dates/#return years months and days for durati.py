#return years months and days for duration diff
from datetime import datetime as d


def date_difference(date1,date2):

    formatted_date1 = d.strptime(date1, '%Y-%m-%d')
    formatted_date2 = d.strptime(date2, '%Y-%m-%d')

    duration = formatted_date1 - formatted_date2

    years = duration.days // 365
    months = (duration.days % 365) // 30
    days = (duration.days % 365) % 30

    return f'{years} years, {months} months, {days} days'
