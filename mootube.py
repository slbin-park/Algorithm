import sys

sys.setrecursionlimit(10**5)


def find_video(start, prevmin, k):
    global cnt
    for i in v[start]:
        if visited[i[0]] == 0 and min(prevmin, i[1]) >= k:
            visited[i[0]] = 1
            cnt += 1
            find_video(i[0], min(prevmin, i[1]), k)


input = sys.stdin.readline
n, q = map(int, input().split())
cnt = 0
v = [[] for i in range(n + 1)]
for i in range(n - 1):
    pi, qi, ri = map(int, input().split())
    v[pi].append((qi, ri))
    v[qi].append((pi, ri))
for i in range(q):
    cnt = 0
    ki, vi = map(int, input().split())
    visited = [0] * (n + 1)
    visited[vi] = 1
    find_video(vi, 100000001, ki)
    print(cnt)
