import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x,y):
    cur_cnt = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[ny][nx] == 0:
            graph[ny][nx] = 1
            cur_cnt+=dfs(nx,ny)
    return cur_cnt
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = []
result_cnt = 0
m , n , k = map(int,input().split())
graph = [[0 for i in range(n)]for i in range(m)]
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            graph[k][j] = 1
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result.append(dfs(j,i))
            result_cnt+=1
print(result_cnt)
result.sort()
print(*result)
            