import collections
import sys
import math

input = sys.stdin.readline
arr = {}
n, m = map(int, input().split())
for i in range(n):
    a = str(input().strip())
    arr[a] = str(i + 1)
    arr[str(i + 1)] = a
for i in range(m):
    a = input().strip()
    print(arr[a])
