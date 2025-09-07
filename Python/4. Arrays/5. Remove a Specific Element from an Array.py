def remove_element(arr, val):
    res = []
    for x in arr:
        if x != val:
            res.append(x)
    return res

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
val = int(input())
arr = remove_element(arr, val)
for x in arr:
    print(x)
