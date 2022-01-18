from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    answer = -1
    visited = [[-1 for i in range(m)] for i in range(n)]
    visited[0][0] = 1
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        x, y, cnt = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and maps[nx][ny] == 1:
                    dq.append((nx, ny, cnt + 1))
                    visited[nx][ny] = cnt + 1
                    if nx == n - 1 and ny == m - 1:
                        return cnt + 1
    return answer