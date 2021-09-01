import sys
sys.setrecursionlimit(10**8)

n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
dp = [0]*(max(d)+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, max(d)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in d:
    print(dp[i])
