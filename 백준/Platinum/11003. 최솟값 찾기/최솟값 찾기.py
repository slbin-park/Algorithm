from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys
sys.setrecursionlimit(10**5)

INF = 1e9
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
dq =deque()

def get_index(i):
    if i-m+1 < 0:
        return 0
    return i-m+1
for i in range(n):
    # 인덱스 오버되는거 다 삭제
    while dq and dq[0][1] < get_index(i):
        dq.popleft()
    # 삽입할때 현재삽입할려는것보다 작은거 다 삭제
    while dq and dq[-1][0] >= arr[i]:
        dq.pop()
    dq.append([arr[i],i])
    print(dq[0][0],end=" ")