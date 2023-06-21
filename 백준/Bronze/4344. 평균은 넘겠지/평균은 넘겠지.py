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
for i in range(n):
    arr = list(map(int, input().split()))
    arrSum = sum(arr) - arr[0]
    avg = arrSum / arr[0]
    cnt = 0
    for j in range(1, len(arr)):
        if arr[j] > avg:
            cnt += 1
    per = round(decimal.Decimal(cnt * 100 / arr[0]), 3)
    print("%.3f" % per + "%")
