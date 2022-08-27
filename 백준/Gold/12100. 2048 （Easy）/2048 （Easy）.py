from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
input = sys.stdin.readline

def dfs(c_arr,index):
    global result
    if index == 5:
        result = max(max(map(max,c_arr)),result)
        return
    # 위로 이동
    n_arr = deepcopy(c_arr)
    # i 는 옆으로 이동함
    for i in range(n):
        top = 0
        for j in range(1,n):
            tmp = n_arr[j][i]
            n_arr[j][i] = 0
            if tmp !=0 :
                if n_arr[top][i] ==0:
                    n_arr[top][i] = tmp
                elif n_arr[top][i] == tmp:
                    n_arr[top][i] += tmp
                    top +=1
                else:
                    top+=1
                    n_arr[top][i] = tmp
                
    dfs(n_arr,index+1)
    n_arr = deepcopy(c_arr)
    # 밑으로 이동
    for i in range(n):
        top = n-1
        for j in range(n-2,-1,-1):
            tmp = n_arr[j][i]
            n_arr[j][i] = 0
            if tmp != 0 :
                if n_arr[top][i] == 0 :
                    n_arr[top][i] = tmp
                elif n_arr[top][i] == tmp:
                    n_arr[top][i] += tmp
                    top-=1
                else:
                    top-=1
                    n_arr[top][i] = tmp
    dfs(n_arr,index+1)
    
    n_arr = deepcopy(c_arr)
    # 오른쪽으로 이동
    # 처음에 높이를 고정 시킴
    for i in range(n):
        top = n-1
        for j in range(n-2,-1,-1):
            tmp = n_arr[i][j]
            n_arr[i][j] = 0
            if tmp != 0:
                if n_arr[i][top] == 0:
                    n_arr[i][top] = tmp                
                elif n_arr[i][top] == tmp:
                    n_arr[i][top] += tmp
                    top-=1
                else:
                    top-=1
                    n_arr[i][top] = tmp
    dfs(n_arr,index+1)
    
    n_arr = deepcopy(c_arr)
    # 왼쪽으로 이동시킴
    # 처음에 높이를 고정 시킴
    for i in range(n):
        top = 0
        for j in range(1,n):
            tmp = n_arr[i][j]
            n_arr[i][j] = 0
            if tmp != 0:
                if n_arr[i][top] == 0:
                    n_arr[i][top] = tmp
                elif n_arr[i][top] == tmp:
                    n_arr[i][top] += tmp
                    top+=1
                else:
                    top+=1
                    n_arr[i][top] = tmp
    dfs(n_arr,index+1)
      
result = 0      
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dfs(arr,0)
print(result)