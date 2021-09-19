import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = [(0) for i in range(n)]
arr.sort()
sum = arr[0]
for i in range(1, n):
    sum += arr[i]
    if sum < (i + 1) * (i) // 2:
        print(-1)
        exit(0)
if sum == n * (n - 1) // 2:
    print(1)
else:
    print(-1)