import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
left = 0
right = n - 1
n -= 2
res = 0
while left <= right:
    res = max(res, n * min(arr[left], arr[right]))
    if arr[left] < arr[right]:
        left += 1
    else:
        right -= 1
    n -= 1
print(res)
