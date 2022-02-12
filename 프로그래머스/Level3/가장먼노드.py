from collections import deque


def dfs(arr, n):
    dq = deque()
    dq.append((1, 1))
    visited = [0 for i in range(n + 1)]
    visited[1] = 1
    while dq:
        idx, cnt = dq.popleft()
        for i in arr[idx]:
            if visited[i] == 0:
                dq.append((i, cnt + 1))
                visited[i] = cnt + 1
    maxn = max(visited)
    res = 0
    for i in range(n + 1):
        if visited[i] == maxn:
            res += 1
    return res


def solution(n, edge):
    answer = 0
    arr = [[] for i in range(n + 1)]
    for i in range(len(edge)):
        arr[edge[i][0]].append(edge[i][1])
        arr[edge[i][1]].append(edge[i][0])
    return dfs(arr, n)
