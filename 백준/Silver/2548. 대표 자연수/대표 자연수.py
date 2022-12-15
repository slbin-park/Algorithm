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
arr = list(map(int,input().split()))
arr.sort()
answer = 1e9
c_cum = 1e9
for item in arr:
    cur_sum = 0
    for jtem in arr:
        cur_sum += abs(item-jtem)
    if c_cum  > cur_sum:
        answer = item
        c_cum = cur_sum
print(answer)