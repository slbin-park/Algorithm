import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n , m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
result = 0
left , right = 1 ,max(arr)
while left<=right:
    mid = (left+right)//2
    cur_cnt = 0
    for i in range(n):
        cur_cnt+= arr[i]//mid
    if m <= cur_cnt :
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)