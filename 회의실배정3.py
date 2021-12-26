import sys

input = sys.stdin.readline

n = int(input())
dp = [1e9 for i in range(n + 1)]
dp[n] = 0
for i in range(n, 0, -1):
    if i % 3 == 0:
        dp[i // 3] = min(dp[i // 3], dp[i] + 1)
    if i % 2 == 0:
        dp[i // 2] = min(dp[i // 2], dp[i] + 1)
    dp[i - 1] = min(dp[i - 1], dp[i] + 1)
print(dp[1])
