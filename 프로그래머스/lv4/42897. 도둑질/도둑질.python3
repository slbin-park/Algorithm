def solution(money):
    answer =0
    if len(money)==3:
        return max(money[0]+money[2],money[1])
    dp = [0 for i in range(len(money))]
    dp[0] = money[0]
    for i in range(1,len(money)-1):
        dp[i]=max(dp[i-2]+money[i],dp[i-1])
    answer = dp[-2]
    dp = [0 for i in range(len(money))]
    dp[0] = 0
    for i in range(1,len(money)):
        dp[i]=max(dp[i-2]+money[i],dp[i-1])
    answer = max(answer,dp[-1])
    return answer