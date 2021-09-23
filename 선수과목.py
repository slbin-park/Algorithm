import sys
import collections
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
cur = [0 for i in range(n + 1)]
res = [0 for i in range(n + 1)]
dq = deque()
arr = collections.defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    res[b] += 1

for i in range(1, n + 1):
    if res[i] == 0:  #진입차수가 0 이면
        dq.append((i, 1))  #진입차수가 0 인것을 dq에 삽입
        cur[i] = 1  #1학기에 바로 이수 가능

while dq:
    a, cnt = dq.popleft()
    for i in arr[a]:
        res[i] -= 1
        if res[i] == 0:
            dq.append((i, cnt + 1))
            cur[i] = cnt + 1
print(*cur[1:])
