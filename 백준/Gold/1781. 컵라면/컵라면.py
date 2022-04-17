import heapq
import queue
import sys

input = sys.stdin.readline

n = int(input())
heap = []
day = 0
for i in range(n):
    m, v = map(int, input().split())
    heap.append([m, v])
heap.sort()
res = []
for m, v in heap:
    heapq.heappush(res, v)
    if m < len(res):
        heapq.heappop(res)
print(sum(res))