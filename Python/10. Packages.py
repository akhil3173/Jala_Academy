class ClassOne:
    def __init__(self):
        self.value = input("Enter value for ClassOne: ")

    def method_one(self):
        print("ClassOne method called with value:", self.value)

class ClassTwo:
    def __init__(self):
        self.value = input("Enter value for ClassTwo: ")

    def method_two(self):
        print("ClassTwo method called with value:", self.value)

# __init__.py content simulated by importing in this script (since single script)

# Importing classes (simulated as already defined above)

def main():
    obj1 = ClassOne()
    obj1.method_one()
    obj2 = ClassTwo()
    obj2.method_two()

main()
