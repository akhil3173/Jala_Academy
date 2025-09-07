class AttributesConstructor:
    def __init__(self):
        self.attr1 = input("Enter attribute 1: ")
        self.attr2 = int(input("Enter attribute 2: "))

    def show_attributes(self):
        print("Attribute 1:", self.attr1)
        print("Attribute 2:", self.attr2)

obj = AttributesConstructor()
obj.show_attributes()
