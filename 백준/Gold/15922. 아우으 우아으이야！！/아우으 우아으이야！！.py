import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
res = 0
start = arr[0][0]
end = arr[0][1]
for i in range(1, n):
    if end <= arr[i][0]:
        res += abs(end - start)
        start = arr[i][0]
        end = arr[i][1]
    elif end > arr[i][0]:
        if end < arr[i][1]:
            end = arr[i][1]
res += abs(end - start)
print(res)