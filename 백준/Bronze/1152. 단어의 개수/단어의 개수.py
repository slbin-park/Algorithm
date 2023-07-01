from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

input = sys.stdin.readline
n = input().strip()
n = n.split(" ")
res = 0
for i in range(len(n)):
    if n[i] != " " and n[i] != "":
        res += 1
print(res)
