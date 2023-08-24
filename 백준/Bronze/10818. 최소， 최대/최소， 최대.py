import sys

input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

N = int(input())
arr = list(map(int, input().split()))
res1 = 1e9
res2 = -1e9
for i in range(N):
    res1 = min(res1, arr[i])
    res2 = max(res2, arr[i])
print(res1, res2)
