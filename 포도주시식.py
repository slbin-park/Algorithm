import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(10000)]
for i in range(n):
    arr[i] = int(input())
d = [0 for _ in range(10000)]
d[0] = arr[0]
d[1] = arr[0] + arr[1]
d[2] = max(arr[0]+arr[2], arr[1]+arr[2], d[1])
for i in range(3, n):
    d[i] = max(d[i-2]+arr[i], arr[i]+arr[i-1]+d[i-3], d[i-1])
print(max(d))
