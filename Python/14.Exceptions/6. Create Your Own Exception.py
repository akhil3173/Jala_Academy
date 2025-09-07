class MyException(Exception):
    pass

def raise_myexception():
    raise MyException("This is my custom exception")

try:
    raise_myexception()
except MyException as e:
    print("Caught custom exception:", e)
