class MyClass:
    def method(self, a, b):
        print("Method called with two parameters:", a, b)

    def method_same(self, a, b):
        print("Second method with same parameters:", a, b)

obj = MyClass()
obj.method(int(input("Enter first parameter: ")), int(input("Enter second parameter: ")))
obj.method_same(int(input("Enter first parameter: ")), int(input("Enter second parameter: ")))
