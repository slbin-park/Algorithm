import sys
import heapq
from copy import deepcopy
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
res = []
index = 1
while len(res)!=n:
    if  '666' in str(index):
        res.append(index)
    index+=1
print(res[-1])