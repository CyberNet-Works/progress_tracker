#reformat dates with strptime and strftime
from datetime import datetime

def convert_date_format(date):
    unformatted = datetime.strptime(date, '%d-%m-%Y')
    formatted_date = unformatted.strftime('%m-%d-%Y')
    
    return formatted_date 
