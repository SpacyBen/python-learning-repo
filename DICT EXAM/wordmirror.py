def odd(num):
    return num % 2 != 0

word = input("Enter a word: ")
mirror = word

if odd(len(word)):
    for i in range(len(word)-2, -1, -1):
        mirror += word[i]
else:
    mirror += word[::-1]
print(mirror)