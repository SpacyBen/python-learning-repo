import time
def correctcounter(word,text):
    word_correct = word.split()
    text_correct = text.split()
    correctword = 0
    for a,b in zip(word_correct,text_correct):
        if a == b:
            correctword += 1
    return correctword
def wpmcounter(start_t,end_t,count):
    finish = ((end_t-start_t)/60)
    wpm = round(count/finish,2)
    seconds = round(finish * 60,2)
    return wpm, seconds
def  incorrects(text,word):
    incorrect  = ""
    mistakes = 0
    for i in range(len(text)):
        if i < len(word) and i < len(text) and word[i] == text[i]:
            incorrect += word[i]
        else:
            mistakes += 1
            if text[i] != ' ':
                incorrect += "_"
            else:
                incorrect += "-"
    return mistakes, incorrect

text = "ambogi ko, ako to si ben. programmer na, pro-gamer pa"
input("Press Enter to start.")
start_time = time.time()
word = input("Type here: ")
end_time = time.time()
count =  correctcounter(word,text)
print("Correct  word: ",count)
wpm, seconds = wpmcounter(start_time,end_time,count)
mistakes, incorrect = incorrects(text,word)

print(f"Underscore ( _ and - ) Mistake: {incorrect}")
print(f"You typing speed is: {wpm} Word per minute. You finished typing: {seconds}s")
print(f"Number of Mistakes: {mistakes}")
