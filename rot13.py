n = input()
res = ''
for i in range(len(n)):
    if n[i] == ' ' or ord(n[i]) < ord('A'):
        res += n[i]
    else:
        if ord(n[i]) + 13 > 122:
            res += chr(96 + (ord(n[i]) + 13) - 122)
        elif ord(n[i]) + 13 > 90 and ord(n[i]) < 91:
            res += chr(64 + (ord(n[i]) + 13) - 90)
        else:
            res += chr(ord(n[i]) + 13)
print(res)
