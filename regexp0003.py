import re 

print(re.search(r'Number: [^5]', 'Number: 0').group())
