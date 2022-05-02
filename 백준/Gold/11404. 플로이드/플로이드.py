import sys

input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
arr = [[INF for i in range(n + 1)] for i in range(n + 1)]

for i in range(m):
    u, v, w = map(int, input().split())
    arr[u][v] = min(arr[u][v], w)

for k in range(1, n + 1):  # 거치는 점
    for i in range(1, n + 1):  # 시작점
        for j in range(1, n + 1):  # 끝점
            if i == j:
                arr[i][j] = 0
            elif arr[i][j] > arr[i][k] + arr[k][j]:  # k를 거쳐서 j로 가는게 더 빠를경우
                arr[i][j] = arr[i][k] + arr[k][j]
for i in range(1, n + 1):
    for j in range(1, n):
        if arr[i][j] == INF: print(0, end=' ')
        else: print(arr[i][j], end=' ')
    if arr[i][-1] == INF: print(0)
    else: print(arr[i][-1])
