import re 

print(re.search(r'Co+kie', 'Cooookie').group())

print(re.search(r'Ca*o*kie', 'Cookie').group()) 

print(re.search(r'Colou?r', 'Color').group()) 

print(re.search(r'\d{9,10}', '0987654321').group())
