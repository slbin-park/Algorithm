import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    a, start, end = map(int, input().split())
    arr.append([start, end])
arr.sort()
heap = []
for start, end in arr:
    if len(heap) == 0:
        heapq.heappush(heap, end)
    else:
        if heap[0] <= start:
            heapq.heappop(heap)
            heapq.heappush(heap, end)
        else:
            heapq.heappush(heap, end)
print(len(heap))