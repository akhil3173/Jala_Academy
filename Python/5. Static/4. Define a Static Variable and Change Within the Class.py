class D:
    w = int(input("Enter initial value for static variable w in class D: "))

D.w = int(input("Enter new value for static variable w modified by class D: "))
print(D.w)
d = D()
print(d.w)
