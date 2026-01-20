def DOUBLE(word):
    result = ""
    for char in word:
        if word.count(char) == 1:
            result += char * 2   # appears once → double
        else:
            result += char       # appears more than once → single
    print(result)

word = "Kamusta"
DOUBLE(word)
