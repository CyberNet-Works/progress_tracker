def calculate_era(earned_runs, innings_pitched):
    ERA = earned_runs * 9 / innings_pitched

    return  round(ERA, 2)