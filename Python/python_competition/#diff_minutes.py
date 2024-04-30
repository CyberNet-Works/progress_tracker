#diff_minutes.py
from datetime import datetime

def calculate_duration(start_time, final_time):
    # write your code here
    start_datetime = datetime.strptime(start_time, "%H:%M")
    final_datetime = datetime.strptime(final_time, "%H:%M")
    difftime = final_datetime - start_datetime

    return "{:.0f}".format(difftime.total_seconds() / 60)
