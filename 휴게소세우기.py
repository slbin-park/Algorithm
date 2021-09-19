import sys

input = sys.stdin.readline
n, m, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
arr.sort()
arr.append(l)
start, end = 0, arr[n]
res = l
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, len(arr)):
        # print(mid)
        cnt += (arr[i] - arr[i - 1] - 1) // mid
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        res = min(res, mid)
print(res)
