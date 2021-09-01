
n = int(input())
dp = [0] * (n+1) #전에 했던 값을 저장하기 위해서 선언
for i in range(2, n+1): 
    dp[i] = dp[i-1] + 1 #2,3으로 나눠지지 않으면 무조건 1 을 빼기때문에 
    if i%2 ==0:
        dp[i] = min(dp[i],dp[i//2]+1) # 2로 나눠지고 
    if i%3 ==0:
        dp[i] = min(dp[i],dp[i//3] + 1)
print(dp[n])