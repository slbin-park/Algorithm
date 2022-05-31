import sys

input = sys.stdin.readline
n, m = map(int, input().split())
res = [[0 for i in range(n + 2)] for i in range(n + 2)]

for i in range(1, n + 1):
    ans = list(map(int, input().split()))
    for j in range(1, n + 1):
        res[i][j] = ans[j - 1] + res[i - 1][j] + res[i][j - 1] - res[i - 1][j -
                                                                            1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    a = res[x2][y2]
    b = res[x2][y1 - 1]
    c = res[x1 - 1][y2]
    d = res[x1 - 1][y1 - 1]
    print(a - b - c + d)