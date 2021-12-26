import sys

input = sys.stdin.readline


def dfs(idx, big_jump, energy):
    global res
    if idx == n:
        res = min(res, energy)
        return
    if idx + 1 <= n:
        dfs(idx + 1, big_jump, energy + arr[idx][0])
    if idx + 2 <= n:
        dfs(idx + 2, big_jump, energy + arr[idx][1])
    if big_jump == 0 and idx + 3 <= n:
        dfs(idx + 3, 1, energy + k)


n = int(input())
res = 1e9
arr = [[] for i in range(n)]
for i in range(1, n):
    a, b = map(int, input().split())
    arr[i] = [a, b]
k = int(input())
dfs(1, 0, 0)
print(res)