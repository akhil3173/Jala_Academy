class C:
    z = int(input("Enter initial value for static variable z in class C: "))

c = C()
c.z = int(input("Enter new value for static variable z modified by instance c: "))
print(c.z)
print(C.z)
