import sys

input = sys.stdin.readline
a = input()
plus = 0
minus = 0
strnumber = ''
ch = 0
for i in range(len(a) + 1):
    if i == len(a) - 1:
        if ch == 0:
            plus += int(strnumber)
            break
        else:
            minus += int(strnumber)
            break
    if a[i] == '+':
        if ch == 0:
            plus += int(strnumber)
            strnumber = ''
        else:
            minus += int(strnumber)
            strnumber = ''
    elif a[i] == '-':
        if ch == 0:
            ch = 1
            plus += int(strnumber)
            strnumber = ''
        else:
            minus += int(strnumber)
            strnumber = ''
    elif a[i] != '+' and a[i] != '-':
        strnumber += a[i]
print(plus - minus)
