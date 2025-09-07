class MyClass:
    def method(self, *args):
        if len(args) == 1:
            print("One parameter method called with:", args[0])
        elif len(args) == 2:
            print("Two parameter method called with:", args[0], args[1])

obj = MyClass()
obj.method(int(input("Enter one parameter: ")))
obj.method(int(input("Enter first parameter: ")), int(input("Enter second parameter: ")))
