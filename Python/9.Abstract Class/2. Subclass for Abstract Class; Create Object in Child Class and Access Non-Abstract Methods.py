class ChildClass(AbstractClass):
    def abstract_method(self):
        print("Abstract method implementation")

    def use_parent_methods(self):
        self.non_abstract_method()

child = ChildClass()
child.use_parent_methods()
