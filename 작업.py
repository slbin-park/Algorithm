import sys
import collections
from collections import deque

input = sys.stdin.readline
n = int(input())
curt = [0 for i in range(n + 1)]  #시간
arr = collections.defaultdict(list)  #연결된 간선들
ign = [0 for i in range(n + 1)]  #간선의 개수
res = [0 for i in range(n + 1)]
dq = deque()
for i in range(1, n + 1):
    arrip = list(map(int, input().split()))
    curt[i] = arrip[0]
    for j in range(arrip[1]):
        arr[arrip[j + 2]].append(i)
        ign[i] += 1
for i in range(1, n + 1):
    if ign[i] == 0:
        dq.append((i, curt[i]))
        res[i] = curt[i]
while dq:
    cur, cnt = dq.popleft()
    for i in arr[cur]:
        ign[i] -= 1
        res[i] = max(res[i], res[cur] + curt[i])
        if ign[i] == 0:
            dq.append((i, res[cur] + curt[i]))
print(max(res))
