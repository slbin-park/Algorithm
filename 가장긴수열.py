import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]
닝
for i in range(x):
    if arr[i] > dp[-1]:
        # 오른쪽에서 왼쪽방향 -1
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
print(len(dp))
