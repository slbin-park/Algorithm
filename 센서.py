import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = []
for i in range(1, n):
    res.append(arr[i] - arr[i - 1])
res.sort(reverse=True)
ans = 0
for i in range(m - 1, n - 1):
    ans += res[i]
print(ans)