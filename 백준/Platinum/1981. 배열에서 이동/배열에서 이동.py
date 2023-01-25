import sys
import heapq
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
prev = 0


def bfs(diff):
    for i in range(min_v, max_v - diff+1):
        visited = [[0 for i in range(n)] for i in range(n)]
        dq = deque()
        if arr[0][0] < i or arr[0][0] > i + diff:
            continue
        dq.append([0, 0])
        visited[0][0] = 1
        while dq:
            x, y = dq.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == 0 and i <= arr[nx][ny] <= i + diff:
                        if nx == n - 1 and ny == n - 1:
                            return True
                        visited[nx][ny] = 1
                        dq.append([nx, ny])
    return False;


answer = 0
n = int(input())
min_v = 1e9
max_v = 0
arr = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
    min_v = min(min_v, min(arr[i]))
    max_v = max(max_v, max(arr[i]))
left = 0
right = max_v - min_v
answer = 1e9
while left <= right:
    mid = (left + right) // 2
    if (bfs(mid)):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
