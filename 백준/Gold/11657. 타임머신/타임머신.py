import sys
import heapq
import math

input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def bellman_ford():
    dis[1] = 0
    # 노드의 개수만큼 반복
    for i in range(n):
        # 간선을 모두 확인한다
        for j in range(m):
            cur_node = arr[j][0]
            next_node = arr[j][1]
            cost = arr[j][2]
            if dis[cur_node] != INF and dis[next_node] > dis[cur_node] + cost:
                dis[next_node] = dis[cur_node] + cost
                if i == n - 1:
                    return False
    return True


n, m = map(int, input().split())
dis = [INF] * (n + 1)
arr = []
for i in range(m):
    u, v, w = map(int, input().split())
    arr.append([u, v, w])

if bellman_ford():
    for i in range(2, n + 1):
        if dis[i] == INF:
            print("-1")
            continue
        print(dis[i])
else:
    print(-1)