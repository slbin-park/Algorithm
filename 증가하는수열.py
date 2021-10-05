import sys
import bisect

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = [0 for i in range(n)]
dp = [arr[0]]
maxindex = 0  #인덱스
maxnum = 0  #숫자
ans = []
for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        res[i] = len(dp)
        maxnum = res[i]
        maxindex = i
    else:
        idx = bisect.bisect_left(dp, arr[i])
        res[i] = idx + 1
        dp[idx] = arr[i]
ans.append(arr[maxindex])
maxindex -= 1
maxnum -= 1
while maxnum > 0:
    if maxnum == res[maxindex]:
        ans.append(arr[maxindex])
        maxnum -= 1
    maxindex -= 1
print(len(ans))
for i in range(len(ans) - 1, -1, -1):
    print(ans[i], end=' ')
