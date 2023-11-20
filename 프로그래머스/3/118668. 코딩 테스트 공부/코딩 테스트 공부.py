def solution(alp, cop, problems):
    answer = 1e9
    # 목표치
    maxAlp = 0
    maxCop = 0
    problems.append([0,0,0,1,1])
    problems.append([0,0,1,0,1])
    for i in range(len(problems)):
        maxAlp = max(maxAlp,problems[i][0])
        maxCop = max(maxCop,problems[i][1])
    dp = [[1e9 for i in range(maxCop+1)]for i in range(maxAlp+1)]
    alp = min(alp,maxAlp)
    cop = min(cop,maxCop)
    dp[alp][cop] = 0
    for i in range(alp,maxAlp+1):
        # j = 코딩력
        for j in range(cop,maxCop+1):
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i >= alp_req and j >= cop_req:
                    mAlp = min(maxAlp,i+alp_rwd)
                    mCop = min(maxCop,j+cop_rwd)
                    dp[mAlp][mCop] = min(dp[i][j] + cost, dp[mAlp][mCop])
    return dp[-1][-1]