import sys
input = sys.stdin.readline
n = int(input())
res = [[0] * 10 for i in range(n+1)]
res[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    res[i][0] = res[i-1][1]
    res[i][9] = res[i-1][8]
    for j in range(1, 9):
        res[i][j] = res[i-1][j-1]+res[i-1][j+1]
print(sum(res[n]) % 1000000000)
