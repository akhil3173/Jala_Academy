filename = input()
f = open(filename, "r")
while True:
    data = f.read(1024)
    if not data:
        break
f.close()
