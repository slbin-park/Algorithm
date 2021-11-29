import sys

input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = int(input())
    if a == 1:
        print(0)
        continue
    res = 0
    arr = list(map(int, input().split()))
    b = max(arr)  # n번
    visited = [0 for i in range(b + 1)]
    for j in range(a):
        for k in range(1, arr[j] + 1):
            visited[k] += 1
    print(res)
