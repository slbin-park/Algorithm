import sys

INF = 1e9
n = int(input())
arr = [[] for i in range(n)]
dp = [[0, 0, 0] for i in range(n)]
for i in range(n):
    inp = list(map(int, input().split()))
    arr[i] = inp
res = INF
for i in range(3):
    for j in range(3):
        if i == j:
            dp[0][i] = arr[0][i]
        else:
            dp[0][j] = INF
    for j in range(1, n):
        dp[j][0] = arr[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = arr[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = arr[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for j in range(3):
        if j == i:
            continue
        else:
            res = min(res, dp[n - 1][j])
print(res)