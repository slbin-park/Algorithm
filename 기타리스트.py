import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0 for i in range(M + 1)] for i in range(N + 1)]
dp[0][S] = 1
for i in range(N):
    flag = 0
    for j in range(M + 1):
        if dp[i][j] == 1 and j + arr[i] <= M:
            dp[i + 1][j + arr[i]] = 1
            flag = 1
        if dp[i][j] == 1 and j - arr[i] >= 0:
            dp[i + 1][j - arr[i]] = 1
            flag = 1
    if flag == 0:
        print(-1)
        exit()
res = 0
for i in range(M + 1):
    if dp[N][i] == 1:
        res = max(res, i)
print(res)
