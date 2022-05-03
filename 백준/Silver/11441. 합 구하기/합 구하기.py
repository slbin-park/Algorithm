import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + arr[i - 1]
m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[e] - dp[s - 1])
