import sys

input = sys.stdin.readline
n = int(input())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())
arr.sort()
res = 0
for i in range(n):
    res += abs(arr[i] - (i + 1))
print(res)