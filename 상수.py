n, m = map(int, input().split())
a = str(n)
b = str(m)
resa = ''
resb = ''
resa = a[2] + a[1] + a[0]
resb = b[2] + b[1] + b[0]
print(max(int(resa), int(resb)))
