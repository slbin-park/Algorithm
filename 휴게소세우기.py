import sys

input = sys.stdin.readline
n, m, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
arr.append(l)
arr.sort()
start, end = 1, arr[-1]
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    if mid == 0:
        break
    for i in range(1, len(arr)):
        cnt += (arr[i] - arr[i - 1] - 1) // mid
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        res = mid
print(res)
