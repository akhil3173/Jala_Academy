class MyClass:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default constructor called")
        elif b is None:
            print("One argument constructor called with:", a)
        else:
            print("Two argument constructor called with:", a, b)

def main():
    obj1 = MyClass()
    obj2 = MyClass(int(input("Enter one argument: ")))
    obj3 = MyClass(int(input("Enter first argument: ")), int(input("Enter second argument: ")))

main()
