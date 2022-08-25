import sys
from collections import deque
input = sys.stdin.readline

def dfs(x,y):
    dq.append((x,y))
    while dq:
        x,y = dq.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<a and ny>=0 and ny<b:
                if arr[nx][ny]==1:
                    dq.append((nx,ny))
                    arr[nx][ny] =2

n = int(input())
cnt=0
dq = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(n):
    a ,b ,m  =  map(int,input().split())
    arr = [[0 for i in range(b)] for j in range(a)]
    cnt = 0
    for j in range(m):
        k,l = map(int,input().split())
        arr[k][l] = 1
    for i in range(a):
        for j in range(b):
            if(arr[i][j]==1):
                dfs(i,j)
                cnt+=1
    print(cnt)
