import heapq
import sys

input = sys.stdin.readline


def que(arr):
    if len(arr) == 1:
        return 1
    heap = []
    res = 1
    for i in arr:
        heapq.heappush(heap, i)
    while len(heap) != 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        res = (res * ((a % 1000000007) * (b % 1000000007))) % 1000000007
        heapq.heappush(heap, a * b)
    return res


n = int(input())
for i in range(n):
    a = int(input())
    arr = list(map(int, input().split()))
    print(que(arr))