n = int(input())
cnt = 1
res = []
res.append(64)
while 1:
    if sum(res) == n:
        break
    a = res.pop()
    if a // 2 >= n:
        res.append(a // 2)
    elif a == 1:
        continue
    else:
        res.append(a // 2)
        res.append(a // 2)
print(len(res))
