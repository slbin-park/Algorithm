import bisect
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = [arr[0]]
for i in range(n):
    if res[-1] < arr[i]:
        res.append(arr[i])
    else:
        idx = bisect.bisect_left(res, arr[i])
        res[idx] = arr[i]
print(len(res))
