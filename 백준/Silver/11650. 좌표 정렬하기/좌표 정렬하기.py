from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

n = int(input())
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append([x,y])
arr.sort()
for x,y in arr:
    print(x,y)