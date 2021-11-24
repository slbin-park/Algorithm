import sys
import heapq

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = 1e9
cur = 1


def dijkstra():
    hq = []
    global cur
    heapq.heappush(hq, (arr[0][0], 0, 0))
    visited[0][0] = 0
    while hq:
        cost, x, y = heapq.heappop(hq)
        if x == n - 1 and y == n - 1:
            print('Problem', cur, end='')
            print(':', cost)
            cur += 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                ncost = cost + arr[nx][ny]
                if ncost < visited[nx][ny]:
                    visited[nx][ny] = ncost
                    heapq.heappush(hq, (ncost, nx, ny))


while True:
    n = int(input())
    if n == 0:
        break
    arr = [[0 for i in range(n)] for i in range(n)]
    visited = [[INF for i in range(n)] for i in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
    dijkstra()
