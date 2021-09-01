import sys
from collections import deque


def dfs(v1, t):
    visited = [0]*n
    print('v', v1)
    cnt = 0
    dq.append([v1, cnt])
    while dq:
        x = dq.popleft()
        value = x[0]  # 노드번호
        count = x[1]  # 카운터
        print('value = ', value)
        print('visited', visited[value])
        if value == t:
            return count
        if visited[value] == 0:
            count += 1
            visited[value] = 1
            for i in res[value]:
                if not visited[i]:
                    print('i = ', i)
                    dq.append([i, count])
    return -1


n = int(input())
v, target = map(int, input().split())
res = [[] for i in range(n)]
m = int(input())
dq = deque()
for i in range(m):
    a, b = map(int, input().split())
    res[a-1].append(b-1)
    res[b-1].append(a-1)
print(res)
result = dfs(v-1, target-1)
print(result)
