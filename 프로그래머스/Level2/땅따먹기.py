def solution(land):
    dp = [[0, 0, 0, 0] for i in range(len(land))]
    dp[0][0] = land[0][0]
    dp[0][1] = land[0][1]
    dp[0][2] = land[0][2]
    dp[0][3] = land[0][3]

    for i in range(1, len(land)):
        dp[i][0] = land[i][0] + max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3])
        dp[i][1] = land[i][1] + max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3])
        dp[i][2] = land[i][2] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3])
        dp[i][3] = land[i][3] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])

    answer = max(dp[len(land) - 1])
    return answer