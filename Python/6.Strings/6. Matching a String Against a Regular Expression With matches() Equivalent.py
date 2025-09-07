import re
s = input("Enter the string: ")
pattern = input("Enter regex pattern: ")
matched = False
for _ in re.finditer(pattern, s):
    matched = True
print(matched)
