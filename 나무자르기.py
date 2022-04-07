import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
left = 0
right = 2000000001
res = 0
while left <= right:
    mid = (left + right) // 2
    sum = 0
    for meter in arr:
        if mid >= meter:
            break
        else:
            sum += meter - mid
    if sum >= m:
        left = mid + 1
        res = mid
    else:
        right = mid - 1

print(res)
