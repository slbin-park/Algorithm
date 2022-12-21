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
a,b,c = map(int,input().split())
x,y,z = map(int,input().split())
flag = True
while flag:
    flag = False
    if a!=0 and x!=0:
        flag = True
        d = min(a,x)
        x -= d
        a -= d
        answer+=d
    if a == 0 and x>=3:
        flag = True
        y += x//3
        x = x%3
    if b !=0 and y!=0:
        flag = True
        d = min(b,y)
        b -= d
        y -= d
        answer += d
    if b == 0 and y>=3:
        flag = True
        z += y//3
        y = y%3
    if c!=0 and z!=0 :
        flag = True
        d = min(c,z)
        c -= d
        z -= d
        answer += d
    if c == 0 and z>=3:
        flag = True
        x += z//3
        z = z%3
print(answer)