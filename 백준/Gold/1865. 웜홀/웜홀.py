import sys
import heapq
import math

input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def bellman_ford(start):
    dis = [INF for i in range(n + 1)]
    # 노드의 개수만큼 반복
    for i in range(n):
        # 간선을 모두 확인한다
        for j in range(len(arr)):
            cur_node = arr[j][0]
            next_node = arr[j][1]
            cost = arr[j][2]
            if dis[next_node] > dis[cur_node] + cost:
                dis[next_node] = dis[cur_node] + cost
                if i == n - 1:
                    return True
    return False


T = int(input())
for _ in range(T):
    arr = []
    n, m, w = map(int, input().split())

    for _ in range(m):
        s, e, t = map(int, input().split())
        arr.append([s, e, t])
        arr.append([e, s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        arr.append([s, e, -t])
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")
