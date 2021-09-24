n = int(input())
for i in range(n):
    a = int(input())
    b = a // 25
    a = a % 25
    c = a // 10
    a = a % 10
    d = a // 5
    a = a % 5
    e = a
    print(b, c, d, e)
