import sys
import bisect

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [0 for i in range(1000001)]
res = 0
dp = [arr[0]]
exchange = 0
ans = []
res = 0
for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        res += 1
        dp[idx] = arr[i]
print(len(dp))
print(res)
