import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    a = list(map(int,input().split()))
    if a[0]==0 and len(heap):
        print(-heapq.heappop(heap))
    elif a[0]!=0:
        for j in range(1,a[0]+1):
            heapq.heappush(heap,-a[j])
    else:
        print(-1)
        