from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
input = sys.stdin.readline


# 루트 찾기
def find(x):
    if x != root[x]:
        return find(root[x])
    return root[x]

while 1:
    m , n = map(int,input().split())
    if m == 0 and n == 0 : 
        break;
    arr = []
    root = [i for i in range(m+1)]
    value = 0
    for i in range(n):
        a,b,c = map(int,input().split())
        arr.append([a,b,c])
        value+=c
    arr.sort(key=lambda x : x[2])
    result = 0
    for a,b,c in arr:
        ar = find(a)
        br = find(b)
        if ar != br:
            if ar > br:
                root[ar] = br
            else:
                root[br] = ar
            result+=c
    print(value - result)