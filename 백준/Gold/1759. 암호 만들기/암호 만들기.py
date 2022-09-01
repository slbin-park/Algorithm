from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))

def dfs(s,index):
    if index == m:
        if len(s) == n and 0<s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')<n-1:
            result.append(s)
            return 
        else:
            return
    dfs(s,index+1)
    dfs(s+arr[index],index+1)
        
n , m = map(int,input().split())
arr = list(map(str,input().split()))
arr.sort()
result = []
dfs('',0)
result.sort()
for i in result:
    print(i)