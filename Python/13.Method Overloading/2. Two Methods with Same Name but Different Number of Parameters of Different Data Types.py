class MyClass:
    def method(self, *args):
        if len(args) == 1 and type(args[0]) == int:
            print("One int parameter method called with:", args[0])
        elif len(args) == 2 and type(args[0]) == int and type(args[1]) == str:
            print("Two parameters (int, str) method called with:", args[0], args[1])

obj = MyClass()
obj.method(int(input("Enter an int parameter: ")))
obj.method(int(input("Enter int parameter: ")), input("Enter string parameter: "))
