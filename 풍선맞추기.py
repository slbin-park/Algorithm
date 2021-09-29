import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = [0 for i in range(1000001)]
cnt = 1
res[arr[0] - 1] = 1
for i in range(1, n):
    if res[arr[i]] >= 1:
        res[arr[i]] = 0
        res[arr[i] - 1] += 1
    else:
        cnt += 1
        res[arr[i] - 1] += 1
print(cnt)