import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [[] for i in range(n)]
if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[1], arr[0], arr[0] + arr[1]))
elif n >= 3:
    res[0] = arr[0]
    res[1] = max(res[0] + arr[1], arr[1])
    res[2] = max(res[1] + arr[2], arr[2], arr[1] + arr[2])
    for i in range(3, n):
        res[i] = max(res[i - 1] + arr[i], arr[i], arr[i - 1] + arr[i])
    print(max(res))
