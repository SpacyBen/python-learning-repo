# Special Characters
# by CodeChum Admin

# Write a program that takes a character, character, as input and checks if it is a special character. 
# If the character is neither an alphabet letter nor a digit, it prints "Character is a special character." Otherwise, it does nothing.
# Sample Output 1
# Enter character: !
# Character is a special character.

# Sample Output 2
# Enter character: a

# Sample Output 3
# Enter character: /
# Character is a special character.

character = input("Enter character: ")
if not character.isalpha() and not character.isdigit():
    print("Character is a special character.")