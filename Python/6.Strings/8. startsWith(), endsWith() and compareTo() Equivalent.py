s = input("Enter string: ")
prefix = input("Enter prefix: ")
suffix = input("Enter suffix: ")
def starts_with(s, prefix):
    if len(prefix) > len(s):
        return False
    for i in range(len(prefix)):
        if s[i] != prefix[i]:
            return False
    return True
def ends_with(s, suffix):
    if len(suffix) > len(s):
        return False
    for i in range(1, len(suffix)+1):
        if s[-i] != suffix[-i]:
            return False
    return True
def compare_to(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i])
    return len(a) - len(b)
print(starts_with(s, prefix))
print(ends_with(s, suffix))
print(compare_to(s, prefix))
