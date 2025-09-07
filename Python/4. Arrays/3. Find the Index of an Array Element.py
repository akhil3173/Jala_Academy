n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
val = int(input())
idx = -1
for i in range(n):
    if arr[i] == val:
        idx = i
        break
print(idx)
