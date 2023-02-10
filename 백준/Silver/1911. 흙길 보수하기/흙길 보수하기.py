import sys
from collections import deque
input = sys.stdin.readline

n,l = map(int,input().split())

def add_cnt():
    global start,end,cnt
    a = (end - start)//l
    if((end-start)%l > 0):
        cnt+=1
        end += l - (end - start)%l
    cnt += a

arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort()
cnt = 0
start , end = arr[0][0],arr[0][1]
add_cnt()
for i in range(1,n):
    if arr[i][0] > end:
        start = arr[i][0]
        end = arr[i][1]
        add_cnt()
    elif end < arr[i][1]:
        start = end
        end = arr[i][1]
        add_cnt()
print(cnt)