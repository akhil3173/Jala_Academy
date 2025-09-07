try:
    a = int(input())
    b = int(input())
    print(a // b)
    arr = [1,2,3]
    idx = int(input())
    print(arr[idx])
except ZeroDivisionError:
    print("ArithmeticException: Division by zero")
except IndexError:
    print("IndexError: List index out of range")
