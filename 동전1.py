import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
arr2 = [0 for i in range(m + 1)]
arr2[0] = 1
for i in arr:
    for j in range(i, m + 1):
        if j - i >= 0:
            arr2[j] += arr2[j - i]
print(arr2[m])
