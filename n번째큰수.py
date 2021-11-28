import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if len(heap) == n:
            a = heapq.heappop(heap)
            if a < arr[j]:
                heapq.heappush(heap, arr[j])
            else:
                heapq.heappush(heap, a)
        else:
            heapq.heappush(heap, arr[j])
print(heapq.heappop(heap))
