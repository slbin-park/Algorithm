import sys


# dfs
def dfs(x, y, z):
    global cnt

    cnt = max(cnt, z)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            dfs(nx, ny, z + 1)
            visited[graph[nx][ny]] = 0

    return cnt

r, c = map(int, sys.stdin.readline().split())
graph = [list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(r)]
visited = [0] * 26 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1
visited[graph[0][0]] = 1
print(dfs(0, 0, cnt))