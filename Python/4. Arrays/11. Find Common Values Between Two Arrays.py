n = int(input())
arr1 = []
for _ in range(n):
    arr1.append(int(input()))
m = int(input())
arr2 = []
for _ in range(m):
    arr2.append(int(input()))
common = []
for x in arr1:
    for y in arr2:
        if x == y:
            found = False
            for c in common:
                if c == x:
                    found = True
                    break
            if not found:
                common.append(x)
for x in common:
    print(x)
