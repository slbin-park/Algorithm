import sys

input = sys.stdin.readline
n = int(input())
arrlen = list(map(int, input().split()))
arr = list(map(int, input().split()))
res = 0
cur = arr[0]
res = arr[0] * arrlen[0]
for i in range(1, n - 1):
    if cur > arr[i]:
        cur = arr[i]
    res += cur * arrlen[i]
print(res)