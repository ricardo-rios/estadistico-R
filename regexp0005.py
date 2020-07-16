import re

print("Lowercase w:", re.search(r'Co\wk\we', 'Cookie').group())

print("Uppercase W:", re.search(r'C\Wke', 'C@ke').group())

print("Uppercase W won't match, and return:", re.search(r'Co\Wk\We', 'Cookie'))


print("Lowercase s:", re.search(r'Eat\scake', 'Eat cake').group())
print("Uppercase S:", re.search(r'cook\Se', "Let's eat cookie").group())

print("How many cookies do you want? ", re.search(r'\d+', '100 cookies').group())


