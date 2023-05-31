from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a = input().rstrip()
    a = a.split(" ")
    a[0] = int(a[0])
    a.append(i)
    arr.append(a)
arr.sort(key=lambda x:(int(x[0]),x[2]))
for age,name,index in arr:
    print(age,name)
