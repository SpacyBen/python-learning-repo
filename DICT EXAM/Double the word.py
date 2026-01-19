def DOUBLE(word):
    result = ""
    dict_chars = {}
    for char in word:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
        
    for char in word:
            if dict_chars[char] != 2:
                result += char * 2
            else:
                result += char
    print(result)

word = "Kamusta"
DOUBLE(word)