n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
mn = arr[0]
mx = arr[0]
for x in arr:
    if x < mn:
        mn = x
    if x > mx:
        mx = x
print(mx - mn)
