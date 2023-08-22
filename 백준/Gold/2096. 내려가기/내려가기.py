import sys

# sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
max_dp = [[0, 0, 0], [0, 0, 0]]
min_dp = [[0, 0, 0], [0, 0, 0]]
for i in range(1, n + 1):
    a = max_dp[0][0]
    b = max_dp[0][1]
    c = max_dp[0][2]
    max_dp[1][0] = max(a, b) + arr[i - 1][0]
    max_dp[1][1] = max(a, b, c) + arr[i - 1][1]
    max_dp[1][2] = max(b, c) + arr[i - 1][2]
    max_dp[0] = max_dp[1]
    a = min_dp[0][0]
    b = min_dp[0][1]
    c = min_dp[0][2]
    min_dp[1][0] = min(a, b) + arr[i - 1][0]
    min_dp[1][1] = min(a, b, c) + arr[i - 1][1]
    min_dp[1][2] = min(b, c) + arr[i - 1][2]
    min_dp[0] = min_dp[1]
print(max(max_dp[0]), min(min_dp[0]))
