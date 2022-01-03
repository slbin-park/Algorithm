import sys
from collections import deque

input = sys.stdin.readline
a, b, c = map(int, input().split())
dq = deque([0 for i in range(b)])
arr = list(map(int, input().split()))
dq1 = deque(arr)
res = 0
curl = 0  # 하중
while dq:
    res += 1
    dq.popleft()
    if dq1:
        if sum(dq) + dq1[0] <= c:
            dq.append(dq1.popleft())
        else:
            dq.append(0)
print(res)
