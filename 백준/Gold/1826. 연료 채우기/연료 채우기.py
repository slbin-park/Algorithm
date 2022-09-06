from copy import deepcopy
import heapq
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
INF = 1e9
input = sys.stdin.readline


n = int(input())
cnt = 0
arr = []
oil = []
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
l,p = map(int,input().split())
# p는 현재 연료
# l은 가야할 거리
for i in range(n):
    if p < arr[i][0]:
        while oil:
            if p >= arr[i][0]:
                break;
            p += -heapq.heappop(oil)
            cnt+=1
        if p < arr[i][0]:
            break;
    heapq.heappush(oil,-arr[i][1])

while oil:
    if p >= l:
        break;
    p += -heapq.heappop(oil)
    cnt+=1

if  p >= l:
    print(cnt)
else:
    print(-1)