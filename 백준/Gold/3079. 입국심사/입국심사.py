import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(int(input()) for _ in range(n)))
left = 0
right = min(arr) * m
res = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(n):
        cnt += mid // arr[i]
    if cnt >= m:
        right = mid - 1
    else:
        left = mid + 1
        res = left
print(res)