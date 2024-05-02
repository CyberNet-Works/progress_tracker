def remove_vowels(string):
    vowels = str.maketrans("", "", "AEIOUaeiou")

    translation = string.translate(vowels)

    return translation

    
#with 3 arguments for str.maketrans 
#you have input, output, and removed
#if two arguments:
#input and output only