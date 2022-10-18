import sys
import heapq
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
arr = []
white = 0
blue = 0
for i in range(n):
    arr.append(list(map(int,input().split())))

def div(startx,starty,cur_n):
    cur_n = cur_n//2
    dfs(startx,starty,cur_n) # 왼쪽
    dfs(startx,starty+cur_n,cur_n) # 오른쪽
    dfs(startx+cur_n,starty,cur_n) # 왼쪽밑
    dfs(startx+cur_n,starty+cur_n,cur_n) #오른쪽 밑

def dfs(startx,starty,cur_n):
    global white,blue
    for i in range(startx,startx+cur_n):
        for j in range(starty,starty+cur_n):
            if arr[startx][starty] != arr[i][j]:
                div(startx,starty,cur_n)
                return
    if arr[startx][starty]==1:
        blue+=1
    else:
        white+=1
dfs(0,0,n)
print(white)
print(blue)