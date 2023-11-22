def solution(alp, cop, problems):
    answer = 1e9
    maxAlp = 0
    maxCop = 0
    for i in range(len(problems)):
        maxAlp = max(maxAlp,problems[i][0])
        maxCop = max(maxCop,problems[i][1])
    dp = [[1e9 for i in range(maxCop+1)]for i in range(maxAlp+1)]
    dp[min(alp,maxAlp)][min(cop,maxCop)] = 0
    for i in range(min(alp,maxAlp),maxAlp+1):
        for j in range(min(cop,maxCop),maxCop+1):
            mi = min(i+1,maxAlp)
            mj = min(j+1,maxCop)
            dp[mi][j] = min(dp[mi][j],dp[i][j]+1)
            dp[i][mj] = min(dp[i][mj],dp[i][j]+1)
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i>=alp_req and j>=cop_req:
                    mi = min(maxAlp,i+alp_rwd)
                    mj = min(maxCop,j+cop_rwd)
                    dp[mi][mj] = min(dp[mi][mj],dp[i][j]+cost)
    return dp[-1][-1]