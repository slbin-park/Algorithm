import heapq
import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = int(input())
    heap = []
    max_heap = []
    visited = [0 for i in range(1000001)]
    visited[i] = 1
    cur = 0
    for j in range(a):
        str1, value = input().split()
        if str1 == 'I':
            heapq.heappush(heap, [int(value), j])
            heapq.heappush(max_heap, [-int(value), j])
            visited[j] = 1
        else:
            if value[0] == '1':  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if len(max_heap) > 0:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
            else:
                while heap and visited[heap[0][1]] == 0:
                    heapq.heappop(heap)
                if len(heap) > 0:
                    visited[heap[0][1]] = 0
                    heapq.heappop(heap)
    while heap and visited[heap[0][1]] == 0:
        heapq.heappop(heap)
    while max_heap and visited[max_heap[0][1]] == 0:
        heapq.heappop(max_heap)
    if len(heap) > 0:
        print(-max_heap[0][0], heap[0][0])
    else:
        print('EMPTY')
