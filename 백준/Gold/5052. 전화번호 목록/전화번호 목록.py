from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
input = sys.stdin.readline

n = int(input())
for i in range(n):
    m = int(input())
    arr = []
    for i in range(m):
        arr.append(input().strip())
    arr.sort()
    flag = 0
    for i in range(m-1):
        leng = len(arr[i])
        if arr[i] == arr[i+1][:leng]:
            flag = 1
            break;
    if flag==1:
        print('NO')
    else:
        print('YES')