s = input("Enter the string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
res = ''
i = start
while i < end:
    res += s[i]
    i += 1
print(res)
