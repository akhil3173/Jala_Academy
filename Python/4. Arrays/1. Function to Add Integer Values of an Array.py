def array_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(array_sum(arr))
