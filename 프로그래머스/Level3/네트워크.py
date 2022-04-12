from collections import deque


def solution(n, computers):
    answer = 0
    dq = deque()
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0:
            dq.append(i)
            answer += 1
            while dq:
                x = dq.popleft()
                for i in range(n):
                    if i != x and visited[i] == 0 and computers[x][i] == 1:
                        visited[i] = 1
                        dq.append(i)
    return answer