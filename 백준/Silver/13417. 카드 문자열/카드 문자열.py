import sys
import heapq
input = sys.stdin.readline
n = int(input())
for i in range(n):
    m = int(input())
    arr = list(map(str,input().split()))
    res = arr[0]
    for j in range(1,m):
        if res[0] >= arr[j]:
            res = arr[j]+res
        else:
            res += arr[j]
    print(res)