import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
day = 0
for i in range(n):
    p, d = map(int, input().split())
    heap.append([d, p])
heap.sort()
res = []
for d, p in heap:
    heapq.heappush(res, p)
    if len(res) > d:
        heapq.heappop(res)
print(sum(res))
