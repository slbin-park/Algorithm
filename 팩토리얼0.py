n = int(input())
res = 1
for i in range(1, n + 1):
    res = res * i
ans = str(res)
cnt = 0
if ans[len(ans) - 1] != '0':
    print(0)
else:
    for i in range(len(ans) - 1, -1, -1):
        if ans[i] == '0':
            cnt += 1
        else:
            break
    print(cnt)
