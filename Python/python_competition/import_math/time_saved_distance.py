def time_saved(distance, speed1, speed2):
	time1 = distance / speed1
	time2 = distance / speed2

	return round((time1 - time2), 2)