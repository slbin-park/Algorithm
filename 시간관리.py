import sys

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((b, a))
arr.sort()
res = arr[0][0] - arr[0][1]
for i in range(n):
    a