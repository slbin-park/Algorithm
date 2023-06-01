from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    cmd = input().strip().split(" ")
    # print(cmd)
    if cmd[0] == "push":
        stack.append(cmd[1])
    if cmd[0] == "top":
        print(stack[-1] if len(stack) else -1)
    if cmd[0] == "size":
        print(len(stack))
    if cmd[0] == "empty":
        print(0 if len(stack) else 1)
    if cmd[0] == "pop":
        print(stack.pop() if len(stack) else -1)
