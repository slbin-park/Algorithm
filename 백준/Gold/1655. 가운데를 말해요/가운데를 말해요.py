from copy import deepcopy
import heapq
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline

n = int(input())
l_heap = []
r_heap = []
for i in range(n):
    m = int(input())
    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap,-m)
    else:
        heapq.heappush(r_heap,m)
    if r_heap and -l_heap[0] > r_heap[0]:
        l = -heapq.heappop(l_heap)
        r = heapq.heappop(r_heap)
        heapq.heappush(r_heap,l)
        heapq.heappush(l_heap,-r)
    print(-l_heap[0])