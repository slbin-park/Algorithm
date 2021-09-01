import sys
from collections import deque
input = sys.stdin.readline
def dfs(x,y):
    dq.append([x,y])
    while(dq):
        a = dq.popleft()
        x = a[0]
        y = a[1]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] ==1 and visited[nx][ny] ==0 :
                        dq.append([nx,ny])
                        visited[nx][ny] = visited[x][y]+1




n,m= map(int,input().split())
arr = [[0 for i in range(m)] for j in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
visited[0][0] = 1
dq = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    a = input()
    for j in range(m):
        arr[i][j] = int(a[j])
dfs(0,0)
print(visited[n-1][m-1])