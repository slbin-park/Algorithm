import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
