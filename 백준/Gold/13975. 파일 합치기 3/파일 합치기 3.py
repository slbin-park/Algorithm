import heapq
import sys

input = sys.stdin.readline


def que(arr):
    res = 0
    heap = []
    for item in arr:
        heapq.heappush(heap, item)
    while len(heap) != 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        res += a + b
        heapq.heappush(heap, a + b)
    return res


n = int(input())
for i in range(n):
    a = int(input())
    arr = list(map(int, input().split()))
    cur = que(arr)
    print(cur)