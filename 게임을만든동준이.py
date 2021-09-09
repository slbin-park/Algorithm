import sys

input = sys.stdin.readline
n = int(input())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())
arr.reverse()
cnt = 0
for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        cnt += arr[i] - (arr[i - 1] - 1)
        arr[i] = arr[i - 1] - 1
print(cnt)