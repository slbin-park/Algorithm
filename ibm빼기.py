n = int(input())
for i in range(n):
    a = input()
    res = ''
    for j in a:
        if j == 'Z':
            res += 'A'
        else:
            res += chr(ord(j) + 1)
    print('String #', end='')
    print(i + 1)
    print(res)
    print()
