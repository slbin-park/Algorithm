import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [[0, 0]]
knapsack = [[0 for i in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = arr[i][0]
        v = arr[i][1]
        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i - 1][j - w],
                                 knapsack[i - 1][j])
print(knapsack[n][k])
