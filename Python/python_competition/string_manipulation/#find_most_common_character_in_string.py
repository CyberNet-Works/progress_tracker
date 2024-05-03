#find_most_common_character_in_string
def most_common_character(s):
    string = [char for char in s if char.lower() in "abcdefghijklmnopqrstuvwxyz"]
    data = {}

    for key, value in enumerate(string):
        data[value] = string.count(value)
            
    for key, value in data.items():
        if value == max(data.values()):
            return key