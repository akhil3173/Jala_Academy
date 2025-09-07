s = input("Enter the string: ")
sub = input("Enter substring to find: ")
index = -1
for i in range(len(s) - len(sub) + 1):
    found = True
    for j in range(len(sub)):
        if s[i+j] != sub[j]:
            found = False
            break
    if found:
        index = i
        break
print(index)
