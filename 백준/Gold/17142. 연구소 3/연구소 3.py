import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
n , m  = map(int,input().split())
# list(itertools.combinations(arr, m)
arr = [[]for i in range(n)]
wall = 0
virus = []
result = 1e9
for i in range(n):
    arr[i] = list(map(int,input().split()))
    for j in range(n):
        if arr[i][j] == 2:
            virus.append([i,j])
        if arr[i][j] == 1:
            wall+=1     
            
for items in list(combinations(virus, m)):
    dq = deque()
    visited = [[-1 for i in range(n)]for i in range(n)]
    cnt = 0
    for item in items:
        dq.append(item)
        visited[item[0]][item[1]] = 0
    min_time = 0
    while dq:
        if n*n-wall-len(virus) == cnt:
            break;
        x,y, =dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y]+1
                    min_time = visited[x][y]+1
                    dq.append([nx,ny])
                    if arr[nx][ny]==0:
                        cnt+=1
    # print(min_time)
    # for i in visited:
    #     print(i)
    # print()
    if n*n-wall-len(virus) == cnt:
        result = min(min_time,result)
if(result == 1e9):
    print(-1)
else: print(result)

