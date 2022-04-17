import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
heap = []
bag = []
res = 0
for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(heap, [m, v])
for i in range(k):
    bag.append(int(input()))
bag.sort()
heap2 = []
for i in range(k):
    while heap and bag[i] >= heap[0][0]:
        m, v = heapq.heappop(heap)
        heapq.heappush(heap2, -v)
    if len(heap2) > 0:
        res -= heapq.heappop(heap2)
    elif len(heap) == 0:
        break

print(res)
