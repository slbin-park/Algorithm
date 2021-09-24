n = int(input())
dp = [1000 for i in range(50001)]
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        dp[i] = min(dp[i], dp[i - j * j] + 1)
print(dp[n])
