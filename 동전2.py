import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0 for i in range(n)]
cnt = 0
for i in range(n):
    arr[i] = int(input())
arr.sort()
dp = [10001 for i in range(m + 1)]
dp[0] = 0
for i in range(n):
    for j in range(arr[i], m + 1):
        if j - arr[i] < 0:
            break
        dp[j] = min(dp[j], dp[j - arr[i]] + 1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])