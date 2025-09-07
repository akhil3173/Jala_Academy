s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
res = 0
for i in range(min(len(s1), len(s2))):
    if s1[i] != s2[i]:
        res = ord(s1[i]) - ord(s2[i])
        break
else:
    res = len(s1) - len(s2)
print(res)
