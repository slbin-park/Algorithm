import sys
from collections import deque

dq = deque()
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[[] for i in range(n + 1)] for i in range(n + 1)]
visited = [[0 for i in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    inp = list(map(int, input().split()))
    arr[inp[0]][inp[1]].append([inp[2], inp[3]])
for i in arr[1][1]:
    dq.append(i)
print(dq)
while dq:
    a, b = dq.popleft()
