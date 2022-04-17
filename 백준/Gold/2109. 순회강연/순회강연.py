import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
day = 0
for i in range(n):
    p, d = map(int, input().split())
    day = max(d, day)
    heapq.heappush(heap, [-p, d])
arr = [0 for i in range(day + 1)]
while heap:
    p, d = heapq.heappop(heap)
    for i in range(d, 0, -1):
        if arr[i] == 0:
            arr[i] = -p
            break
print(sum(arr))