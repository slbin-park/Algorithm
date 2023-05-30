from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
arr = set()
for i in range(n):
    arr.add(input().strip())
arr = list(arr)
arr.sort(key=lambda x: (len(x),x))
for item in arr:
    print(item)
