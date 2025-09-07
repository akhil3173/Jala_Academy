s = input("Enter string: ")
start = 0
end = len(s) - 1
while start <= end and s[start] == ' ':
    start += 1
while end >= start and s[end] == ' ':
    end -= 1
res = ''
i = start
while i <= end:
    res += s[i]
    i += 1
print(res)
