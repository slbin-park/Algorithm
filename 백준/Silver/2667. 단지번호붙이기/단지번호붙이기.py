import sys
from collections import deque
input = sys.stdin.readline


def bfs(x,y):
    count = 0
    arr2 = []
    for i in range(n):
        for j in range(n):
            count=0
            if arr[i][j] ==1:
                dq.append([i,j])
                while dq:
                    a=dq.pop()
                    x = a[0] #세로 
                    y = a[1] #가로
                    #print('vis',visited[x][y])
                    if visited[x][y] == 0:
                        count+=1
                        #print('x,y',x,y)
                        if y+1<n:
                            if arr[x][y+1] == 1:
                                dq.append([x,y+1])
                        if x+1<n:
                            if arr[x+1][y] == 1:
                                dq.append([x+1,y])
                        if y-1 >= 0:
                            if arr[x][y-1] ==1:
                                dq.append([x,y-1])
                        if x-1 >=0 :
                            if arr[x-1][y] == 1:
                                dq.append([x-1,y])
                    visited[x][y] = 1
                if(count>0):
                    arr2.append(count)
    return arr2

                
n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
visited = [[0 for i in range(n)] for j in range(n)]
dq = deque()
for i in range(n):
    a = input()
    for j in range(n):
        arr[i][j] = int(a[j])
arr2=bfs(0,0)
print(len(arr2))
arr2.sort()
for i in arr2:
    print(i)