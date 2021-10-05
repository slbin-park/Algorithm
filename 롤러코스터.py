import sys
import bisect

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dpup = [1 for i in range(n)]
dpdown = [1 for i in range(n)]
dp = [arr[0]]
res = 1
for i in range(n):
    cur = 0
    dp = [arr[i]]
    for j in range(i, -1, -1):
        if arr[j] > dp[-1]:
            dp.append(arr[j])
        else:
            idx = bisect.bisect_left(dp, arr[j])
            dp[idx] = arr[j]
    cur += len(dp)
    dp = [arr[i]]
    for k in range(i, n):
        if arr[k] > dp[-1]:
            dp.append(arr[k])
        else:
            idx = bisect.bisect_left(dp, arr[k])
            dp[idx] = arr[k]
    cur += len(dp)
    res = max(res, cur - 1)
print(res)
