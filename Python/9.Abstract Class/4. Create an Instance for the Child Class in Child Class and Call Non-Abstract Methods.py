class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Abstract method implementation")

    def call_non_abstract(self):
        child = ChildClass()
        child.non_abstract_method()

child = ChildClass()
child.call_non_abstract()
