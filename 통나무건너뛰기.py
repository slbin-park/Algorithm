import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    res = 0
    a = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for j in range(2, a):
        res = max(res, arr[j] - arr[j - 2])
    print(res)