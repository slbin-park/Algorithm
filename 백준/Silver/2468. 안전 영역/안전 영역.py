import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(x,y):
    global visited
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny] == 0 and arr[nx][ny]>h:
                visited[nx][ny] = 1
                dfs(nx,ny)
            
n = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
arr = []
mn = 0
for i in range(n):
    arr.append(list(map(int,input().split())))
visited = [[0 for i in range(n)]for i in range(n)]
result = 1
h = 1
while True:
    cur_cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and arr[i][j]>h:
                dfs(i,j)
                cur_cnt+=1
    result = max(result,cur_cnt)
    if cur_cnt == 0:
        break;
    visited = [[0 for i in range(n)]for i in range(n)]
    h+=1
print(result)
        