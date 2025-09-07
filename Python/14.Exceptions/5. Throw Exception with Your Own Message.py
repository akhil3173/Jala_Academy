def check_value(v):
    if v < 0:
        raise Exception("Value must not be negative")

v = int(input())
try:
    check_value(v)
    print("Value is", v)
except Exception as e:
    print("Exception:", e)
