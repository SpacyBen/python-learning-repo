# Did you Find my Key?
# by CodeChum Admin

# A dictionary is initialized with key-value pairs in the code editor.

 

# Ask the user for a string input and check if that input exists as a key in the dictionary.

 

# Print "The {key} exists in the dictionary." if it exists, otherwise print "The {key} does not exist in the dictionary."
# on the next line.

# Sample Output 1

# Enter a key: name
# The name exists in the dictionary.
# Sample Output 2

# Enter a key: eye_color
# The eye_color does not exist in the dictionary.
# Sample Output 3

# Enter a key: color
# The color exists in the dictionary.

person_details = {
    "name": "Cody",
    "age": "4",
    "color": "blue",
    "nickname": "Chum"
}
key = input("Enter a key: ")
if key in person_details:
    print("The name exists in the dictionary.")
else:
    print(f"The {key} does not exist in the dictionary.")