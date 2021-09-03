import sys

input = sys.stdin.readline
n = int(input())
arr = [[0 for i in range(3)] for j in range(n)]
res = [[0 for i in range(3)] for j in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
res[0][0] = arr[0][0]
res[0][1] = arr[0][1]
res[0][2] = arr[0][2]
res[1][0] = min(arr[0][1], arr[0][2]) + arr[1][0]
res[1][1] = min(arr[0][0], arr[0][2]) + arr[1][1]
res[1][2] = min(arr[0][0], arr[0][1]) + arr[1][2]
for i in range(1, n):
    res[i][0] = min(res[i - 1][1], res[i - 1][2]) + arr[i][0]
    res[i][1] = min(res[i - 1][0], res[i - 1][2]) + arr[i][1]
    res[i][2] = min(res[i - 1][0], res[i - 1][1]) + arr[i][2]
print(min(res[n - 1]))
