filename = input("Enter filename to read line by line: ")
f = open(filename, "r")
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()
