import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
arr = [[], []]
arr2 = [[] for i in range(n + 2)]
res = 0
for i in range(1, n):
    t, a, p = input().split()
    a = int(a)
    p = int(p)
    arr.append([t, a, p])
    arr2[p].append(i + 1)


def dfs(now):
    scount = 0 if arr[now][0] == 'W' else arr[now][1]
    if len(arr2[now]) == 0:
        if arr[now][0] == 'S':
            return arr[now][1]
        else:
            return 0
    for i in arr2[now]:
        scount += dfs(i)
    if arr[now][0] == 'W':
        if arr[now][1] > scount:
            scount = 0
            arr[now][1] = arr[now][1] - scount
        else:
            scount = scount - arr[now][1]
            arr[now][1] = 0
    return scount


res = dfs(1)
print(res)
