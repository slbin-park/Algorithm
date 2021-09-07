import sys

input = sys.stdin.readline
n = int(input())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())
arr.sort(reverse=True)
maxnum = arr[0]
for i in range(1, n):
    if maxnum + (arr[i] - (i)) > maxnum:
        maxnum = maxnum + (arr[i] - (i))
    else:
        break
print(maxnum)