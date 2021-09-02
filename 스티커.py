import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = int(input())
    arr = [list(map(int, input().split())) for h in range(2)]
    if a > 1:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
        for i in range(2, a):
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])
    print(max(arr[0][a - 1], arr[1][a - 1]))
