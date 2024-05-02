#return_first_non_repeating_char.py
def first_nonrepeated(s):
    for i, x in enumerate(s):
        if s.count(x) == 1:
            return x
        
#return next((x for x in s if s.count(x) == 1), None)

