import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = [0]
m = int(input())
answer = 0
for i in range(n-1):
    a = int(input())
    heapq.heappush(heap,-a)
while -heap[0] >= m:
    a = -heapq.heappop(heap)
    a -=1
    heapq.heappush(heap,-a)
    m+=1
    answer+=1
print(answer)