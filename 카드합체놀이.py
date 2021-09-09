import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(m):
    arr.sort()
    temp = arr[0] + arr[1]
    arr[0] = temp
    arr[1] = temp
print(sum(arr))
