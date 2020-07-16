import re 


pattern = "cookie"
sequence = "Cake and cookie"

heading  = r'<h1>TITLE</h1>'
print(re.match(r'<.*>', heading).group())
