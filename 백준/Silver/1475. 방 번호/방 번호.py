import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n = input().strip()
arr = [0 for i in range(10)]
for i in range(len(n)):
    if int(n[i]) == 6 or int(n[i]) == 9:
        if arr[6] >= arr[9]:
            arr[9]+=1
        else:
            arr[6]+=1
    else:
        arr[int(n[i])]+=1
print(max(arr))
        