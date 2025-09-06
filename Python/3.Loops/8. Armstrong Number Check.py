n = int(input())
num = n
digits = len(str(n))
s = sum(int(d) ** digits for d in str(n))
print(s == num)
