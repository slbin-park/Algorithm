import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [[0] * n for _ in range(2)]
maxres = arr[0]
if n == 1:
    print(arr[0])
else:
    res[0][0] = arr[0]
    for i in range(1, n):
        res[0][i] = max(res[0][i - 1] + arr[i], arr[i])
        res[1][i] = max(res[1][i - 1] + arr[i], res[0][i - 1])
        maxres = max(maxres, res[0][i], res[1][i])
    print(maxres)
