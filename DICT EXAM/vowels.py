def is_vowel(c):
    return c.lower() in 'aeiou'

word = input("Enter a word: ")
result = ''
for char in word:
    if is_vowel(char):
        result += char * 3
    else:
        result += char * 2
print(result)
    