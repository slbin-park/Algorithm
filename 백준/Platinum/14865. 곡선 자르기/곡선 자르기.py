from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys
sys.setrecursionlimit(10**5)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
INF = int(1e9)
input = sys.stdin.readline
arr = []
n = int(input())
stack = []
x,y = map(int,input().split())
cnt = 0
for i in range(n-1):
    nx,ny = map(int,input().split())
    # 내려가는 경우
    if y>0 and ny<0:
        # 앞에서 올라가지 않았는데
        # 내려가는 경우 stack에 넣음
        if len(stack)==0:
            cnt+=1
            stack.append([nx,cnt])
        else:
            cx,cur_cnt = stack.pop()
            arr.append([cx,cur_cnt])
            arr.append([nx,cur_cnt])
    # 올라가는 경우
    # 무조건 스택에 넣음
    if y<0 and ny>0:
        cnt+=1
        stack.append([nx,cnt])
    y = ny
    x = nx
# 스택에 1개 있을 경우는
while len(stack)>1:
    cnt+=1
    dx = stack.pop()
    arr.append([dx[0],cnt])
    dx = stack.pop()
    arr.append([dx[0],cnt])
if len(stack)==1:
    cnt+=1
    dx = stack.pop()
    arr.append([dx[0],cnt])
    arr.append([x,cnt])
arr.sort()
stack = []
first = 0
second = 0
for i in range(len(arr)):
    if len(stack)==0:
        stack.append(arr[i])
    else:
        if stack[-1][1] == arr[i][1]:
            if arr[i][1] == arr[i-1][1]:
                second+=1
            stack.pop()
            if len(stack)==0:
                first+=1
        else:
            stack.append(arr[i])

print(first,second)