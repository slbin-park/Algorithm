import sys
import heapq
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
prev = 0
answer = 0


def hang(x,y):
    while y+1<b:
        y += 1
        if arr[x][y] != "-":
            break;
        visited[x][y] = 1
def yull(x,y):
    while x+1<a:
        x+=1
        if arr[x][y] != "|":
            break;
        visited[x][y] = 1
        
a,b = map(int,input().split())
arr = [[""for i in range(b)]for i in range(a)]
visited = [[0 for i in range(b)]for i in range(a)]
for i in range(a):
    c = input().strip()
    for j in range(b):
        arr[i][j] = c[j]

for i in range(a):
    for j in range(b):
        if visited[i][j] == 0:
            if arr[i][j] == "-":
                answer+=1
                hang(i,j)
            else:
                answer+=1
                yull(i,j)
print(answer)
