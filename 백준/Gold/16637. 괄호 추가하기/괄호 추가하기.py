from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

answer = -2e9

# sys.setrecursionlimit(10**5)

# 0 = 0,1
# 1 = 1,2
# 2 = 2,3
# 3 = 3,4


def get_value(a, b, oper):
    if oper == "+":
        return a + b
    if oper == "-":
        return a - b
    if oper == "*":
        return a * b


def get_order(depth, v):
    global answer
    if depth == n // 2:
        answer = max(answer, v)
        # print(v)
        return
    # 오퍼레이터를 지금 써버림
    cur_v = get_value(v, number[depth + 1], opers[depth])
    # print("dpeth = ", depth, "v = ", cur_v)
    get_order(depth + 1, cur_v)
    # 오퍼레이터를 다음 꺼 먼저함
    if depth < n // 2 - 1:
        cur_v1 = get_value(number[depth + 1], number[depth + 2],
                           opers[depth + 1])
        cur_v2 = get_value(v, cur_v1, opers[depth])
        get_order(depth + 2, cur_v2)


input = sys.stdin.readline
n = int(input())
arr = input().rstrip()
number = []
opers = []
for i in range(n):
    if i % 2 == 0:
        number.append(int(arr[i]))
    else:
        opers.append(arr[i])
get_order(0, number[0])
print(answer)