def avg_array(arr):
    return sum(arr) / len(arr)
arr2 = list(map(int, input().split()))
print(avg_array(arr2))
