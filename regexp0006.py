import re 

# Example for \t
print("\\t (TAB) example: ", re.search(r'Eat\tcake', 'Eat	cake').group())

# Example for \b
print("\\b match gives: ",re.search(r'\b[A-E]ookie', 'Cookie').group())
