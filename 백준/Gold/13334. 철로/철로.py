import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []
answer = 0
road = []
for i in range(n):
    a = list(map(int, input().split()))
    a.sort()
    arr.append([a[0], a[1]])
l = int(input())
for i in range(n):
    if arr[i][1] - arr[i][0] <= l:
        road.append(arr[i])
road.sort(key=lambda x: x[1])
heap = []
for item in road:
    if len(heap) == 0:
        heapq.heappush(heap, item)
    else:
        while heap[0][0] < item[1] - l:
            heapq.heappop(heap)
            if len(heap):
                break
        heapq.heappush(heap, item)
    answer = max(answer, len(heap))
print(answer)