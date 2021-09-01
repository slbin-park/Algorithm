import sys
from collections import deque
sys.setrecursionlimit(100000)  # 재귀 최대깊이를 정해줌


def dfs(x1, y1, x2, y2):
    dq = deque()
    dq.append([x1, y1])
    arr[x1][y1] = 1
    while dq:
        x, y = dq.popleft()
        if x == x2 and y == y2:
            return arr[x][y]-1
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if(nx >= 0 and nx < a and ny >= 0 and ny < a):
                if arr[nx][ny] == 0:
                    dq.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1


n = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for i in range(n):
    a = int(input())
    arr = [[0 for _ in range(a)] for _ in range(a)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(dfs(x1, y1, x2, y2))
