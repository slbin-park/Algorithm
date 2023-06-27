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
res = 0
rres = 0
bres = 0
rcnt = 0
bcnt = 0
prev = ""
for i in range(n):
    if str1[i] == "R":
        rcnt += 1
    elif str1[i] == "B" and prev == "R":
        rres += rcnt
        rcnt = 0
    if str1[i] == "B":
        bcnt += 1
    elif str1[i] == "R" and prev == "B":
        bres += bcnt
        bcnt = 0
    prev = str1[i]
res = min(bres, rres)
rres = 0
bres = 0
rcnt = 0
bcnt = 0
prev = ""
for i in range(n - 1, -1, -1):
    if str1[i] == "R":
        rcnt += 1
    elif str1[i] == "B" and prev == "R":
        rres += rcnt
        rcnt = 0
    if str1[i] == "B":
        bcnt += 1
    elif str1[i] == "R" and prev == "B":
        bres += bcnt
        bcnt = 0
    prev = str1[i]
res = min(res, rres, bres)
print(res)
