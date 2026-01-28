def pal(word):
    index = len(word) - 1
    word2 = ""
    while index >= 0:
        word2 += word[index]
        index -= 1
    
    if word2 == word:
        return print("checker1: Word is Palindrome")
    else:
        return print("checker1: Word is not a Palindrome")
    
def pal2(word):
    if word == word[::-1]:
        return print("checker2: Word is Palindrome")
    else:
        return print("checker2: Word is not a Palindrome")

def pal3(word):
    word3 = list(word)
    l,r = 0, len(word) - 1
    while l < r:
        word3[l], word3[r] = word3[r], word3[l]
        l += 1
        r -= 1
    if list(word) == word3:
        return print("checker3: Word is Palindrome")
    else:
        return print("checker3: Word is not a Palindrome")


print("Palindrome checker")
word = input("Enter Word: ")
pal(word)
pal2(word)
pal3(word)
print("List Palindrome checker")
list2 = input("Enter Numbers or letters seperate with space: ")
tolist = list2.split()
print(tolist)