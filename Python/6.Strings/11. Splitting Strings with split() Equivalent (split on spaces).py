s = input("Enter string: ")
words = []
word = ''
for c in s:
    if c == ' ':
        if word != '':
            words.append(word)
            word = ''
    else:
        word += c
if word != '':
    words.append(word)
for w in words:
    print(w)
