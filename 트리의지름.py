import sys

sys.setrecursionlimit(10**5)
iuput = sys.stdin.readline


def dfs(a, b):
    global res
    sum = 0
    rcur = b
    sarr = []
    for i in arr[a]:
        cur = dfs(i[0], i[1])
        sarr.append(cur)
        rcur = max(b + cur, rcur)  # 밑에서 올라온것 중에 가장 높은값을 저장
    for i in range(len(sarr) - 1):
        for j in range(i + 1, len(sarr)):
            sum = max(sum, sarr[i] + sarr[j])
    res = max(res, sum, rcur)
    return rcur


n = int(input())
arr = [[] for i in range(n + 1)]
res = 0
for i in range(n - 1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
dfs(1, 0)
print(res)