from copy import deepcopy
import heapq
from re import A
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline


def find_dir(dir_):
    if dir_ == 0 or dir_ == 1:
        return [2,3]
    if dir_ == 2 or dir_ == 3:
        return [0,1]
def bfs():
    for i in range(4):
        nx = startx + dx[i]
        ny = starty + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] != '*': 
                dq.append([startx,starty,i,0])
    while dq:
        x,y,dir,cnt = dq.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        while 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] =='*':
                break;
            # 거울이 있을경우 양옆 위아래로 반사
            if arr[nx][ny] == '#':
                if visited[nx][ny][dir] > cnt:
                    visited[nx][ny][dir] = cnt                
            if arr[nx][ny] == '!':
                if visited[nx][ny][dir] > cnt+1:
                    visited[nx][ny][dir] = cnt+1
                    next_dir = find_dir(dir)
                    for i in next_dir:
                        dq.append([nx,ny,i,cnt+1])
            nx+=dx[dir]
            ny+=dy[dir]
                        
                    
# 0 오른쪽 반사하면 2,3
# 1 왼쪽  반사하면 2,3
# 2 밑쪽 반사하면 0,1
# 3 윗쪽 반ㅏ하면 0,1
n = int(input())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
arr = [[''for i in range(n)]for i in range(n)]
visited = [[[INF]*4 for i in range(n)]for i in range(n)]
startx , starty = 0,0
result = []
dq = deque()
for i in range(n):
    inp = input().rstrip()
    for j in range(n):
        arr[i][j] = inp[j]
        if inp[j] == '#':
            result.append([i,j])
            startx = i
            starty = j
bfs()
ans = 1e9
cur_min = min(visited[result[0][0]][result[0][1]])
ans = min(cur_min,ans)
print(ans)
