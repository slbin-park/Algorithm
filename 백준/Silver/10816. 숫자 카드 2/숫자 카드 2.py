from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
n = int(input())
arr = list(map(int,input().split()))
cnt = {}
m = int(input())
result = list(map(int,input().split()))
for i in arr:
    try:
        cnt[i]+=1
    except:
        cnt[i]=1
for i in range(m-1):
    try:
        print(cnt[result[i]],end=' ')
    except:
        print(0 , end=' ')
try:
    print(cnt[result[-1]])
except:
    print(0)