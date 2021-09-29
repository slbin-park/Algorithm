import collections
import sys

input = sys.stdin.readline
arr = {}
n, m = map(int, input().split())
for i in range(n):
    a = input().split()
    arr[a[0]] = a[1]
for i in range(m):
    a = input().strip()
    print(arr[a])
