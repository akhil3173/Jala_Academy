try:
    a = int(input())
    b = int(input())
    print(a // b)
except ZeroDivisionError:
    print("ArithmeticException: Division by zero")
