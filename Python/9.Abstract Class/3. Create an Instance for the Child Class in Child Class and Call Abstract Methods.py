class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Abstract method implementation")

    def call_abstract(self):
        child = ChildClass()
        child.abstract_method()

child = ChildClass()
child.call_abstract()
