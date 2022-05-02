import sys

input = sys.stdin.readline


def find(a):
    if a == arr[a]:
        return a
    arr[a] = find(arr[a])
    return arr[a]


def union(a, b, value):
    global res
    a = find(a)
    b = find(b)
    if a > b:
        arr[a] = b
    else:
        arr[b] = a


res = []
n, m = map(int, input().split())
arr = [i for i in range(n + 1)]
graph = []
for i in range(m):
    u, v, w = map(int, input().split())
    graph.append([u, v, w])
graph.sort(key=lambda x: x[2])
for u, v, w in graph:
    if find(u) != find(v):
        union(u, v, w)
        res.append(w)
print(sum(res) - res[-1])
