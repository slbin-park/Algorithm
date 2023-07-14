from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print("Case #", end="")
    print(i + 1, end="")
    print(":", a, "+", b, "=", a + b)
