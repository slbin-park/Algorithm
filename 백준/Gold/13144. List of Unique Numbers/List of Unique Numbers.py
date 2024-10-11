import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dq = deque()
arr = list(map(int, input().split()))
vis = [0 for i in range(100001)]
idx = 0
result = 0
while idx < N:
    while vis[arr[idx]] == 1:
        number, curIdx = dq.popleft()
        vis[number] = 0
        result += idx - curIdx
    dq.append([arr[idx], idx])
    vis[arr[idx]] = 1
    idx += 1
while dq:
    number, curIdx = dq.popleft()
    result += len(arr) - curIdx
print(result)
