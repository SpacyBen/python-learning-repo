def alphabet_shifter(word):
    shifted_word = ""
    i = 0
    for char in word:
        base = ord('a') if char.islower() else ord('A')
        shifted_char = chr((ord(char) - base + i) % 26 + base)
        shifted_word += shifted_char
        i += 1
    return shifted_word
word = input("Enter a word: ")
print("Shifted word:", alphabet_shifter(word))