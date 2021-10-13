import bisect

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]
ans = 0
for i in range(n):
    dp = [arr[0]]
    for j in range(0, i + 1):
        if arr[j] > dp[-1]:
            dp.append(arr[j])
        else:
            idx = bisect.bisect_left(dp, arr[j])
            dp[idx] = arr[j]
    res = len(dp)
    dp = [arr[-1]]
    for j in range(n - 1, i - 1, -1):
        if arr[j] > dp[-1]:
            dp.append(arr[j])
        else:
            idx = bisect.bisect_left(dp, arr[j])
            dp[idx] = arr[j]
    res += len(dp)
    ans = max(ans, res - 1)
print(ans)
