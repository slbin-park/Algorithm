import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr = sorted(arr, key=lambda a: a[0])
arr = sorted(arr, key=lambda a: a[1])
print(arr)
