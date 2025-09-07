try:
    a = int(input())
    b = int(input())
    print(a // b)
except ZeroDivisionError:
    print("Division by zero error")
finally:
    print("Finally block executed")
