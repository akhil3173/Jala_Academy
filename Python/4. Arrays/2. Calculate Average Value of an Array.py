def array_avg(arr):
    total = 0
    for x in arr:
        total += x
    return total // len(arr)

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(array_avg(arr))
