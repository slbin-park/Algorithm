import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, end):
    dq.append((start, 0))
    visited = [0 for i in range(200002)]
    arr = [0 for i in range(200002)]
    arr[start] = start
    visited[start] = 1
    cnt = 0
    answer = []
    while dq:
        cur, curcnt = dq.popleft()
        if cur == end:
            cnt = curcnt
            while arr[cur] != cur:
                answer.append(cur)
                cur = arr[cur]
            return curcnt, answer
        if cur + 1 <= 100000:
            if visited[cur + 1] == 0:
                visited[cur + 1] = 1
                dq.append((cur + 1, curcnt + 1))
                arr[cur + 1] = cur
        if cur - 1 >= 0:
            if visited[cur - 1] == 0:
                visited[cur - 1] = 1
                dq.append((cur - 1, curcnt + 1))
                arr[cur - 1] = cur
        if cur * 2 <= 100000:
            if visited[cur * 2] == 0:
                visited[cur * 2] = 1
                dq.append((cur * 2, curcnt + 1))
                arr[cur * 2] = cur

    return cnt


n, m = map(int, input().split())
dq = deque()
res, resarr = bfs(n, m)
resarr.append(n)
resarr.reverse()
print(res)
for i in resarr:
    if i == resarr[-1]:
        print(i)
    else:
        print(i, end=' ')
