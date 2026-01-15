import re

input = "Hello, World!"
pattern = r"hello"
	
is_match = re.search(pattern, input, re.IGNORECASE)
	
print(is_match)