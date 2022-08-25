import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline


n , m = map(int,input().split())
arr = list(map(int,input().split()))
val = sum(arr)
if n < m:
    print(n)
else:
    left , right = 0 ,60000000000
    second = 0
    while left<=right:
        mid = (left+right)//2
        cnt = m
        for i in range(m):
            cnt += mid // arr[i]
        if cnt>= n:
            second = mid
            right = mid-1
        else:
            left = mid+1
    cnt = m
    for i in range(m):
        cnt+= (second-1)//arr[i]
    for i in range(m):
        if second % arr[i] == 0:
            cnt+=1
        if cnt == n:
            print(i+1)
            break;