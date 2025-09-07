class PrivateClass:
    def __init__(self):
        self.__private_field = input("Enter private field value: ")

    def __private_method(self):
        print("Private method called with field:", self.__private_field)

    def main(self):
        print("Private field:", self.__private_field)
        self.__private_method()

class SubPrivateClass(PrivateClass):
    def access_private(self):
        try:
            print(self.__private_field)
        except AttributeError:
            print("Cannot access private field")
        try:
            self.__private_method()
        except AttributeError:
            print("Cannot access private method")

obj = PrivateClass()
obj.main()
sub_obj = SubPrivateClass()
sub_obj.access_private()
