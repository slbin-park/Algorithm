from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
sys.setrecursionlimit(10**5)

n = int(input())
str1 = input().rstrip()
# R을 더 올림
res = 1e9
cnt = 0
rcnt = 0
prev = "B"
for i in range(n):
    if str1[i] == "R":
        rcnt += 1
        prev = "R"
    elif str1[i] == "B" and prev == "R":
        cnt += rcnt
        rcnt = 0
    if str1[i] == "B":
        prev = "B"
res = min(res, cnt)
cnt = 0
bcnt = 0
for i in range(n):
    if str1[i] == "B":
        bcnt += 1
        prev = "B"
    elif str1[i] == "R" and prev == "B":
        cnt += bcnt
        bcnt = 0
    if str1[i] == "R":
        prev = "R"
res = min(res, cnt)
print(res)
