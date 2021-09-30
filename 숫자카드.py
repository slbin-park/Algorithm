# def dfs(start, str):
#     global cnt
#     if start >= arrlen:
#         cnt += 1
#     elif start + 1 < arrlen:
#         if int(n[start] + n[start + 1]) < 35:
#             dfs(start + 1, str + ' ' + n[start])
#             dfs(start + 2, str + ' ' + n[start] + n[start + 1])
#         else:
#             dfs(start + 1, str + ' ' + n[start])
#     else:
#         dfs(start + 1, str + ' ' + n[start])

n = input().strip()
arrlen = len(n)
cnt = 0
res = [0 for i in range(arrlen)]
res[0] = 1

if 10 <= int(n[0] + n[1]) < 35 and n[1] != '0':
    res[1] = 2
else:
    res[1] = 1
for i in range(2, arrlen):
    if n[i] != '0':
        res[i] += res[i - 1]
        if n[i - 1] != '0' and int(n[i - 1] + n[i]) < 35:
            res[i] += res[i - 2]
    else:
        if int(n[i - 1] + n[i]) < 35:
            res[i] += res[i - 2]

# if
#     dfs(1, n[0])
#     dfs(2, n[0] + n[1])
# else:
#     dfs(1)
print(res[arrlen - 1])
