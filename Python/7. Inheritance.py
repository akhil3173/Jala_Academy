class A:
    def __init__(self):
        self.data = int(input("Enter data for class A: "))
    def method1(self):
        print("A method1")
    def method2(self):
        print("A method2")
    def override_method(self):
        print("A override method with data:", self.data)

class B(A):
    def __init__(self):
        super().__init__()
        self.data = int(input("Enter data for class B: "))
    def method3(self):
        print("B method3")
    def method4(self):
        print("B method4")
    def override_method(self):
        print("B override method with data:", self.data)

class C(B):
    def __init__(self):
        super().__init__()
        self.data = int(input("Enter data for class C: "))
    def method5(self):
        print("C method5")
    def method6(self):
        print("C method6")
    def override_method(self):
        print("C override method with data:", self.data)

def main():
    a = A()
    a.method1()
    a.method2()
    a.override_method()

    b = B()
    b.method3()
    b.method4()
    b.override_method()

    c = C()
    c.method5()
    c.method6()
    c.override_method()

    print("Overridden method calls with superclass reference:")
    a_ref_b = b
    a_ref_c = c
    A.override_method(a_ref_b)
    A.override_method(a_ref_c)

    print("Runtime polymorphism with data members:")
    print("a.data =", a.data)
    print("b.data =", b.data)
    print("c.data =", c.data)

    a_ref_b_data = b
    a_ref_c_data = c
    print("Superclass ref to B's data:", a_ref_b_data.data)
    print("Superclass ref to C's data:", a_ref_c_data.data)

main()
