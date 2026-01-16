# Word Frequency Counter
# by CodeChum Admin

# Write a program that takes a sentence as input and uses a dictionary to count the frequency 
# of each word in the sentence. The words after the frequency count should be printed in lowercase.
# Sample Output 1
# Enter a sentence: This is a sample string
# Word frequency:
# this: 1
# is: 1
# a: 1
# sample: 1
# string: 1

# Sample Output 2
# Enter a sentence: CodeChum is awesome.
# Word frequency:
# codechum: 1
# is: 1
# awesome.: 1

# Sample Output 3
# Enter a sentence: Hello, World!
# Word frequency:
# hello,: 1
# world!: 1

word = input("Enter a sentence: ")
word_list = word.lower().split()
word_freq = {}
for w in word_list:
    if w in word_freq:
        word_freq[w] += 1
    else:
        word_freq[w] = 1
print(word_freq)
print("Word frequency:")
for w, freq in word_freq.items():
    print(f"{w}: {freq}")
    
