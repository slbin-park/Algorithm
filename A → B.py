import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global res
    while dq:
        cur, cnt = dq.popleft()
        if cur == b:
            res = cnt
            break
        if cur*2 <= b:
            dq.append((cur*2, cnt+1))

        if int(str(cur)+'1') <= b:
            dq.append((int(str(cur)+'1'), cnt+1))


a, b = map(int, input().split())
dq = deque([(a, 1)])
res = -1
bfs()
print(res)
