import re


print(re.search(r'Not a\sregular character', 'Not a regular character').group())


print(re.search(r'Just a \\sregular character', 'Just a \sregular character').group())
