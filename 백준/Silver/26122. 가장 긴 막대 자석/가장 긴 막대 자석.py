import sys
import heapq
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
prev = 0
n = int(input())
a = input().strip()
answer = 0
cnt_n = 0
cnt_s = 0
prev = a[0]
prev_cnt = 1
i=1
while i<len(a):
    if prev != a[i]:
        cnt = 1
        while i<len(a)-1 and a[i] == a[i+1]:
            i+=1
            cnt+=1
        answer = max(answer,min(cnt,prev_cnt)*2)
        prev_cnt = cnt
        prev = a[i]
    else:
        prev_cnt+=1
    i+=1
print(answer)