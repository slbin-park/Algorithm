import sys
from collections import deque
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

result = []
n = int(input())
for i in range(n):
    a = int(input())
    if a==0:
        result.pop()
    else:
        result.append(a)
print(sum(result))