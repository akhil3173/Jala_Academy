class AccessConstructor:
    def __init__(self):
        print("Public constructor")

    def _protected_constructor(self):
        print("Protected constructor (convention)")

    def __private_constructor(self):
        print("Private constructor (name mangled)")

    def default_constructor(self):
        print("Default constructor (same as public in Python)")

obj = AccessConstructor()
obj.__init__()
obj._protected_constructor()
try:
    obj.__private_constructor()
except AttributeError:
    print("Cannot access private constructor directly")
obj.default_constructor()
