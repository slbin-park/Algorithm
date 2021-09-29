import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    a = int(input())
    if a == 0 and len(heap) == 0:
        print(0)
    elif a == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, a)
