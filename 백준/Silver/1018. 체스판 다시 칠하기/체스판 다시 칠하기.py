import sys
import heapq
from copy import deepcopy
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n ,m = map(int,input().split())
arr = [[''for i in range(m)]for i in range(n)]
for i in range(n):
    a = input().rstrip()
    for j in range(m):
        arr[i][j] = a[j]
def check(x,y):
    cur_cnt1 = 0
    flag = 0
    for i in range(x,x+8):
        flag +=1
        for j in range(y,y+8):
            if (flag+j)%2==0 and arr[i][j] == 'B':
                cur_cnt1+=1
            elif (flag+j)%2==1 and arr[i][j] == 'W':
                cur_cnt1+=1
    cur_cnt2 = 0
    flag = 1
    for i in range(x,x+8):
        flag +=1
        for j in range(y,y+8):
            if (flag+j)%2==0 and arr[i][j] == 'B':
                cur_cnt2+=1
            elif (flag+j)%2==1 and arr[i][j] == 'W':
                cur_cnt2+=1
    return min(cur_cnt1,cur_cnt2)
res = 1e9
for i in range(n-7):
    for j in range(m-7):
        res = min(res,check(i,j))
print(res)