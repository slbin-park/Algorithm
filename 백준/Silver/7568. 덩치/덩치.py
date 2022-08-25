import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline


n = int(input())
arr = []
ranking = [0 for i in range(n)]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    cnt = 0
    for j in range(n):
        if i!=j:
            if arr[i][0] <arr[j][0] and arr[i][1] <arr[j][1]:
                cnt+=1
    ranking[i] = cnt+1
for i in range(n-1):
    print(ranking[i],end=' ')
print(ranking[-1],end='')