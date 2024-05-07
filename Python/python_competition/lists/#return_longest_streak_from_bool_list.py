#return the longest streak from a list of boolean values.py
def longest_streak(habit):
    current_streak = 0
    last_streak = 0

    for index in range(len(habit)):
        if habit[index] == True:
            current_streak += 1
        if habit[index] == False:
            last_streak = current_streak
            current_streak = 0

    return max(current_streak, last_streak)