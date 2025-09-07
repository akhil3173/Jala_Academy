def insert_at(arr, val, pos):
    res = []
    for i in range(pos):
        res.append(arr[i])
    res.append(val)
    for i in range(pos, len(arr)):
        res.append(arr[i])
    return res

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
val = int(input())
pos = int(input())
arr = insert_at(arr, val, pos)
for x in arr:
    print(x)
