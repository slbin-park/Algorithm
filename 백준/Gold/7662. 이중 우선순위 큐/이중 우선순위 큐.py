import sys
import heapq

input= sys.stdin.readline
n = int(input())
for i in range(n):
    m = int(input())
    n_heap = []
    m_heap = []
    visited = [0 for i in range(1000001)]
    for j in range(m):
        text,number = map(str,input().split())
        number = int(number)
        if text == 'I':
            heapq.heappush(n_heap, [number,j])
            heapq.heappush(m_heap, [-number,j])
            visited[j] = 1
        elif text == 'D':
            if number == -1:
                while len(n_heap) != 0 and visited[n_heap[0][1]] == 0:
                    heapq.heappop(n_heap)
                if len(n_heap)!=0:
                    visited[n_heap[0][1]] = 0
                    heapq.heappop(n_heap)
            else:
                while len(m_heap) != 0 and visited[m_heap[0][1]] == 0:
                    heapq.heappop(m_heap)
                if len(m_heap)!=0:
                    visited[m_heap[0][1]] = 0
                    heapq.heappop(m_heap)
    while len(m_heap) and visited[m_heap[0][1]] == 0:
        heapq.heappop(m_heap)
    while len(n_heap) and visited[n_heap[0][1]] == 0:
        heapq.heappop(n_heap)
    if len(m_heap) == 0:
        print("EMPTY")
    else:
        print(-heapq.heappop(m_heap)[0],heapq.heappop(n_heap)[0])
    