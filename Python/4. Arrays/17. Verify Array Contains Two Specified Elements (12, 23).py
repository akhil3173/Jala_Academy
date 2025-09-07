n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
found12 = False
found23 = False
for x in arr:
    if x == 12:
        found12 = True
    if x == 23:
        found23 = True
print(found12 and found23)
