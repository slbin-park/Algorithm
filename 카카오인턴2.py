from collections import deque


def solution():
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = [1 for _ in range(5)]
    for i in range(5):
        visited = [[0 for _ in range(5)] for _ in range(5)]
        dq = deque()
        for j in range(5):  #x축
            for h in range(5):  #y축
                if places[i][j][h] == 'P' and visited[j][h] == 0:
                    dq.append((j, h, 0))
                    while dq and res[i] == 1:
                        x, y, cnt = dq.popleft()
                        visited[x][y] = 1
                        if cnt < 2:
                            for k in range(4):
                                nx = x + dx[k]
                                ny = y + dy[k]
                                if 0 <= nx < 5 and 0 <= ny < 5:
                                    if places[i][nx][ny] == 'O' and visited[
                                            nx][ny] == 0:
                                        dq.append((nx, ny, cnt + 1))
                                        visited[nx][ny] = 1
                                    elif places[i][nx][ny] == 'P' and visited[
                                            nx][ny] == 0:
                                        res[i] = 0
    answer = []
    return answer


solution()