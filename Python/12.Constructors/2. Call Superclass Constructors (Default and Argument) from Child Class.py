class SuperClass:
    def __init__(self, a=None):
        if a is None:
            print("SuperClass default constructor")
        else:
            print("SuperClass argument constructor with:", a)

class ChildClass(SuperClass):
    def __init__(self, a=None):
        if a is None:
            super().__init__()
            print("ChildClass default constructor")
        else:
            super().__init__(a)
            print("ChildClass argument constructor with:", a)

c1 = ChildClass()
c2 = ChildClass(int(input("Enter argument for ChildClass: ")))
