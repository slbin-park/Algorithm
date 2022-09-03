from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
from xml.dom.minicompat import NodeList
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))

import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

left = {}
def dfs(index,end,value,dir):
    global cnt,m
    if index == end:
        if dir == 'left':
            if not value in left:
                left[value]=1
            else:
                left[value]+=1
        else:
            if m - value in left:
                cnt += left[m - value]
        return
    dfs(index+1,end,value,dir)
    dfs(index+1,end,value+arr[index],dir)
n,m = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
dfs(0,n//2,0,'left')
dfs(n//2,n,0,'right')
if m==0:
    cnt-=1
print(cnt)