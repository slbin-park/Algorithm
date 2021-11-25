import sys

input = sys.stdin.readline
n = int(input())
arr = [0.0 for i in range(n)]
for i in range(n):
    arr[i] = float(input())
res = [0.0 for i in range(n)]
res[0] = arr[0]
res[1] = max(arr[1], arr[0] * arr[1])
for i in range(2, n):
    res[i] = max(arr[i - 1] * arr[i], arr[i], res[i - 2] * arr[i - 1] * arr[i])
print('%.3f' % (max(res)))
