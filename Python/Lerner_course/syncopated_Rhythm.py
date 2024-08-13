#Syncopated Rhythm:

def is_syncopated(rhythm):
    sync = True
    for i in range(0, len(rhythm) - 1):
        if rhythm[i] != rhythm[i + 1]:
            sync = False
    return "No" if sync == True else "Yes"