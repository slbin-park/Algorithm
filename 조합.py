import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0 for i in range(n + 1)]
arr[1] = 1
for i in range(2, n + 1):
    arr[i] = arr[i - 1] * i
print(arr[n] // (arr[m] * arr[n - m]))
