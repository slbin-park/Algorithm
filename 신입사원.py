import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    res = 1
    m = int(input())
    arr = [[0, 0] for i in range(m)]
    for j in range(m):
        arr[j] = list(map(int, input().split()))
    arr.sort(key=lambda x: x[0])
    prev = arr[0][1]
    for j in range(1, m):
        if arr[j][1] < prev:
            prev = arr[j][1]
            res += 1
    print(res)
