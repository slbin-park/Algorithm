import bisect

x = int(input())
arr = []
for i in range(x):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()
dp = [1 for i in range(x)]
for i in range(1, x):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(x - max(dp))
