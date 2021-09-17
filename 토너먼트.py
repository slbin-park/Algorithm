k, n, m = map(int, input().split())
cnt = 0


def go_to(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n // 2
    elif n % 2 == 1:
        return n // 2 + 1


while 1:
    cnt += 1
    if n == m:
        break
    n = go_to(n)
    m = go_to(m)
print(cnt - 1)
