def second_largest(arr):
    first = arr[0]
    for x in arr:
        if x > first:
            first = x
    second = None
    for x in arr:
        if x != first:
            if second is None or x > second:
                second = x
    return second

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(second_largest(arr))
