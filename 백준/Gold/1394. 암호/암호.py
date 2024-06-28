import sys

input = sys.stdin.readline

available_str = input().strip()
password = input().strip()

dic = {}
for i in range(len(available_str)):
    dic[available_str[i]] = i

cnt = len(available_str)

answer = 0

dp = [0 for i in range(len(password))]
dp[0] = 1
for i in range(1, len(password)):
    dp[i] = (dp[i - 1] * cnt) % 900528

for i in range(len(password)):
    index = dic[password[i]]
    # print(dp[len(password) - 2 - i])
    a = (index + 1) * (dp[len(password) - 1 - i])
    # print("a = ", a)
    # for j in range(len(password) - 1, i, -1):
    #     a = a * cnt
    answer += a
    answer %= 900528
print(answer % 900528)
