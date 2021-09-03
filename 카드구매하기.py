import sys

input = sys.stdin.readline
n = int(input())
arr = [0]
arr += list(map(int, input().split()))
res = [0 for _ in range(n + 1)]
res[1] = arr[1]
if n > 1:
    res[2] = max(res[1] + arr[1], arr[2])

    for i in range(3, n + 1):
        res[i] = arr[i]
        for j in range(i):
            res[i] = max(res[i], res[j] + res[i - j])
print(res[n])