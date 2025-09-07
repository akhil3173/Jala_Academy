def remove_duplicates(arr):
    res = []
    for x in arr:
        found = False
        for y in res:
            if y == x:
                found = True
                break
        if not found:
            res.append(x)
    return res

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = remove_duplicates(arr)
for x in arr:
    print(x)
