import os
filename = input("Enter filename to check permissions: ")
read_access = os.access(filename, os.R_OK)
write_access = os.access(filename, os.W_OK)
print("Read access:", read_access)
print("Write access:", write_access)
