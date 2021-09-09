import sys
import heapq
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.

heap = []
n = int(input())
for i in range(n):
    heapq.heappush(heap, int(input()))
cnt = 0
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    cnt += a + b
    heapq.heappush(heap, a + b)
print(cnt)