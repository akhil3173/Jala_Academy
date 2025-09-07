filename = input("Enter filename to read up to an index: ")
index = int(input("Enter index to read up to: "))
f = open(filename, "r")
data = ''
i = 0
while i < index:
    char = f.read(1)
    if not char:
        break
    data += char
    i += 1
print(data)
f.close()
