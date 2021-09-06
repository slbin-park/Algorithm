import sys
from types import resolve_bases

input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(n + 1)]
res = 0
cnt = 1
for i in range(1, n + 1):
    arr[i] = int(input())
arr.sort(reverse=True)
res = arr[0]
for i in range(1, n + 1):
    if res < arr[i] * (i + 1):
        res = arr[i] * (i + 1)
print(res)
