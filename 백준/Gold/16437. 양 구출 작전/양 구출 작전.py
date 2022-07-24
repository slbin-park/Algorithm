import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
arr = [[],[0,0]]
arr2 = [[] for i in range(n + 2)]
res = 0
for i in range(1, n):
    t, a, p = input().split()
    a = int(a)
    p = int(p)
    arr.append([t, a, p])
    arr2[p].append(i + 1)


def dfs(now):
    scount = 0
    for i in arr2[now]:
        scount += dfs(i)
    if arr[now ][0] == 'S' and now != 1:
        scount += arr[now][1]
    elif arr[now][0] == 'W':
        scount = scount - arr[now][1]
    if scount <= 0:
        scount = 0
    return scount


res = dfs(1)
print(res)
