def contains(arr, val):
    for x in arr:
        if x == val:
            return True
    return False

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
val = int(input())
print(contains(arr, val))
