from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()
res = 0
for i in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        if arr[2] == 1:
            res += arr[1]
        else:
            dq.append((arr[1], arr[2]-1))
    elif len(dq) > 0:
        x, y = dq.pop()
        if y == 1:
            res += x
        else:
            dq.append((x, y-1))
print(res)
