class ProtectedClass:
    def __init__(self):
        self._protected_field = input("Enter protected field value: ")

    def _protected_method(self):
        print("Protected method called with field:", self._protected_field)

class SamePackageClass:
    def access(self, pc):
        print(pc._protected_field)
        pc._protected_method()

class SubClassDifferentPackage(ProtectedClass):
    def access_protected(self):
        print(self._protected_field)
        self._protected_method()

class DifferentPackageClass:
    def access(self, pc):
        try:
            print(pc._protected_field)
            pc._protected_method()
        except AttributeError:
            print("Cannot access protected members")

pc = ProtectedClass()
spc = SamePackageClass()
spc.access(pc)

sub_dp = SubClassDifferentPackage()
sub_dp.access_protected()

dpc = DifferentPackageClass()
dpc.access(pc)
