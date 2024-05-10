#check if list of strings can be segmented

def can_segment_string(s, words = ['apple', 'pear', 'pier', 'pie']):
    
    subset = True
    for word in words:
        if word not in s:
            subset = False

    return subset
