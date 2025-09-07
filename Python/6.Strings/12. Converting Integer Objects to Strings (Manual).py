n = int(input("Enter integer: "))
res = ''
if n == 0:
    res = '0'
else:
    negative = False
    if n < 0:
        negative = True
        n = -n
    digits = []
    while n > 0:
        digits.append(chr((n % 10) + 48))
        n //= 10
    if negative:
        res = '-'
    for i in range(len(digits)-1, -1, -1):
        res += digits[i]
print(res)
