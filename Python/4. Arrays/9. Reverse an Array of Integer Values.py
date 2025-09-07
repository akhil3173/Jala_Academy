def reverse_arr(arr):
    res = []
    for i in range(len(arr)-1, -1, -1):
        res.append(arr[i])
    return res

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = reverse_arr(arr)
for x in arr:
    print(x)
