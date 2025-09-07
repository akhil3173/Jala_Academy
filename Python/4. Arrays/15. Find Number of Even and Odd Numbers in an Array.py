def count_even_odd(arr):
    even = 0
    odd = 0
    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
even, odd = count_even_odd(arr)
print(even, odd)
