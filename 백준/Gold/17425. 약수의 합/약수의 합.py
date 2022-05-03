import sys

input = sys.stdin.readline
MAX = 1000000
n = int(input())
dp = [1 for i in range(MAX + 1)]
res = [0 for i in range(MAX + 1)]
for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1
for i in range(1, MAX + 1):
    res[i] += dp[i] + res[i - 1]
for i in range(n):
    a = int(input())
    print(res[a])