import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = arr[i] + dp[i - 1]
left = 0
right = m - 1
answer = -100000000
if m == 1:
    print(max(arr))
    exit(0)
for i in range(m - 1, n):
    answer = max(dp[right] - dp[left] + arr[left], answer)
    right += 1
    left += 1
print(answer)