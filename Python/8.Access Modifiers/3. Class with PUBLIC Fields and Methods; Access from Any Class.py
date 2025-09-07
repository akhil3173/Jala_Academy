class PublicClass:
    def __init__(self):
        self.public_field = input("Enter public field value: ")

    def public_method(self):
        print("Public method called with field:", self.public_field)

class AnyOtherClass:
    def access_public(self, pc):
        print(pc.public_field)
        pc.public_method()

pc = PublicClass()
aoc = AnyOtherClass()
aoc.access_public(pc)
