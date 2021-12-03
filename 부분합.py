import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0 for i in range(n + 1)]
dp[1] = arr[0]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + arr[i - 1]
start = 0
end = 1
res = n
if dp[-1] < m:
    print(0)
    exit(0)
while start != n:
    if dp[end] - dp[start] >= m:
        if end - start < res:
            res = end - start
        start += 1
    else:
        if end != n:
            end += 1
        else:
            start += 1
print(res)