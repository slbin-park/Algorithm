import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end):
    dq.append((start, 0))
    visited = [0 for i in range(200002)]
    cnt = 100000
    global rescnt
    while dq:
        cur, curcnt = dq.popleft()
        if cur == end:
            cnt = curcnt
            rescnt += 1
            print(dq)
        if curcnt > cnt:
            break
        if cur + 1 <= 100000:
            if visited[cur + 1] == 0:
                visited[cur + 1] = 1
                dq.append((cur + 1, curcnt + 1))
        if cur - 1 >= 0:
            if visited[cur - 1] == 0:
                visited[cur - 1] = 1
                dq.append((cur - 1, curcnt + 1))
        if cur * 2 <= 100000:
            if visited[cur * 2] == 0:
                visited[cur * 2] = 1
                dq.append((cur * 2, curcnt + 1))
    return cnt


rescnt = 0
n, m = map(int, input().split())
dq = deque()
res = bfs(n, m)
print(res)
print(rescnt)