
word = input("Enter a word: ")
i = 0 
alpha = 'abcdefghijklmnopqrstuvwxyz'
shifted_word = ""
for char in word:
    dex = 0 #2
    for index in range(len(alpha)):
        if alpha[index] == char:
            break
        dex += 1
    shifted_word += alpha[dex + i]
    i += 1
print(shifted_word)

    

    

        



