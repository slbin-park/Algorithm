import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr = sorted(arr, key=lambda a: a[0])
arr = sorted(arr, key=lambda a: a[1])
last = 0
cnt = 0
for i, j in arr:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
