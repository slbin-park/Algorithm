import sys
import heapq

input= sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    a = int(input())
    heapq.heappush(heap,a)
result = 0

while len(heap)!=1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    result += a+b
    heapq.heappush(heap,a+b)
print(result)