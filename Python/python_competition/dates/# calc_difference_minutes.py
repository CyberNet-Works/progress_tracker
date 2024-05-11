# calc_difference_minutes

from datetime import datetime

def calculate_duration(start_time, final_time):
    start_time = datetime.strptime(start_time, '%H:%M')    
    final_time = datetime.strptime(final_time, '%H:%M')    

    difference = final_time - start_time

    duration_minutes = difference.seconds // 60

    return duration_minutes