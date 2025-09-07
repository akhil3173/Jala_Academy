def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                found = False
                for d in duplicates:
                    if d == arr[i]:
                        found = True
                        break
                if not found:
                    duplicates.append(arr[i])
    return duplicates

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
result = find_duplicates(arr)
for x in result:
    print(x)
