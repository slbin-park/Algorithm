import sys
from collections import deque
 
input = sys.stdin.readline
 
def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
 
    return parent[a]
 
def union(parent, a, b):
    p1 = find(parent, a)
    p2 = find(parent, b)
    if p1 != p2:
        if p1 > p2:
            parent[p1] = p2
        else:
            parent[p2] = p1
 
case = 0
while True:
    n, m = map(int, input().rstrip().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n+1)]
    cycle = []
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        p1 = find(parent, a)
        p2 = find(parent, b)
        if p1 != p2:
            union(parent, a, b)
        else:
            # cycle이 발생한 케이스이므로 따로 저장
            cycle.append(a)
    # 갱신
    for i in range(n+1):
        find(parent, i)
 
    # cycle이 있는 그룹들 저장
    group = set()
    for cycle_vertex in cycle:
        group.add(parent[cycle_vertex])
 
    answer = 0
    for i in range(1, n+1):
        if parent[i] in group:
            continue
        answer += 1
        group.add(parent[i])
 
    case += 1
    if answer == 0:
        print("Case %d: No trees."%(case))
    elif answer == 1:
        print("Case %d: There is one tree."%(case))
    else:
        print("Case %d: A forest of %d trees."%(case, answer))
