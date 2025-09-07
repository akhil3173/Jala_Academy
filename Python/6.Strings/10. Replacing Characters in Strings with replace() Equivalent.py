s = input("Enter string: ")
old = input("Enter character to replace: ")
new = input("Enter replacement character: ")
res = ''
for c in s:
    if c == old:
        res += new
    else:
        res += c
print(res)
