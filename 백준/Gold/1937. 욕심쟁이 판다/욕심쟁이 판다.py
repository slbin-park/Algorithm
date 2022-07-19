import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x,y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] > arr[x][y]:
                dp[x][y] = max(dfs(nx,ny),dp[x][y])
    return dp[x][y]+1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0
n = int(input())
arr = []
dp = [[-1 for _ in range(n)]for i in range(n)]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if dp[i][j]==-1:
            dfs(i,j)
            # for item in dp:
            #     print(item)
            # print()
print(max(map(max,dp))+1)