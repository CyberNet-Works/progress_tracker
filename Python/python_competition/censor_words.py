def censor_words(sentence):
    words = sentence.split()
    result = ""

    for word in words:
        if word != words[-1]:    
            if len(word) > 4:
                result += len(word) * "*" + " "
            else:
                result += word + " "
        else:
            if len(word) > 4:
                result += len(word) * "*"
            else:
                result += word

    return result            