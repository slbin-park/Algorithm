import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr2 = [0 for i in range(n)]
arr.sort()
for i in range(n):
    arr[i] = arr[i] - i
print(max(arr) + 1 + n)
