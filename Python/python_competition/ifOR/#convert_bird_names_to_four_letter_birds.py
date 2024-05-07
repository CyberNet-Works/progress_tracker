#convert_bird_names_to_four_letter_birds
def bird_code(name):
    namelist = name.split()
    newname = ""

    if len(namelist) == 1:
        newname = name[:5]

    elif len(namelist) == 2:
        newname = namelist[0][0:2] + namelist[1][0:2]
    
    elif len(namelist) >= 3:
        newname = namelist[0][0] + namelist[1][0] + namelist[2][0] + namelist[-1][0]

    return newname.upper()