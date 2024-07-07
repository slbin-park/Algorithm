import sys

input = sys.stdin.readline

C, N = map(int, input().split())
arr = []
dp = [[1e9 for _ in range(C + 1)] for _ in range(N + 1)]
for i in range(N):
    cost, customer = map(int, input().split())
    arr.append([cost, customer])
    dp[i + 1][min(customer, C)] = cost

for i in range(1, N + 1):
    for j in range(1, C + 1):
        cur_cost = arr[i - 1][0]
        cur_customer = arr[i - 1][1]
        index = min(C, j + cur_customer)
        # print("i, index", i, index)
        # print("N, C", N, C)
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        dp[i][index] = min(dp[i][index], dp[i][j] + cur_cost)
answer = []
for i in range(N + 1):
    # print("N = ", dp[i][C])
    # print(dp[i][N])
    answer.append(dp[i][C])
print(min(answer))
