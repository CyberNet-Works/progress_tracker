#check if sentence starts with capital and ends with period.  If not fix.
def correct_sentence(sentence):
    if sentence[0].islower() and sentence[-1] != ".":
        return sentence[0].upper() + sentence[1:] + "."
    elif sentence[0].islower():
        return sentence[0].upper() + sentence[1:]
    else:
        return sentence